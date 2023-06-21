@echo off

REM This batch file will update target version (A or B)
REM Target database info are now global parameters
REM on SQL Server

call config.cmd
python2 "P:\ITD\AREA-ADSD CO-ADSD GIS\Projects\PremierOne\P1_Update_only\proc\pyspt\Copy_to_SQLServer - TRNG.py" %1 %servernameTraining% %2 %username% %3 %password%

PAUSE