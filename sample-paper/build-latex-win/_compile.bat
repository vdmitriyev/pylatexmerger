@echo off
echo 'Compiling LaTex to PDF. Please, wait ...'
pdflatex sample-paper
bibtex sample-paper
pdflatex sample-paper
pdflatex sample-paper
REM dvips sample-paper
pdflatex sample-paper
echo 'Ending...'