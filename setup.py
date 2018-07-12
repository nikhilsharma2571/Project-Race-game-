import cx_Freeze

executables = [cx_Freeze.Executable("pygame1.py")]
cx_Freeze.setup(
    name="A bit Racey",
    version="1.1",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar.png"]}},
    executables = executables

    )
from distutils.core import setup
import py2exe

setup(windows=['pygame1.py'])