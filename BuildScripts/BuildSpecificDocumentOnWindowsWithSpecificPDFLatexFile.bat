set /p texFile="Enter filename with full path of the tex-document which should be compiled: "
set /p pdflatexFile="Enter the filename with full path of your pdflatex.exe or leave it empty if it is available as path-variable: "
powershell -File BuildDocumentOnWindows.ps1 -pdfLatexFile %pdflatexFile% -texFile %texFile% -openDocumentAtEnd