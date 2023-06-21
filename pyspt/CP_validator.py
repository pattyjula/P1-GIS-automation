#! python2
# -*- coding: utf-8 -*-
"""
 ---------------------------------------------------------------------------
 PRODUCTION VERSION!
 DATE: Sept 2021
 DESC: CP validation
 AUTHOR: Patty Jula 
 ---------------------------------------------------------------------------
"""
# Import arcpy module
import arcpy, os

# Load required toolboxes
arcpy.ImportToolbox("P:/ITD/AREA-ADSD CO-ADSD GIS/Projects/PremierOne/Tools/PremierOne_45.tbx")

# Script arguments
COMMONPLACE = os.path.join(arcpy.GetParameterAsText(0), "COMMONPLACE") 
print(COMMONPLACE)
# Local variables:
No_Errors = "true"

# Process: Common Place Validator
# Warning: the toolbox C:/PremierOne/Tools/PremierOne_43.tbx DOES NOT have an alias. 
# Please assign this toolbox an alias to avoid tool name collisions
# And replace arcpy.gp.CommonPlaceValidation(...) with arcpy.CommonPlaceValidation_ALIAS(...)
#arcpy.gp.CommonPlaceValidation(COMMONPLACE, "LAPD_NAME", "", "ALIAS_1;ALIAS_2", "", "", "", "CITY", "", "", "", "")
arcpy.gp.CommonPlaceValidation(COMMONPLACE, "LAPD_NAME", "", "ALIAS_1;ALIAS_2", "LAPD_NAME", "", "", "CITY", "", "", "", "")