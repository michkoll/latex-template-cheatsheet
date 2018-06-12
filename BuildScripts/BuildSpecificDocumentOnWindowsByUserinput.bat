set /p texFile="Enter path of the tex-document which should be compiled: "
set /p pdflatexFile="Enter full path of your pdflatex.exe or leave it empty if it is available as path-variable: "
powershell -File BuildOnWindows.ps1 -pdfLatexFile %pdflatexFile% -texFile %texFile%