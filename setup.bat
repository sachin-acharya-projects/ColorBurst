@ echo off
REM CREATE DISTRIBUTIONS
echo [1;36m CREATING DISTRIBUTION FILES
echo python .\setup.py sdist bdist_wheel
python .\setup.py sdist bdist_wheel

REM UPLOADING
echo UPLOADING FILE TO PYPI
echo twine upload dist/*
twine upload dist/*
echo CLEARING UNNECESSARY FILES/FOLDER
echo Deleting Build Directory
rmdir /S /Q build
echo Deleting ChromaticColorBurst.egg-info
rmdir /S /Q ChromaticColorBurst.egg-info
echo [0m Deleting %%~fd