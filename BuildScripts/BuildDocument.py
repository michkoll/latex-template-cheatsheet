from argparse import ArgumentParser
import os
import subprocess

parser = ArgumentParser()
parser.add_argument("-pdf", dest="pdflatexfile", help="pdfLatex file with full path", default="pdflatex")
parser.add_argument("-tex", dest="texfile", help="texFile which should be compiled", default="cheatsheet.tex")

args = parser.parse_args()
pdfLatexArgument=args.texfile + " -synctex=1 -interaction=nonstopmode"
pdfLatexArgument = pdfLatexArgument.replace('\\','/')
os.chdir("..")
subprocess.call([args.pdflatexfile, pdfLatexArgument])