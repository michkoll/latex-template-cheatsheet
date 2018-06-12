set /p pdflatexFile="Enter full path of your pdflatex.exe: "
powershell -File BuildOnWindows.ps1 -pdfLatexFile %pdflatexFile% -texFile cheatsheet.tex