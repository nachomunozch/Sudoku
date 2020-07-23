import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                     "packages": ["pygame", "random", "sys"],
                     "excludes": ['tkinter'],
                     }

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Sudoku",
      version="1.0",
      description="Flap around",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="Sudoku.py", base=base)])
