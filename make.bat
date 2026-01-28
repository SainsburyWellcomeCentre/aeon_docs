@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=src
set BUILDDIR=docs

if "%1" == "" goto help

if not "%1" == "clean" (
	@echo Building API docs...
	python make_api_doctree.py
	python make_acquisition_doctree.py

	@echo Copying example notebooks into 'src'...
	python copy_examples_to_src.py

	@echo Generating People page...
	python make_people_list.py
) else (
	@echo Removing auto-generated files under 'docs' and 'src'...
	rmdir /S /Q %BUILDDIR%
    rmdir /S /Q %SOURCEDIR%\reference\api\
	del /Q %SOURCEDIR%\about\people.md
	@echo Removing copied example notebooks from 'src'...
	del /Q src\user\how_to\*_copy.ipynb
)

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

REM Remove CNAME file from output to prevent setting custom domain on GH Pages
if exist %BUILDDIR%\CNAME del %BUILDDIR%\CNAME
if exist %BUILDDIR%\dirhtml\CNAME del %BUILDDIR%\dirhtml\CNAME
if exist %BUILDDIR%\html\CNAME del %BUILDDIR%\html\CNAME

goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
