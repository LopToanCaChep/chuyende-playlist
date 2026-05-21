
with open("sync_chuyende.ps1", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the loop logic
new_logic = """
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
            Write-Host " LOI: Khong tim thay file $($row.ID_ChuyenDe).html" -ForegroundColor Red
            continue 
        }

        if ([string]::IsNullOrWhiteSpace($row.Mat_Khau)) {
            $destFileName = "$($row.ID_ChuyenDe).html"
            $fileVal = "'chuyende/$destFileName'"
            Write-Host " OK: $($row.Ten_ChuyenDe) -> $destFileName" -ForegroundColor Green
        }
        else {
            $bytes = [System.Text.Encoding]::UTF8.GetBytes($row.Mat_Khau)
            $hashBytes = [System.Security.Cryptography.SHA256]::Create().ComputeHash($bytes)
            $hashString = [System.BitConverter]::ToString($hashBytes).Replace('-', '').ToLower()
            $destFileName = "chuyende_$hashString.html"
            $hasPassword = "true"
            Write-Host " OK (MAT KHAU): $($row.Ten_ChuyenDe) -> Ma hoa" -ForegroundColor Yellow
        }

        $destPath = Join-Path $DestDir $destFileName
        Copy-Item -Path $sourcePath -Destination $destPath -Force
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
"""

import re
# Find from "if ($row.Trang_Thai -ne "Hien") {" to "$jsonArr += $jsonObj"
pattern = r"if \(\$row\.Trang_Thai -ne \"Hien\"\).*?\$jsonArr \+= \$jsonObj"
content = re.sub(pattern, lambda _: new_logic.strip(), content, flags=re.DOTALL)

with open("sync_chuyende.ps1", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated sync_chuyende.ps1")

