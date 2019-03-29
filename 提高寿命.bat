@@echo off
echo.

set tar_file_name=go.bat
set schedual_name=alarm_my_bottom

echo 创建内容
cd C:\Windows\system32

if exist %tar_file_name% (
  schtasks /F /Delete /tn "%schedual_name%"
  del /F %tar_file_name%
  echo 文件%tar_file_name%存在，撤销定时任务
) else (

(echo @@echo off
echo echo. 
echo echo 抬起屁股走一走，包你活到九十九
echo echo.
echo pause
)>go.bat

echo 创建定时任务...
schtasks /create /tn  "%schedual_name%" /tr %tar_file_name% /sc minute /mo 50
echo 再次管理员运行本文件撤销定时任务
)


echo 成功!
echo.

ping 127.0.0.1 -n 6 >nil_9101271531
del /F nil_9101271531