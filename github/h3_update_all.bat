@echo off
echo This will update your complete HarmonyFramework to the latest server version.
echo Press Ctrl+C to abort, any key to continue.
pause > nul

rem 设置本机git工具的路径
set  gitpath="C:\Git\bin\git.exe"

for /f "tokens=*" %%G in ('dir /b /A:D') do (
	echo.
	echo Updating [%%G]
	cd %%G
	%gitpath% fetch
	%gitpath% checkout .
	%gitpath% checkout master
	%gitpath% reset --hard origin/master
	%gitpath% clean -fx
	%gitpath% clean -fd
	%gitpath% log -n 1 --oneline
	cd..
)