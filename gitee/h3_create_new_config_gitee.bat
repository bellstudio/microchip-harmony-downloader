
@echo **************************************************
@echo *   This will REMOVE all existing config files   *
@echo *  ALL features are turned off after generating  *
@echo * Please manual edit config file after generated *
@echo **************************************************
@echo OFF
pause


set  gitpath="C:\Git\bin\git.exe"

IF EXIST catalog (
	@echo update catalog files
	cd .\catalog
	%gitpath% fetch
	%gitpath% checkout .
	%gitpath% checkout master
	cd ..
	) ELSE (
	@echo No existing catalog file
	@echo Clone catalog file from github
	%gitpath% clone https://gitee.com/Microchip-MPLAB-Harmony/catalog.git
	)
pause
@echo.Remove old configuration files...
del /Q h3gitee*.ini
@echo. Searching Device...
python decode_catalog.py -f configfile -t devices >> h3gitee_devices_config.ini
@echo. Searching APIs...
python decode_catalog.py -f configfile -t api >> h3gitee_libs_config.ini
@echo. Searching Document...
python decode_catalog.py -f configfile -t documentation >> h3gitee_docs_config.ini
@echo. Searching app_demo...
python decode_catalog.py -f configfile -t application >> h3gitee_app_config.ini
@echo. Searching external libs...
python decode_catalog.py -f configfile -t external >> h3gitee_external_config.ini

@echo New config files generated with success!