#Title: RasterClip
#Script by Andrew Paladino
#Second script using Arcpy YEET

import arcpy

def print_message(msg):
    print(msg)
    arcpy.AddMessage(msg)

arcpy.env.overwriteOutput = True
#Specifyworkspace
arcpy.env.workspace = r"C:\Users\AndrewPaladino\Documents\ArcGIS\Projects\Holstein\Holstein.gdb"

print_message("Starting clip...")

#input raster dataset
InRaster = r"W:\Operations\Holstein\ArcGIS\Orthomosaics\12_18_19_20\19_20\Georect\19_20_RGB_WebM_Georect.tif"

#out raster dataset with \<name.tif>" at the end of the specified path
OutRaster = r"W:\Operations\Holstein\ArcGIS\Orthomosaics\12_18_19_20\19_20\Clipped\19_20_RGB_WebM_Georect_Clip.tif"

#Shapefile to base the clip extent on
ExtentPoly = r"W:\Operations\Holstein\ArcGIS\AGO\6_22_2020\19_20.shp"

clipraster = arcpy.Clip_management(InRaster, None, OutRaster, ExtentPoly, None, "ClippingGeometry", None)

print_message("Clipped Raster saved to {0}".format(OutRaster))
print_message("Script_Completed")

                                   
