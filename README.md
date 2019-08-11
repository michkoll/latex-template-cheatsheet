# latex-template-cheatsheet

## Summary

Generating cheatsheets for any topic easily. Download the <a href="https://github.com/michkoll/cheatsheet-forensics/raw/master/cheatsheet.pdf" target="_blank">current forensics-cheatsheet</a> to see an example.

Feel free to contribute to this project!

## Getting started

* Create a new repository and add this repository as submodule in a folder called `template`. (You may use `git submodule add https://github.com/michkoll/latex-template-cheatsheet.git template`.)
* Create a tex-file and write down your content
* Reference your tex-files in `entire-content.tex` relative to the `template`-directory.
* Run `template/BuildScripts/BuildDocument.py`.

This process can be automated. You must only execute the following commands

```
git clone https://github.com/michkoll/latex-template-cheatsheet.git
cd latex-template-cheatsheet
python CreateNew.py C:\myFolderForCheatsheets mycheatsheettitle
```

This will create a new repository with a cheatsheet. In `C:\myFolderForDocuments\entire-content.tex` you can edit the content of yout cheatsheet. The generated pdf-document is located at `C:\myFolderForDocuments\cheatsheet.pdf`.

# Requirements

To get the create- and build-script working the following commands must be available on your system:
* python
* git
* pdflatex
