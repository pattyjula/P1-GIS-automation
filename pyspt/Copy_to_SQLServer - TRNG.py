# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Copy_to_SQLServer.py
# Created on: 2018-04-30 09:12:39.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: Transfer Staging GDB to SQL Server, set A or B
# Changed message severity level to 2 in Feb 2019 to improve speed
# AUTHOR: Patty J
# ---------------------------------------------------------------------------
print(
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This process transfers staging data to the Training SQLServer
Results write to the log file: 
../logs/trainingServer_results.log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
)
    
import os, sys
# Import arcpy module
import arcpy
from art import *
from datetime import datetime
old_stdout = sys.stdout

servernameTraining = sys.argv[1]
usernameTraining = sys.argv[2]
passwordTraining = sys.argv[3]
# Local variables:
version_val = raw_input('Enter the version to be updated (A or b):')
version = version_val.upper() 
print(version)
sp = 'P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/P1_Update_only/Staging/'
stagingGDB = 'StagingGDB.gdb'
# Load required toolboxes
arcpy.ImportToolbox("P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/Tools/PremierOne_45.tbx")
txtFile = open("P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/P1_Update_only/logs/trainingServer_results.log","w")
print("Script start time: " + str(datetime.now()))
txtFile.write("Script start time: " + str(datetime.now())+"\n")
if version =="A" or version =="B":
    StagingGDB_gdb = sp + stagingGDB
    No_Errors = ""
    print("Transferring content from STAGING to TRAINING Server version: " +version+ "\n")
    txtFile.write("Transferring content from STAGING to TRAINING Server version: " +version+ "\n")
    # Process: Copy Geodatabase To SQL Server
    # Warning: the toolbox C:/PremierOne/Tools/PremierOne_44.tbx DOES NOT have an alias. 
    # Please assign this toolbox an alias to avoid tool name collisions
    # And replace arcpy.gp.CopyGeodatabaseToSql(...) with arcpy.CopyGeodatabaseToSql_ALIAS(...)
    arcpy.gp.CopyGeodatabaseToSql(StagingGDB_gdb, servernameTraining, "GISSQL_DATASET_" + version, username, password, "true", "true")
    txtFile.write(arcpy.GetMessages(2))

    txtFile.write("\n"+"End of File!!!"+"\n")
    Art=text2art("Go GIS!","random")

    print(Art)
    
    txtFile.write(
    "Script end time: " + str(datetime.now()))
    txtFile.close()
else:
    print("\n Please review your inputs")
    txtFile.write("Script end time: " + str(datetime.now()))
    txtFile.close()
    pass
    
