
# latex-template-cheatsheet

Generating easy cheatsheets for different topics. Download the <a href="https://github.com/michkoll/latex-template-cheatsheet/raw/cheatsheet-forensics/cheatsheet.pdf" target="_blank">current cheatsheet</a> to see an example.

## Using

* create directory with topic name
* create topic specific TeX-File in new directory
* Copy & Paste multicols-Code in the new file
* Begin

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
