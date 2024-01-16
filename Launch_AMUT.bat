@echo off

rem Step 1 Run ComfyUI
cd ComfyUI_windows_portable
start run_nvidia_gpu.bat

rem Wait for ComfyUI to start (adjust the timeout as needed)
timeout /t 5 /nobreak > nul

rem Step 2 Run Flask Server
@echo off
cd "..\python"
start python server.py


rem Wait for the server to start (adjust the timeout as needed)
timeout /t 5 /nobreak > nul

rem Step 3 Open HTML in Browser
cd "..\"
start python -m http.server 5500
start "" "http://127.0.0.1:5500"


rem Keep the command prompt window open to see any server logs
pause
