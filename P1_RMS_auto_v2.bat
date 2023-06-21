@echo off
REM testing for RMS update, pj 12/14/22
REM Global variables
REM Calling config.cmd
call config.cmd
echo ******************
echo Starting P1_autoRMS.bat
echo Running validators, running MAP Update on CP and CL
echo Creating staging and importing files
echo Handles DOT and Ports imports
echo ******** WARNING ******** 
echo The toolbox: PremierOne_45.tbx
echo must be located in:
echo P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/Tools
echo LOG FILE LOCATION for this script:
echo P:\ITD\AREA-ADSD CO-ADSD GIS\Projects\PremierOne\P1_Update_only\logs\stagingResultRMS.log
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ----- Brought to you by ECCCSD/GTU -----
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

REM *************************************
REM Run Map DATE update and valdiation on COMMONPLACE and STREET in PrepGDB
REM CAUTION  Prep GDB most not be open in Arc software to prevent lock errors
REM transfer latest PrepGDB.gdb to the proper folder prior
REM  to running this batch file
REM *************************************

call config.cmd
REM Command to open folder
%SystemRoot%\explorer.exe %1 pth_V

%SystemRoot%\explorer.exe "P:\ITD\AREA-ADSD CO-ADSD GIS\Projects\PremierOne\P1_Update_only\logs"

REM *************************************
REM Run validator on commonplace and streets
python2 "P:\ITD\AREA-ADSD CO-ADSD GIS\Projects\PremierOne\P1_Update_only\proc\pyspt\CP_validator.py" %1 %ml%
python2 "P:\ITD\AREA-ADSD CO-ADSD GIS\Projects\PremierOne\P1_Update_only\proc\pyspt\Street_validator.py" %1 %ml%

REM Add map date to commonplace and streets
REM *************************************
python2 "P:\ITD\AREA-ADSD CO-ADSD GIS\Projects\PremierOne\P1_Update_only\proc\pyspt\CP_MD.py" %1 %ml% %2 %map_date% %3 %cp_date_prev%
python2 "P:\ITD\AREA-ADSD CO-ADSD GIS\Projects\PremierOne\P1_Update_only\proc\pyspt\St_MD.py" %1 %ml% %2 %map_date%

REM *************************************
REM Run Staging file creation from PrepGDB input gdb
python2 "P:\ITD\AREA-ADSD CO-ADSD GIS\Projects\PremierOne\P1_Update_only\proc\pyspt\P1_prod_version_v5.py" %1 %ml% %2 %gdb_P%
PAUSE