# latex-template-cheatsheet

## Summary

Generating easy cheatsheets for different topics. Download the <a href="https://github.com/michkoll/latex-template-cheatsheet/raw/master/cheatsheet.pdf" target="_blank">current forensics-cheatsheet</a> to see an example.

<details>
	<summary>
		All available cheatsheets (from <a href="https://github.com/anionDev" target="_blank">AnionDev</a>-fork)
	</summary>
	<p>
		<a href="https://github.com/anionDev/latex-template-cheatsheet/raw/cheatsheet-com/cheatsheet.pdf" target="_blank">COM</a>
		<a href="https://github.com/anionDev/latex-template-cheatsheet/raw/cheatsheet-cryptography/cheatsheet.pdf" target="_blank">Kryptographie</a>
		<a href="https://github.com/anionDev/latex-template-cheatsheet/raw/cheatsheet-forensics/cheatsheet.pdf" target="_blank">Forensik</a>
		<a href="https://github.com/anionDev/latex-template-cheatsheet/raw/cheatsheet-git/cheatsheet.pdf" target="_blank">Git</a>
		<a href="https://github.com/anionDev/latex-template-cheatsheet/raw/cheatsheet-penetrationtests/cheatsheet.pdf" target="_blank">Penetrationstests</a>
		<a href="https://github.com/anionDev/latex-template-cheatsheet/raw/cheatsheet-programming-languages/cheatsheet.pdf" target="_blank">Programmiersprachen</a>
		<a href="https://github.com/anionDev/latex-template-cheatsheet/raw/cheatsheet-theoretical-computer-science/cheatsheet.pdf" target="_blank">Theoretische Informatik</a>
	</p>
</details>

## Getting started

* create branch with topic name
* create topic specific TeX-File in new directory
* Copy & Paste multicols-Code in the new file
* Start writing

Feel free to contribute to this project!
## Template-Body

```latex
%Body for every cheatsheet
\raggedright
\footnotesize
\begin{multicols}{3}	
	% multicol parameters
	% These lengths are set only within the two main columns
	%\setlength{\columnseprule}{0.25pt}
	\setlength{\premulticols}{1pt}
	\setlength{\postmulticols}{1pt}
	\setlength{\multicolsep}{1pt}
	\setlength{\columnsep}{2pt}

\begin{center}
     \Large{\underline{Sample}} \\
\end{center}

\section{Section 1}
Text
\subsection{xCode}
Subsection text

\section{Section 2}
Text 2

\section{Section 3}
Etc.

% You can even have references
\rule{0.3\linewidth}{0.25pt}
\scriptsize
\bibliographystyle{abstract}
\bibliography{refFile}
\end{multicols}
```
