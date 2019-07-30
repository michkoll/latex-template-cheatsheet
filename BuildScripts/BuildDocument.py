from argparse import ArgumentParser
import os
import subprocess
parser = ArgumentParser()
parser.add_argument("-pdf", dest="pdflatexfile", help="pdfLatex file with full path", default="pdflatex")
args = parser.parse_args()
pdfLatexArgument="\"\input{cheatsheet.tex}\" -synctex=1 -interaction=nonstopmode -job-name cheatsheet -halt-on-error -output-directory .."
os.chdir("..")
subprocess.call(args.pdflatexfile + " " + pdfLatexArgument)
