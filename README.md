+++++++++++

# P1&RMS/GIS Update Procedures

+++++++++++

## Quick Start Guide

============================

- Write 5 - 10 tests based on recent street, commonplace, boundary edits for the Communications Division to test in the file located one level../P1 tests.xlsx

- Transfer the most recent nightly back-up GDB from the PremierOne/Date_timecapsule folder to the ../PrepGDB folder and rename that file to PrepGDB.gdb; Double check the data present 

- Run the commonplace and street attributions (Assign Values to Commonplace and Assign Values to Streets) in ArcCatalog from the toolbox ECCCSD/GTU.tbx

- Update path variables found in config.cmd depending on your computer paths ands the map date

- Double click to run P1_RMS_auto_v2.bat - this contains the zipcode and other needs for RMS (the P1_auto_v1.bat was used previously, before RMS)

- the Staging GDB transfers to the ../MapData folder, delete previous gdb and rename the Staging GDB to whatever you deleted

- View the map and map date in ArcMap, review data to check integrity of results

- If map checks out, run P1_sql_TrainingServer.bat

- Ask dispatch to review tests created above

- If all checks out, run P1_sql_Production.bat and ask designated party to switch the sets

## Reminder

============================

- Make sure that you write to inactive set for Training and Production updates. Work with ECCCSD (Howard) to get the correct set.


### ReadMe Info

============================  
Created by: P Jula to provide to Motorla, 3/1/2023  
Last updated: P Jula, 6/6/2023 

