@echo off

set url1=https://raw.githubusercontent.com/Dimbreath/WutheringData/master/TextMap/en/MultiText.json
set output1=MultiText.json

set url2=https://raw.githubusercontent.com/Dimbreath/WutheringData/master/ConfigDB/Skill.json
set output2=Skill.json

curl -L -o %output1% %url1%
curl -L -o %output2% %url2%

echo Files downloaded: %output1%, %output2%
pause