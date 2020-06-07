from subprocess import Popen, PIPE
import pathlib
from pathlib import Path
import os
process = Popen(["arara", "cheatsheet.tex"])
(output, err) = process.communicate()
exit_code = process.wait()
if(exit_code!=0):
    raise Exception("Compiling cheatsheet resulted in exitcode "+str(exit_code))
os.rename("cheatsheet.pdf",".."+os.path.sep+os.path.basename(Path(pathlib.Path(__file__).parent.absolute()).parent)+".pdf")

