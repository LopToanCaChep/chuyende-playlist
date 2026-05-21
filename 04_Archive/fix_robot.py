# -*- coding: utf-8 -*-

with open("sync_chuyende.ps1", "r", encoding="utf-8") as f:
    c = f.read()

# Replace the "LOI + continue" with just a warning (no continue)
c = c.replace(
    """        if (-not (Test-Path $sourcePath)) { 
            Write-Host " LOI: Khong tim thay file $($row.ID_ChuyenDe).html" -ForegroundColor Red
            continue 
        }""",
    """        if (-not (Test-Path $sourcePath)) { 
            Write-Host " CHUA CO FILE: $($row.Ten_ChuyenDe) - Van hien thi the" -ForegroundColor DarkYellow
            $hasPassword = "true"
        }
        else {"""
)

# Need to close the else block - find the copy line and add closing brace after it
c = c.replace(
    """        $destPath = Join-Path $DestDir $destFileName
        Copy-Item -Path $sourcePath -Destination $destPath -Force
    } else {""",
    """        $destPath = Join-Path $DestDir $destFileName
        Copy-Item -Path $sourcePath -Destination $destPath -Force
        }
    } else {"""
)

with open("sync_chuyende.ps1", "w", encoding="utf-8") as f:
    f.write(c)

print("Done - Robot updated")
