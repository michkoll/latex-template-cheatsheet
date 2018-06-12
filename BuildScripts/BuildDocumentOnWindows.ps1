Param(
  [string]$pdfLatexFile,#this parameter is not required if pdflatex.exe is available in the path-variable. Execute 'setx /M PATH "%PATH%;C:\my\pdfLatex\Folder"' as administrator for this purpose but be careful about the maximal length of the content of the path-variable.
  [string]$texFile,#relative path based on the repository-root-folder.
  [switch]$openDocumentAtEnd
)
$argument="$texFile -synctex=1 -interaction=nonstopmode"
$argument = $argument -replace '\\','/'
cd ..
if([string]::IsNullOrEmpty($pdfLatexFile)){
    pdflatex $argument
} else {
    & $pdfLatexFile $argument
}
if($openDocumentAtEnd){
	$fileName=[System.IO.Path]::GetFileNameWithoutExtension($texFile)
	$file="$fileName.pdf"
	Invoke-Item $file
}