import argparse
import os
import sys
import subprocess
import shutil
parser = argparse.ArgumentParser(description='Creates a new formal letter.')

parser.add_argument('folder_for_new_document', help='Specifies the folder where the new document should be stored')
parser.add_argument('document_name', help='Specifies the name of the new document')

args = parser.parse_args()
template_folder=os.path.dirname(os.path.abspath(__file__))

def execute(command:str, argument:str):
    print(subprocess.getoutput(command+" "+argument))

new_document_folder=os.path.join(args.folder_for_new_document,args.document_name)
if(os.path.isdir(new_document_folder)):
    print(new_document_folder + " does already exist")
    sys.exit(1)
os.makedirs(new_document_folder)
os.chdir(new_document_folder)
execute("git", "init")
execute("git", "submodule add "+template_folder+" template")
content_file="entire-content.tex"
content_file_content="TODO"
with open(content_file,'w') as f:
    f.write(content_file_content)
with open("License.txt",'w') as f:
    f.write("Only the author of the content of '"+content_file+"' is allowed to use the content of this repository.")
with open("metadata.tex",'w') as f:
    f.write("\\newcommand{\\cheatsheetcreator}{authorname}\n"+
    "\\newcommand{\\cheatsheetname}{"+args.document_name+"}\n"+
    "\\newcommand{\\customfooter}{Fehler und Verbesserungen inhaltlicher Art bitte melden: \\url{https://example.com/mycheatsheet}}")
shutil.copyfile(os.path.join(template_folder,".gitignore"),os.path.join(new_document_folder,".gitignore"))
os.chdir("template")
execute("Python", "BuildDocument.py")
os.chdir("..")
execute("git", "add -A")
execute("git", 'commit -m "Initial commit"')
