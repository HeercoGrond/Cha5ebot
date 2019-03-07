@echo off
python --version 2>NUL
if errorlevel 1 goto errorNoPython

python .\Cha5ebot.py

pause
goto:eof

:errorNoPython
echo.
echo Error^: Python was not installed, make sure you have ran the install_dependencies file.