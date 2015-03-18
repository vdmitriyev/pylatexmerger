@echo off
echo Converting models from EMF format to EPS ...
echo Files that are converted:

for %%f in (*.emf) do (            
			echo %%~nf
            metafile2eps.exe "%%~nf.emf" "%%~nf.eps"
			cp "%%~nf.eps" ../eps/"%%~nf.eps"
			rm "%%~nf.eps"
	)
	
echo For *.ESP files, please check '../eps/' folder.