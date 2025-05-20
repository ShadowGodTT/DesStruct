@echo off
echo Installing required packages...
pip install -r requirements.txt

echo Building executable...
pyinstaller --noconfirm --onefile --windowed --icon=NONE --add-data "logic;logic" --name "DesStruct" run_desstruct.py

echo Done! The executable is in the dist folder.
pause 