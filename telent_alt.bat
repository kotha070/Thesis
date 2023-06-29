@echo off

setlocal enabledelayedexpansion

set input_file=ip_addresses.txt
set output_file=response_times.txt

REM Remove the output file if it already exists
if exist %output_file% (
  del %output_file%
)

REM Loop through each IP address in the input file
for /F "usebackq delims=" %%G in ("%input_file%") do (
  set ip_address=%%G
  set start_time=!time!

  REM Send GET request using telnet
  telnet %ip_address% 80 << EOF
GET / HTTP/1.1
Host: %ip_address%
Connection: close

EOF

  set end_time=!time!

  REM Calculate response time
  for /F "tokens=1-4 delims=:." %%a in ("%start_time%") do (
    set /A start_seconds=%%a*3600 + %%b*60 + %%c
    set /A start_milliseconds=%%d
  )

  for /F "tokens=1-4 delims=:." %%a in ("%end_time%") do (
    set /A end_seconds=%%a*3600 + %%b*60 + %%c
    set /A end_milliseconds=%%d
  )

  set /A response_time_seconds=end_seconds - start_seconds
  set /A response_time_milliseconds=end_milliseconds - start_milliseconds

  if !response_time_milliseconds! LSS 0 (
    set /A response_time_seconds=response_time_seconds - 1
    set /A response_time_milliseconds=response_time_milliseconds + 1000
  )

  REM Append IP address and response time to the output file
  echo !ip_address! !response_time_seconds!.!response_time_milliseconds! >> %output_file%
)

echo Done.

