
SETLOCAL
rem Please modify this according to your own system setting
set  gitpath="C:\Git\bin\git.exe"


@echo OFF
rem DO NOT modify other contents

if "%~1"=="/h" (
	@echo.This is a batch file create files according to catalog file configuration
	@echo.User should modify configuration files after creating
	@echo.All modules are disabled by default
	@echo.
	@echo.Usage:
	@echo.h3_create_new_config_github.bat [/h] [-h] [/update]
	@echo. /h, -h	    Show help information
	@echo. /update 	    Try update local catalog files even existed
	@echo.
	@echo. -- eg. C:\harmony\h3_create_new_config_github.bat /h
	@echo.    This will display this help screen
	goto end
	)
if "%~1"=="-h" (
	@echo.This is a batch file create files according to catalog file configuration
	@echo.User should modify configuration files after creating
	@echo.All modules are disabled by default
	@echo.
	@echo.Usage:
	@echo.h3_create_new_config_github.bat [/h] [-h] [/update]
	@echo. /h, -h	Show help information
	@echo. /update 	    Try update local catalog files even existed
	@echo.
	@echo. -- eg. C:\harmony\h3_create_new_config_github.bat /h
	@echo.    This will display this help screen
	goto end
	)

@echo.	
@echo.      *------------------------------------------------*
@echo.      *   This will REMOVE all existing config files   *
@echo.      *  ALL features are turned off after generating  *
@echo.      * Please manual edit config file after generated *
@echo.      *------------------------------------------------*
@echo.
@echo OFF
pause
	
IF EXIST catalog (
	if "%~1"=="/update" (
		@echo update catalog files
		cd .\catalog
		%gitpath% fetch
		%gitpath% checkout .
		%gitpath% checkout master
		cd ..
		)
	) ELSE (
	@echo No existing catalog file
	@echo Clone catalog file from github
	%gitpath% clone https://github.com/Microchip-MPLAB-Harmony/catalog.git
	)

@echo.Remove old configuration files...
del /Q h3github*.ini
@echo. Searching Device...
python decode_catalog.py -f configfile -t devices >> h3github_devices_config.ini
@echo. Searching APIs...
python decode_catalog.py -f configfile -t api >> h3github_lib_config.ini
@echo. Searching Documents...
python decode_catalog.py -f configfile -t documentation >> h3github_docs_config.ini
@echo. Searching app_demos...
python decode_catalog.py -f configfile -t application >> h3github_app_config.ini
@echo. Searching external libs...
python decode_catalog.py -f configfile -t external >> h3github_external_config.ini

@echo New config files generated with success!

:end
ENDLOCAL