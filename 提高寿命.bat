@@echo off
echo.

set tar_file_name=go.bat
set schedual_name=alarm_my_bottom

echo ��������
cd C:\Windows\system32

if exist %tar_file_name% (
  schtasks /F /Delete /tn "%schedual_name%"
  del /F %tar_file_name%
  echo �ļ�%tar_file_name%���ڣ�������ʱ����
) else (

(echo @@echo off
echo echo. 
echo echo ̧��ƨ����һ�ߣ�������ʮ��
echo echo.
echo pause
)>go.bat

echo ������ʱ����...
schtasks /create /tn  "%schedual_name%" /tr %tar_file_name% /sc minute /mo 50
echo �ٴι���Ա���б��ļ�������ʱ����
)


echo �ɹ�!
echo.

ping 127.0.0.1 -n 6 >nil_9101271531
del /F nil_9101271531