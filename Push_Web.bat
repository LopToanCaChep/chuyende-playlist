@echo off
chcp 65001 >nul
echo ==============================================
echo  DONG BO CHUYEN DE LEN WEB - TOAN CA CHEP
echo ==============================================
echo.

powershell.exe -ExecutionPolicy Bypass -File ".\sync_chuyende.ps1"

echo.
pause
