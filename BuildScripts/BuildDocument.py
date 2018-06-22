from argparse import ArgumentParser
import os
import subprocess
parser = ArgumentParser()
parser.add_argument("-pdf", dest="pdflatexfile", help="pdfLatex file with full path", default="pdflatex")
parser.add_argument("-tex", dest="texfile", help="texFile which should be compiled", default="entire-content.tex")
args = parser.parse_args()
pdfLatexArgument="\"\input{overhead/first-part.tex}\input{"+args.texfile+"}\input{overhead/last-part.tex}\" -synctex=1 -interaction=nonstopmode -job-name cheatsheet"
os.chdir("..")
subprocess.call(args.pdflatexfile + " " + pdfLatexArgument)
