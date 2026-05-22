$ErrorActionPreference = "Stop"

# ===========================================================
# CHUYEN DE HUB - SYNC SCRIPT (Premium v2)
# Toan Ca Chep - 2026
# ===========================================================

# Load shared library
. "$PSScriptRoot\..\..\03_Automation\sync_lib.ps1"
$CsvPath = ".\quan_ly_chuyen_de.csv"
$SourceDir = ".\03_Outputs"
$DestDir = ".\chuyende"
$HtmlPath = ".\index.html"

Write-Host ""
Write-Host "=========================================" -ForegroundColor Magenta
Write-Host "  ROBOT CHUYEN DE - BUILD & PUSH" -ForegroundColor Magenta
Write-Host "=========================================" -ForegroundColor Magenta

# 1. Kiem tra thu muc
if (-not (Test-Path $SourceDir)) { New-Item -ItemType Directory -Path $SourceDir -Force | Out-Null }
if (-not (Test-Path $DestDir)) { New-Item -ItemType Directory -Path $DestDir -Force | Out-Null }

# 2. Doc CSV hien tai
if (Test-Path $CsvPath) {
    $csvData = Import-Csv $CsvPath -Encoding UTF8
} else {
    $csvData = @()
}

# 3. Cap nhat So_Cau cho cac chuyen de hien co neu co file HTML tuong ung
$updatedCsv = $false
foreach ($row in $csvData) {
    $expectedPath = Join-Path $SourceDir "$($row.ID_ChuyenDe).html"
    if (Test-Path $expectedPath) {
        $htmlRaw = Get-Content $expectedPath -Raw -Encoding UTF8
        $slideCount = ([regex]::Matches($htmlRaw, 'class="slide"')).Count
        $soCauReal = [Math]::Max($slideCount - 2, 0)
        if ([int]$row.So_Cau -ne $soCauReal) {
            $row.So_Cau = $soCauReal
            $updatedCsv = $true
            Write-Host " CAP NHAT SO CAU: $($row.Ten_ChuyenDe) -> $soCauReal cau" -ForegroundColor Yellow
        }
    } else {
        if ([int]$row.So_Cau -ne 0) {
            $row.So_Cau = 0
            $updatedCsv = $true
            Write-Host " KHONG TIM THAY FILE: $($row.Ten_ChuyenDe) -> Reset So_Cau = 0" -ForegroundColor DarkYellow
        }
    }
}

# 4. Quet file trong Kho Chuyen De va them vao CSV neu chua co
$htmlFiles = Get-ChildItem -Path $SourceDir -Filter "*.html" -File
$newEntriesAdded = $false

$maxIdNum = 0
foreach ($row in $csvData) {
    if ($row.ID_ChuyenDe -match 'chuyende_(\d+)') {
        $num = [int]$Matches[1]
        if ($num -gt $maxIdNum) { $maxIdNum = $num }
    }
}

foreach ($file in $htmlFiles) {
    $fileBase = $file.BaseName
    $alreadyInCsv = $false
    foreach ($row in $csvData) {
        if ("$($row.ID_ChuyenDe).html" -eq $file.Name) { $alreadyInCsv = $true; break }
    }

    if (-not $alreadyInCsv) {
        $maxIdNum++
        $newId = "chuyende_{0:D2}" -f $maxIdNum
        
        # Đổi tên file cho chuẩn
        $newName = "$newId.html"
        $newPath = Join-Path $SourceDir $newName
        if ($file.FullName -ne $newPath) {
            Rename-Item -Path $file.FullName -NewName $newName
        }
        
        # Dem so cau tu file HTML (dem slide)
        $htmlRaw = Get-Content $newPath -Raw -Encoding UTF8
        $slideCount = ([regex]::Matches($htmlRaw, 'class="slide"')).Count
        $soCau = [Math]::Max($slideCount - 2, 0)
        
        $newLine = "$newId,$($fileBase),Toán,12,$soCau,,An"
        Add-Content -Path $CsvPath -Value $newLine -Encoding UTF8
        $newEntriesAdded = $true
        Write-Host " MOI: $($file.Name) -> Da them vao CSV voi ID $newId" -ForegroundColor Green
    }
}

if ($newEntriesAdded) {
    $csvData = Import-Csv $CsvPath -Encoding UTF8
} elseif ($updatedCsv) {
    $csvData | Export-Csv $CsvPath -NoTypeInformation -Encoding UTF8
    $csvData = Import-Csv $CsvPath -Encoding UTF8
}

# 4. Copy sang thu muc /chuyende va build JSON
Write-Host "Don dep thu muc /chuyende..." -ForegroundColor Cyan
Remove-Item -Path "$DestDir\*" -Recurse -Force
$jsonArr = @()

Write-Host "Dang build danh sach chuyen de..." -ForegroundColor Cyan
foreach ($row in $csvData) {
    if ($row.Trang_Thai -eq "An") { 
        Write-Host " Bo qua (AN): $($row.Ten_ChuyenDe)" -ForegroundColor DarkGray
        continue 
    }
    
    $destFileName = ""
    $hasPassword = "false"
    $fileVal = "null"
    $isComingSoon = ($row.Trang_Thai -eq "Coming_Soon")

    if (-not $isComingSoon) {
        $sourcePath = Join-Path $SourceDir "$($row.ID_ChuyenDe).html"
        if (-not (Test-Path $sourcePath)) { 
            Write-Host " CHUA CO FILE: $($row.Ten_ChuyenDe) - Van hien thi the" -ForegroundColor DarkYellow
            $hasPassword = "true"
        }
        else {

        if ([string]::IsNullOrWhiteSpace($row.Mat_Khau)) {
            $destFileName = "$($row.ID_ChuyenDe).html"
            $fileVal = "'chuyende/$destFileName'"
            Write-Host " OK: $($row.Ten_ChuyenDe) -> $destFileName" -ForegroundColor Green
        }
        else {
            $destFileName = Get-HashedFileName -Password $row.Mat_Khau -Prefix "chuyende_"
            $hasPassword = "true"
            Write-Host " OK (MAT KHAU): $($row.Ten_ChuyenDe) -> Ma hoa" -ForegroundColor Yellow
        }

        $destPath = Join-Path $DestDir $destFileName
        Copy-Item -Path $sourcePath -Destination $destPath -Force
        }
    } else {
        Write-Host " COMING SOON: $($row.Ten_ChuyenDe)" -ForegroundColor Cyan
    }

    $numIcon = "CD"
    if ($row.ID_ChuyenDe -match 'chuyende_(\d+)') {
        $numIcon = $Matches[1]
    }
    
    $jsonObj = @"
  {
    id: '$($row.ID_ChuyenDe)',
    file: $fileVal,
    hasPassword: $hasPassword,
    title: '$($row.Ten_ChuyenDe)',
    subject: '$($row.Mon_Hoc)',
    grade: '$($row.Lop)',
    questions: $($row.So_Cau),
    icon: '$numIcon',
    iconStyle: 'blue',
    status: '$($row.Trang_Thai)'
  }
"@
    $jsonArr += $jsonObj
}

# 5. Cap nhat index.html
Write-Host "Cap nhat index.html..." -ForegroundColor Cyan
$jsonStr = $jsonArr -join ",`n"
$htmlContent = Get-Content $HtmlPath -Raw -Encoding UTF8
$pattern = "(?s)const CHUYENDE = \[.*?\];"
$replacement = "const CHUYENDE = [`n$jsonStr`n];"
$newHtmlContent = $htmlContent -replace $pattern, $replacement
Set-Content -Path $HtmlPath -Value $newHtmlContent -Encoding UTF8
Write-Host " Da cap nhat index.html!" -ForegroundColor Cyan

# ============== PHASE 1.5: PRE-PUSH VALIDATION (sync_lib) ==============
$passed = Invoke-PrePushValidation -SchemaKey "list_chuyende" -HtmlScanDir $SourceDir
if (-not $passed) { exit 1 }

# ============== PHASE 2: GITHUB PUSH (sync_lib) ==============
Invoke-GitPush -CommitMessage "Auto-sync Chuyen De $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
