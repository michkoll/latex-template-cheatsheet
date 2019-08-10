# latex-template-cheatsheet

## Summary

Generating easy cheatsheets for different topics. Download the <a href="https://github.com/michkoll/cheatsheet-forensics/raw/master/cheatsheet.pdf" target="_blank">current forensics-cheatsheet</a> to see an example.

## Getting started

* Create a new repository and add this repository as submodule in a folder called `template`. (You may use `git submodule add https://github.com/michkoll/latex-template-cheatsheet.git template`.)
* Create a tex-file and write down your content
* Reference your tex-files in `entire-content.tex` relative to the `template`-directory.
* Run `template/BuildScripts/BuildDocument.py`.

Feel free to contribute to this project!
