#! python2
# -*- coding: utf-8 -*-
"""
 ---------------------------------------------------------------------------
 PRODUCTION VERSION!
 DATE: Sept 2021
 DESC: Automate map date update for street layer, this is helpful
       for users of PremierOne
 AUTHOR: Patty Jula 
 ---------------------------------------------------------------------------
"""
# Import libraries
import os, sys
import arcpy
from datetime import datetime
old_stdout = sys.stdout

try:

    # Input date of street feature class
    
    street = os.path.join(arcpy.GetParameterAsText(0), "STREET")
    street_date = arcpy.GetParameterAsText(1)
    # GET DATE VALUE
    field = "LAPD_NAME"
    cursor = arcpy.UpdateCursor(street)
    for row in cursor:
		row.getValue(field)
		if row.getValue(field) is not None and row.getValue(field).startswith("MAP DATE"):
			row.setValue("LAPD_NAME", "MAP DATE P1 " + street_date)
			cursor.updateRow(row)
			arcpy.AddMessage("Street field value..." + row.getValue(field))
			#printMessages(messages)
			#print(arcpy.GetMessages())
		elif row.getValue(field) is None:
			continue
			
		else:
			continue
    del row
    del cursor
	
except:
    # print error if there's a problem
    print("Unexpected error:", sys.exc_info()[0])
    raise




