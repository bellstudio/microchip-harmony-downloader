	@echo OFF
	rem make all varieables locally not change the OS variables
	SETLOCAL

	@echo ON
	set  gitpath="C:\Git\bin\git.exe"

	@echo OFF
	rem DO NOT modify other content

	@echo OFF
	set demo=0

:BEGIN
	if "%~1"=="/h" (
		@echo.This is a batch file download files according to .ini file configuration
		@echo.All content name and access URLs are located in configuration file
		@echo.
		@echo.Usage:
		@echo.h3-downloader.bat [/h] [-h] [/demo]
		@echo. /h, -h	    Show help information
		@echo. /demo 	    Run in demo mode, only shows download information, no files will be created
		@echo.
		@echo. -- eg. C:\harmony\h3-downloader.bat /h
		@echo.    This will display this help screen
		goto end
		)
		
	if "%~1"=="-h" (
		@echo.This is a batch file download files according to .ini file configuration
		@echo.All content name and access URLs are located in configuration file
		@echo.
		@echo.Usage:
		@echo.h3-downloader.bat [/h] [-h] [/demo]
		@echo. /h, -h	Show help information
		@echo. /demo 	Run in demo mode, only shows download information, no files will be created
		@echo.
		@echo. -- eg. C:\harmony\h3-downloader.bat /h
		@echo.    This will display this help screen
		goto end
		)
		
	if "%~1"=="/demo" (
		set demo=1
		
		@echo.
		@echo.      *                Now runs in DEMO mode                        *
		@echo.      *     The program will not download ANY file to your disk     *
		
		)
		
	goto content_dispaly

:update_catalog
	rem %gitpath% clone %gitrepo%/catalog.git
	rem %gitpath% clone %gitrepo%/community_catalog.git

:content_dispaly
	@echo.	
	@echo.      *-------------------------------------------------------------*
	@echo.      *  This program will download Harmony Framework from network  * 
	@echo.      *-------------------------------------------------------------*
	@echo.
	@echo.Following content will be downloaded:

	for /f "tokens=*" %%G in ('dir /b h3*.ini') do (
		for /F "eol=; tokens=1,2 delims=, " %%i in (%%G) do (
		@echo. * %%i
		)
	)

	if "%demo%" == "1" (
		goto end
		)

:download

	rem 	pause
rem 	@echo.
	@echo.
	@echo. Press N(n) to stop and quite, ANY other key to start downloading
	set /p permission=
	if "%permission%" == "N" (
		@echo Downloading is terminated by user
		goto end
		)
	if "%permission%" == "n" (
		@echo Downloading is terminated by user
		goto end
		)
		
	for /f "tokens=*" %%H in ('dir /b h3*.ini') do (
		for /F "eol=; tokens=1,2 delims=, " %%i in (%%H) do (
		@echo Starting clone %%j ...
		%gitpath% clone %%j
		) 
	)
	@echo.
	@echo. Downloading complete
	goto end

	echo Wrong way
	
:end
ENDLOCAL
pause
