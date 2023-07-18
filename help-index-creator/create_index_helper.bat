@echo off

@echo.^<!DOCTYPE html^>
@echo.^<html^>
@echo.^<head^>
@echo.^<meta charset="utf-8"^>
@echo.^<title^>Harmony Help Collection^<^/title^>
@echo.^<^/head^>
@echo.^<body^>
@echo.^<h1^>Harmony Help Collection^<^/h1^>


@echo.^<h2^>API Summary^<^/h2^>
for /f "tokens=*" %%G in ('dir /b /A:D') do (
rem 	echo.%%G
	echo %%G|findstr "app" > indexhelper || (
		cd %%G
			if EXIST ./docs/index.html (
							@echo ^<p^>^<a href="./%%G/docs/index.html"^>%%G-help^<^/a^>^<^/p^>
							)
		cd ..
	)
	)
)


@echo.^<h2^>Example App help summary^<^/h2^>
for /f "tokens=*" %%G in ('dir /b /A:D') do (
rem 	echo.%%G
	echo %%G|findstr "app" > indexhelper && (
		cd %%G
			if EXIST ./docs/index.html (
							@echo ^<p^>^<a href="./%%G/docs/index.html"^>%%G-help^<^/a^>^<^/p^>
							)
		cd ..
	)
	)
)

@echo.^<^/body^>
@echo.^<^/html^>