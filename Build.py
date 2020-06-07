from subprocess import Popen, PIPE
import pathlib
from pathlib import Path
import os
process = Popen(["arara", "cheatsheet.tex"])
(output, err) = process.communicate()
exit_code = process.wait()
if(exit_code!=0):
    raise Exception("Compiling cheatsheet resulted in exitcode "+str(exit_code))
filename=".."+os.path.sep+os.path.basename(Path(pathlib.Path(__file__).parent.absolute()).parent)+".pdf"
if os.path.exists(filename):
    os.remove(filename)
os.rename("cheatsheet.pdf",filename)

