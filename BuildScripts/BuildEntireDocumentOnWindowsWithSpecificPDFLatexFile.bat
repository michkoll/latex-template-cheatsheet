set /p pdflatexFile="Enter the filename with full path of your pdflatex.exe: "
powershell -File BuildDocumentOnWindows.ps1 -pdfLatexFile %pdflatexFile% -texFile cheatsheet.tex -openDocumentAtEnd