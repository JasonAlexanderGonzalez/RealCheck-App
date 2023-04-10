import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": []}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="BatteryPercent",
    version="0.1",
    description="Battery level monitoring app",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py", base=base)]
)
