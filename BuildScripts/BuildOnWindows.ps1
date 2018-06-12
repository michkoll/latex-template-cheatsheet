Param(
  [string]$pdfLatexFile,
  [string]$texFile
)
$argument="$texFile -synctex=1 -interaction=nonstopmode"
cd ..
if([string]::IsNullOrEmpty($pdfLatexFile)){
    pdflatex $argument
} else {
    & $pdfLatexFile $argument
}