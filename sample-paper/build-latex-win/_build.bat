pushd ..
del sample-paper.pdf
call build-latex-win/_truncate.bat
REM call build-latex-win/_emf_to_eps_conversion.bat
call build-latex-win/_compile.bat
call build-latex-win/_copy.bat
call build-latex-win/_truncate.bat
call sample-paper.pdf
popd
call _truncate.bat
cls
REM pause