#! python2
# -*- coding: utf-8 -*-
"""
 ---------------------------------------------------------------------------
 PRODUCTION VERSION!
 DATE: Sept 2021
 DESC: Street validation
 AUTHOR: Patty Jula 
 ---------------------------------------------------------------------------
"""
# Import arcpy module
import arcpy, os

# Load required toolboxes
arcpy.ImportToolbox("P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/Tools/PremierOne_45.tbx")

STREET = os.path.join(arcpy.GetParameterAsText(0), "STREET") # provide a default value if unspecified

# Local variables:
No_Errors = "true"

# Process: Street Centerline Validator
# Warning: the toolbox C:/PremierOne/Tools/PremierOne_44.tbx DOES NOT have an alias. 
# Please assign this toolbox an alias to avoid tool name collisions
# And replace arcpy.gp.StreetCenterlineValidation(...) with arcpy.StreetCenterlineValidation_ALIAS(...)
arcpy.gp.StreetCenterlineValidation(STREET, "", "ADLF", "ADLT", "ADRF", "ADRT", "LAPD_NAME", "", "", "L_CITY_ID", "R_CITY_ID", "", "", "")

