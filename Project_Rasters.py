#projecting multiple raster datasets

import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = None

print("Raster Projecting into Web Mercator has commenced")

SpatialReference = arcpy.SpatialReference(3857)

In_Raster_One = r"W:\Operations\Holstein\P4D\12_18_19_20\19_20_RGB_FINAL\3_dsm_ortho\2_mosaic\19_20_RGB_FINAL_mosaic_group1.tif"
#In_Raster_Two = 
#In_Raster_Three = 

#specify save location and \<name.tif>
OutputRaster = r"W:\Operations\Holstein\ArcGIS\Orthomosaics\12_18_19_20\19_20\Projected\19_20_RGB_WebM.tif"
#OutputRasterOne = 
#OutputRasterTwo =

WebMRasterOne = arcpy.ProjectRaster_management(In_Raster_One, OutputRaster, SpatialReference)
print("{0} has been projected into EPSG:3857".format(WebMRasterOne))
#WebMRasterTwo = arcpy.ProjectRaster_management(In_Raster_Two, OutputRaster, SpatialReference)
#WebMRasterThree = arcpy.ProjectRaster_management(In_Raster_Three, OutputRaster, SpatialReference)

print("All Raster Projected into Spatial Reference 3857!")
