#! python2
# -*- coding: utf-8 -*-
"""
 ---------------------------------------------------------------------------
 PRODUCTION VERSION!
 DATE: Sept 2021
 DESC: Automate map date update, this is helpful
       for users of PremierOne
 AUTHOR: Patty Jula 
 ---------------------------------------------------------------------------
"""
#! python2
# Import libraries
import os, sys
import arcpy
from datetime import datetime
old_stdout = sys.stdout

def printMessages(messages):
  '''provide a list of messages to this method'''
  messages = ['Updating map date values']
  for i in messages:
    print i
    #arcpy.AddMessage(i)  #uncomment if using arcpy
if __name__ == '__main__':
  #import arcpy  #uncomment if using arcpy
  messages=[]
  messages.append("Updating map date values...")
  printMessages(messages)

try:

    # Input date of commonplace feature class
    
    commonplace = os.path.join(arcpy.GetParameterAsText(0), "COMMONPLACE")
    cp_date = arcpy.GetParameterAsText(1)
    cp_date_prev = arcpy.GetParameterAsText(2)
    # GET DATE VALUE
    field = "LAPD_NAME"
    field_short = "SHORT_NAME"
    field_prev = "LAPD_EDIT_NOTE"
    cursor = arcpy.UpdateCursor(commonplace)
    for row in cursor:
        row.getValue(field)
        if row.getValue(field) is not None and row.getValue(field).startswith("MAP DATE CP"):
            row.setValue(field, "MAP DATE CP P1 " + cp_date)
            cursor.updateRow(row)
            #arcpy.AddMessage("Commonplace LAPD_NAME value..." + row.getValue(field))
	del row
    del cursor
    
    cursor = arcpy.UpdateCursor(commonplace)
    for row in cursor:
        row.getValue(field_prev)
        
        if row.getValue(field_short) is not None and row.getValue(field_short).startswith("MAP DATE"):
            row.setValue(field_short, "MAP DATE " + cp_date)
            cursor.updateRow(row)
            #arcpy.AddMessage("Commonplace SHORT_NAME value..." + row.getValue(field_short))
    del row
    del cursor
    cursor = arcpy.UpdateCursor(commonplace)
    for row in cursor:
        row.getValue(field_short)     
        
        if row.getValue(field_prev) is not None and row.getValue(field_prev).startswith("New Schema 3-26-19"):

            row.setValue(field_prev, "New Schema 3-26-19 MAP DATE PREVIOUS " + cp_date_prev)
            cursor.updateRow(row)
            #arcpy.AddMessage("Commonplace LAPD_EDIT_NOTE value..." + row.getValue(field_prev))
			
        else:
            continue
    del row
    del cursor
	
except:
    # print error if there's a problem
    print("Unexpected error:", sys.exc_info()[0])
    raise


