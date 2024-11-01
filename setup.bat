@echo off
set VENV_NAME=.venv
set PYTHON=%VENV_NAME%\Scripts\python.exe

REM Check if the virtual environment exists
if exist %VENV_NAME% (
    echo %VENV_NAME% already created. Skipping package installation.
) else (
    echo Creating virtual environment and installing packages...
    python -m venv %VENV_NAME%
    %PYTHON% -m pip install -U pip
    %PYTHON% -m pip install -Ur requirements.txt
)

REM Run the Python script after setting up the virtual environment
echo Running script.py...
%PYTHON% script.py