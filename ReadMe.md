# LaTeX templates for cheatsheets

## Summary

Generating cheatsheets for any topic easily. Download the [forensics-cheatsheet-document](https://github.com/michkoll/cheatsheet-forensics/raw/master/cheatsheet-forensics.pdf) to see an example.

Feel free to contribute to this project!

## Getting started

Create a new repository (`git init`) and add this repository as submodule in a folder called `template`. (You may use `git submodule add https://github.com/michkoll/latex-template-cheatsheet.git template`.) Then create a file like `my-cheatsheet.tex` on the toplevel of your repository with the following content:

``` TeX
% arara: pdflatex

% metadata:
\newcommand{\cheatsheetcreator}{My name}
\newcommand{\cheatsheetname}{My cheatsheet title}
\newcommand{\customfooter}{My custom footer}

\input{template/Template/cheatsheet-template-prefix.tex}

% cheatsheet content:
% <your cheatsheet-content>

\input{template/Template/cheatsheet-template-suffix.tex}
```

Then you simply call `arara my-cheatsheet.tex` to compile your document.

See the content of the [forensics-cheatsheet-repository](https://github.com/michkoll/cheatsheet-forensics) for an example.

## Requirements

To get this working the following commands must be available on your system:

* git (only for cloning)
* pdflatex
* [arara](https://gitlab.com/islandoftex/arara) (also contained in TeX-distributions like [TeX Live](https://www.tug.org/texlive))

## License

This repository is licensed under the terms of the [MIT-license](https://raw.githubusercontent.com/michkoll/latex-template-cheatsheet/master/License.txt).
