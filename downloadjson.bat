@echo off

set url1=https://raw.githubusercontent.com/Dimbreath/WutheringData/master/TextMap/en/MultiText.json
set output_file1=MultiText.json

set url2=https://raw.githubusercontent.com/Dimbreath/WutheringData/master/ConfigDB/Skill.json
set output_file2=Skill.json

curl -L -o %output_file1% %url1%
curl -L -o %output_file2% %url2%

echo Files downloaded: %output_file1%, %output_file2%
pause