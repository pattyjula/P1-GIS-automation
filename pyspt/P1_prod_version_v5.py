#! python2
# -*- coding: utf-8 -*-
"""
 ---------------------------------------------------------------------------
 PRODUCTION VERSION!
 DATE: Sept 2021
 DESC: Automate creation of StagingGDB.gdb
 AUTHOR: Jula
 NOTE: Update for RMS 03/2023
 ---------------------------------------------------------------------------
"""

# Import libraries
import os
import sys

import datetime

import arcpy

old_stdout = sys.stdout

# Import customized Motorola tools
arcpy.ImportToolbox(
    "P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/Tools/PremierOne_45.tbx"
)
fldr = "P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/P1_Update_only/staging"
arcpy.env.workspace = fldr

try:

    # Open text file for logging
    txtFile = open(
        "P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/P1_Update_only/logs/stagingResultRMS.log",
        "w",
    )
    ml_gdb = "P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/P1_Update_only/MapData/StagingGDB.gdb"
    print("GDB creation start time: " + str(datetime.datetime.now()) + "\n")
    txtFile.write("Script start time: " + str(datetime.datetime.now()))
    ml = arcpy.GetParameterAsText(0)
    gdb = arcpy.GetParameterAsText(1)
    street = ml + "STREET"
    # Get tables related to streets
    StandardizationExceptions = gdb + "StandardizationExceptions"
    STREETNAMEALISES = gdb + "STREETNAMEALIAS"
    # Motorola XML files - p1g schema updated 9/9/21 for 45 version -pj
    NetworkXML = "P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/P1_Update_only/config/NetworkDatasetParamsLAPD_20170919.xml"
    P1GDB_Schema = (
        "C:/Program Files (x86)/Motorola/PremierOne Data Import Tools/P1GDBSchema.xml"
    )
    # Staging vars
    sp = "P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/P1_Update_only/Staging/"
    stagingGDB = "StagingGDB.gdb"
    oldGDB = "StagingGDB_old.gdb"
    arcpy.env.workspace = sp
    commonplace = ml + "COMMONPLACE"
    R_D = ml + "POLICE"  # POLICE
    DOT = ml + "DOT_RD"  # DOT
    PP = ml + "PP_RD"  # PP

    # Rename former gdb to .._old and create a new one
    if arcpy.Exists(stagingGDB) is True and arcpy.Exists(oldGDB) is False:
        arcpy.Rename_management(stagingGDB, oldGDB)
        arcpy.Delete_management(stagingGDB)
        txtFile.write(arcpy.GetMessages(0))

    elif arcpy.Exists(stagingGDB) is True and arcpy.Exists(oldGDB) is True:
        arcpy.Delete_management(oldGDB)
        arcpy.Rename_management(stagingGDB, oldGDB)
        arcpy.Delete_management(stagingGDB)
        txtFile.write(arcpy.GetMessages(0))

    else:
        pass

    # Process: Remove tilde (~) from Postal city left and right in street, PJ 1/11/23
    fieldList = ["L_POSTAL", "R_POSTAL"]
    if fieldList:
        with arcpy.da.UpdateCursor(street, fieldList) as cursor:
            for row in cursor:
                for i in range(len(fieldList)):
                    try:
                        if row[i][:1] in ["~"]:
                            row[i] = row[i][1:]
                            cursor.updateRow(row)
                    except:
                        pass

    # Process: Remove tilde (~) from Postal city left and right in cp, PJ 1/11/23
    fieldList = ["POSTAL"]
    if fieldList:
        with arcpy.da.UpdateCursor(commonplace, fieldList) as cursor:
            for row in cursor:
                for i in range(len(fieldList)):
                    try:
                        if row[i][:1] in ["~"]:
                            row[i] = row[i][1:]
                            cursor.updateRow(row)
                    except:
                        pass

    # Process: Create PremierOne Geodatabase and import schema
    arcpy.CreateFileGDB_management(fldr, stagingGDB)
    arcpy.gp.CreatePremierOneGeodatabase(stagingGDB, P1GDB_Schema)

    txtFile.write(
        "*****************STARTED STAGING GDB DATA IMPORT *****************" + "\n"
    )
    txtFile.write("... Importing STREET\n")
    # Process: Street Centerline Import
    # Add zip code here pj 12/7/22
    # Added zipcode, state, postal city, pj 12/13/22
    arcpy.gp.StreetCenterlineImport(
        stagingGDB,
        street,
        StandardizationExceptions,
        STREETNAMEALISES,
        "ADLF",
        "ADLT",
        "ADRF",
        "ADRT",
        "LAPD_NAME",
        "",
        "",
        "",
        "L_CITY_ID",
        "R_CITY_ID",
        "L_POSTAL",
        "R_POSTAL",
        "",
        "",
        "",
        "",
        "L_ZIPCODE",
        "R_ZIPCODE",
        "STATE",
    )
    txtFile.write(arcpy.GetMessages(2))

    arcpy.FeatureClassToFeatureClass_conversion(
        street, stagingGDB + "/ROUTING", "STREET_NET"
    )

    try:
        if arcpy.CheckExtension("Network") == "Available":
            arcpy.CheckOutExtension("Network")
        else:
            # raise a custom exception
            txtFile.write(arcpy.GetMessages(0))
            raise LicenseError
    except:
        pass
    # print("Creating network dataset")
    txtFile.write("Creating network dataset" + "\n")
    # Process: Create P1 Network
    arcpy.CreatePremierOneNetworkDataset(
        target_workspace=stagingGDB, input_params=NetworkXML
    )
    txtFile.write(arcpy.GetMessages(2))
    txtFile.write("Importing Commonplace and Response Boundary" + "\n")

    # Import Commonplace
    # Adding zip and postal city, pj 12/13/22
    # Do we need a state field in CP? Yes!
    arcpy.gp.CommonPlaceImport(
        stagingGDB,
        commonplace,
        "LAPD_NAME",
        "",
        "ALIAS_1;ALIAS_2",
        "ADDRESS",
        "",
        "",
        "",
        "",
        "CITY",
        "POSTAL",
        "",
        "",
        "",
        "",
        "ZIPCODE",
        "STATE",
    )
    txtFile.write(arcpy.GetMessages(0))

    # Import response boundaries
    def polyImp(featureClass):
        arcpy.gp.ResponseBoundaryImport(stagingGDB, featureClass, "AGENCY", "NAME")
        txtFile.write("Importing " + featureClass + "\n")
        txtFile.write(arcpy.GetMessages(1))

    polyImp(R_D)
    polyImp(DOT)
    polyImp(PP)

    txtFile.write(
        "\n*****************FINISHED STAGING GDB CREATION *****************\n"
    )

    # Import feature classes
    arcpy.env.workspace = ml
    featureclasses = arcpy.ListFeatureClasses()
    # Copy shapefiles to a file geodatabase
    for fc in featureclasses:
        arcpy.CopyFeatures_management(
            fc, os.path.join(sp + stagingGDB + "/MAP_LAYERS", os.path.splitext(fc)[0])
        )
    # Copy Staging GDB to map data folder
    # Delete all the files EXCEPT MAP_LAYERS
    # and Routing which will not delete from program
    # Delete old gdb in Prep Location and create a new one
    if arcpy.Exists(ml_gdb) is True:
        arcpy.Delete_management(ml_gdb)
        txtFile.write(arcpy.GetMessages(2))
    else:
        pass

    arcpy.Copy_management(sp + stagingGDB, ml_gdb)
    arcpy.env.workspace = ml_gdb
    # Routing needs to be deleted manually
    # Once fixed, the following lines can be uncommented
    try:
        arcpy.Delete_management("Routing")
        # txtFile.write('\n'+'Routing deleted'+'\n')
    except:
        print("Routing not deleted, must do so manually")
        txtFile.write("\n" + "Routing not deleted, must do so manually" + "\n")

    # List tables to prepare for deletion
    tables = arcpy.ListTables()
    for table in tables:
        arcpy.Delete_management(table)

    # List all feature datasets except those that start with M for MAP_LAYERS
    datasets = list(
        set(arcpy.ListDatasets("*", "Feature"))
        - set(arcpy.ListDatasets("RO*", "Feature"))
        - set(arcpy.ListDatasets("M*", "Feature"))
    )
    for d in datasets:
        arcpy.Delete_management(d)

    txtFile.write("Script end time: " + str(datetime.datetime.now()))
    txtFile.close()
    print("Script end time: " + str(datetime.datetime.now()))
    print(
        "Transfer Import and Validation CSV to P1 update only P1_Update_only\DataImportTools drive location"
    )

except:
    # print error if there's a problem
    print("Unexpected error:", sys.exc_info()[0])
    raise
