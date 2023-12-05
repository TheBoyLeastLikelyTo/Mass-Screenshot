@echo off
setlocal enabledelayedexpansion

set "target_directory=%1"
if not defined target_directory (
    echo Please provide a directory.
    exit /b
)

set "target_type=%2"
if not defined target_type (
    echo Please provide a file type.
    exit /b
)

if not exist "%target_directory%" (
    echo Directory does not exist.
    exit /b
)

pushd "%target_directory%"

set i=1

for %%F in (*) do (
    set "filename=000!i!"
    set "filetype=!target_type!"
    set "newname=!filename:~-3!.!filetype!"
    ren "%%F" "!newname!"
    set /a i+=1
)

popd
endlocal
