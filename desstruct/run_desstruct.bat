@echo off
echo Checking Python installation...
python --version
echo.
echo Checking tkinter installation...
python -c "import tkinter; print('Tkinter is installed')"
echo.
echo Starting DesStruct...
python app.py
echo.
echo If you see any errors above, please report them.
pause 