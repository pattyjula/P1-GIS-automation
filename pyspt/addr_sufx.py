# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# new.py
# Created on: 2018-09-13
#               by Patty Jula
# Description: 
# ---------------------------------------------------------------------------

# Import libraries
import os
import arcpy

# Define variables
arcpy.env.workspace = "C:/PremierOne/_Data/Current/PrepGDB.gdb/MAP_LAYERS"
fc = "ADDRESS"
lapd_fld = "LAPD_SUFF"
lapd_dir_sfx = 'LAPD_SUFX_DIR'
#--------------------------------------------------
# Process AddField
# Add lapd suffix field
#arcpy.AddField_management(fc, lapd_fld,'STRING','5','')

# This process queries one field and inputs the required value
# to another field using a dictionary, function with an update cursor
# and a for loop

# Street suffix dictionary
dict ={"STR_SFX_CD = 'AL'" : "ALY","STR_SFX_CD = 'AVE'" : "AV", 
            "STR_SFX_CD = 'BLVD'" : "BL",
            "STR_SFX_CD = 'CIR'" : "CIR","STR_SFX_CD = 'CK'" : "CK",
            "STR_SFX_CD = 'CL'" : "CL",
            "STR_SFX_CD = 'COVE'" : "CV","STR_SFX_CD = 'COURT'" : "CT","STR_SFX_CD = 'CT'" : "CT","STR_SFX_CD = 'CRES'" : "CRES","STR_SFX_CD = 'CYN'" : "CYN",
            "STR_SFX_CD = 'CREEK'" : "CRK", "STR_SFX_CD = 'CK'" : "CRK", "STR_SFX_CD = 'CRK'" : "CRK",
            "STR_SFX_CD = 'DR'" : "DR","STR_SFX_CD = 'GLEN'" : "GLN",
            "STR_SFX_CD = 'GRN'" : "GRN","STR_SFX_CD = 'GY'" : "GY",
            "STR_SFX_CD = 'HILL'" : "HL", "STR_SFX_CD = 'HWY'" : "HWY",
            "STR_SFX_CD = 'LANE'" : "LN","STR_SFX_CD = 'LOOP'" : "LOOP",
            "STR_SFX_CD = 'MALL'" : "MALL",
            "STR_SFX_CD = 'PARK'" : "PK", "STR_SFX_CD = 'PASS'" : "PASS","STR_SFX_CD = 'PROM'" : "PROM", "STR_SFX_CD = 'PROMENADE'" : "PROM",
            "STR_SFX_CD = 'PKWY'" : "PKWY","STR_SFX_CD = 'PLACE'" : "PL","STR_SFX_CD = 'PL'" : "PL","STR_SFX_CD = 'PT'" : "PT",
            "STR_SFX_CD = 'PZ'" : "PLZ",
            "STR_SFX_CD = 'ROAD'" : "RD","STR_SFX_CD = 'RD'" : "RD","STR_SFX_CD = 'RDG'" : "RDG","STR_SFX_CD = 'ROW'" : "ROW",
            "STR_SFX_CD = 'SQ'" : "SQ","STR_SFX_CD = 'SP'" : "SP",
            "STR_SFX_CD = 'ST'" : "ST",
            "STR_SFX_CD = 'TER'" : "TER","STR_SFX_CD = 'TR'" : "TER",
            "STR_SFX_CD = 'TRAIL'" : "TRL", 
            "STR_SFX_CD = 'VIEW'" : "VW","STR_SFX_CD = 'VISTA'" : "VIS","STR_SFX_CD = 'VIS'" : "VIS",
            "STR_SFX_CD = 'WALK'" : "WALK","STR_SFX_CD = 'WAY'" : "WY"}

# Function to update schema to desired values
def update_sufx(where_clause, new_val):
    # Specify feature class field, and query
    with arcpy.da.UpdateCursor(fc, [lapd_fld], where_clause) as cursor:
        # Iterate 
        for row in cursor:
            # Specify proper field value for row
            row[0]= new_val
            # Update row
            cursor.updateRow(row)

# Use for loop and items method to return
# Key value pairs from dictionary
for where_clause, new_val in dict.items():
    # Call function and update values
	update_sufx(where_clause, new_val)

# Add suffix direction
dict_dir ={"STR_SFX_DIR_CD = 'WEST'" : "W","STR_SFX_DIR_CD = 'EAST'" : "E", 
            "STR_SFX_DIR_CD = 'SOUTH'" : "S",
            "STR_SFX_DIR_CD = 'NORTH'" : "N"}

def update_sufx(where_clause, new_val):
    with arcpy.da.UpdateCursor(fc, [lapd_dir_sfx], where_clause) as cursor:
        for row in cursor:
            #print(row)
            row[0]= new_val
            cursor.updateRow(row)

# Run update suffix direction cursor
for where_clause, new_val in dict_dir.items():
	update_sufx(where_clause, new_val)
