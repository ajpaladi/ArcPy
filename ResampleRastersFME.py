#ResampleRaster.py
#This script takes two rasters and resamples them, primary used for post FME Conversion
#Script by Andrew Paladino

import arcpy
arcpy.env.overwriteOutput = True

#input path to Kiewit RGB post conversion
RGBraster = r"W:\Operations\Kiewit\6_23_2020\Projected\RGB\RGB_USft_To_Feet_Conversion.tif"
OutputRGB = r"W:\Operations\Kiewit\6_23_2020\Projected\RGB"

#input path to Kiewit DSM raster post conversion
DSMraster = r"W:\Operations\Kiewit\6_23_2020\Projected\DSM\DSM_USft_To_Feet_Conversion.tif"
OutputDSM = r"W:\Operations\Kiewit\6_23_2020\Projected\DSM"

print("Resampling Rasters...")

SaveRGB = OutputRGB + "/" + "RGB_Resampled.tif" 
arcpy.Resample_management(RGBraster, SaveRGB, 0.3, "CUBIC")

print("\nRGB Resampled and saved to: {0}".format(OutputRGB))

SaveDSM = OutputDSM + "/" + "DSM_Resampled.tif" 
arcpy.Resample_management(DSMraster, SaveDSM, 0.3, "CUBIC")

print("\nDSM Resampled and saved to: {0}".format(OutputDSM))
print("\nScript Completed!")
