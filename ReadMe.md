# latex-template-cheatsheet

## Summary

Generating cheatsheets for any topic easily. Download the [forensics-cheatsheet-document](https://github.com/aniondev/cheatsheet-forensics/raw/master/cheatsheet-forensics.pdf) to see an example.

Feel free to contribute to this project!

## Getting started

* Create a new repository and add this repository as submodule in a folder called `template`. (You may use `git submodule add https://github.com/aniondev/latex-template-cheatsheet.git template`.)
* Create a tex-file and write down your content
* In your repository on the top-level create a  `entire-content.tex` and `metadata.tex`
* Run `template/Build.py`.

`metadata.tex` should contain the following content:
```
\newcommand{\cheatsheetcreator}{Some author}
\newcommand{\cheatsheetname}{Some title}
\newcommand{\customfooter}{Some footer}
```

See the content of the [forensics-cheatsheet-repository](https://github.com/aniondev/cheatsheet-forensics) for an example.

## Requirements

To get the create- and build-script working the following commands must be available on your system:
* python
* pdflatex
* arara (contained in many tex-distributions, e. g. `TeX Live`)
