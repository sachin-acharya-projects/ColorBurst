@ echo off

REM CREATE DISTRIBUTIONS
echo [1;36m CREATING DISTRIBUTION FILES
echo [32m python .\setup.py sdist bdist_wheel
python .\setup.py sdist bdist_wheel

REM UPLOADING
echo [1;36m UPLOADING FILE TO PYPI
echo [32m twine upload dist/*
twine upload dist/*