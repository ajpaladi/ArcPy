#Script by Andrew Paladino | 5/19/2022
#Must have ArcGIS Pro installaed to run
#Ran on Python 3.6.9

import arcpy
import os
import time
from datetime import datetime

arcpy.env.OverwriteOutput = True


#Input GeoTiff Alias
geotiff_alias = "EglinRGBArea3"
#Input Geotiff CaptureDate
geotiff_capturedate = "2020"
#Input Path to GeoTiff
geotiff = r"Z:\mapwaregis\Andy\Eglin_AFB\Raw\SID\2020\Eglin_AFB_26Dec2020_WGS84_utm16_25cm_2of3\Eglin_AFB_26Dec2020_WGS84_utm16_25cm_2of3.sid"
#Input path where you want you deliverable directories created + saved
saveDir = r"Z:\mapwaregis\Andy\Eglin_AFB\PythonTesting\testing"

print("\nCreating Output Directories...")

#Make Two Working Directories for NoDate and Split Rasters
timestr = time.strftime("%m%d%Y-%H%M%S")

nodataRasterDir = saveDir + r"\nodataRasters\\" + timestr + "_" + geotiff_alias + "_" + geotiff_capturedate
if not os.path.exists(nodataRasterDir): 
    os.makedirs(nodataRasterDir)

splitrasterDir = saveDir + r"\splitRasterDir\\" + timestr + "_" + geotiff_alias + "_" + geotiff_capturedate
if not os.path.exists(splitrasterDir):
    os.makedirs(splitrasterDir)

print("\nTwo new save directories have been created! They are:")
print("\n" + nodataRasterDir)
print(splitrasterDir)

#--------------Only execute the below line of code if there is a nodata mask (black or white) around your geotiff --------------#

outputRaster = nodataRasterDir + "/" + geotiff_alias + "_" + geotiff_capturedate + ".tif"
splitrasterBaseName = geotiff_alias + "_" + geotiff_capturedate + "_"

removeNoData = input("\nIs there a NoData mask around your raster than needs to be removed? Print YES or N0... \n\nAnswer:")

if removeNoData == "YES":
    backgroundStatus = input("\nIs the NoData mask around your raster white or black? Print WHITE or BLACK... \n\nAnswer:")
    if backgroundStatus == "WHITE":
        print("\nRemoving NoData background value...")
        white_background = 255
        copyRasterW = arcpy.management.CopyRaster(geotiff, outputRaster, 0, white_background)
        print("\nNoData mask removed! Proceeding to the SplitRaster function...")
        print("\nSplitting Raster")
        splitRasterW = arcpy.management.SplitRaster(copyRasterW, splitrasterDir, splitrasterBaseName, "SIZE_OF_TILE", "TIFF", "NEAREST","#","64 64","","METERS")
    elif backgroundStatus == "BLACK":
        print("\nRemoving NoData background value...")
        black_background = 0
        copyRasterB = arcpy.management.CopyRaster(geotiff, outputRaster, 0, black_background)
        print("\nNoData mask removed! Proceeding to the SplitRaster function...")
        print("\nSplitting Raster")
        splitRasterB = arcpy.management.SplitRaster(copyRasterB, splitrasterDir, splitrasterBaseName, "SIZE_OF_TILE", "TIFF", "NEAREST","#","64 64","","METERS")

elif removeNoData == "NO":
    print("\nProceeding to the SplitRaster function...")
    splitRasterO = arcpy.management.SplitRaster(geotiff, splitrasterDir, splitrasterBaseName, "SIZE_OF_TILE", "TIFF", "NEAREST","#","64 64","","METERS")

#---------Split Raster Function-------#


print("Success")


