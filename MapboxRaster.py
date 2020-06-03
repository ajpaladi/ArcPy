#Title: ArcGIS Desktop integration into Mapbox
#Script by Andrew Paladino
#First python script using Arcpy GET BLAZED

import arcpy

def print_message(msg):
    print(msg)
    arcpy.AddMessage(msg)

arcpy.env.overwriteOutput = True
#Specify the path to your workspace or geodatabase
arcpy.env.workspace = r"W:\Operations\Holstein\ArcGIS\AGO"

#specify the path to raster that needs to be borderless
InRaster = r"W:\Operations\Holstein\ArcGIS\Orthomosaics\Clipped_EvenReadier\34_IR_WebM_Clip1_Georect.tif"

#specify location to be saved and \<name.tif> at the end of the path
OutRaster = r"W:\Operations\Holstein\ArcGIS\Test\MapboxRaster2.tif"

mapboxraster = arcpy.CopyRaster_management(in_raster = InRaster, out_rasterdataset = OutRaster,
                                           config_keyword = None, background_value = 0, nodata_value = 0,
                                           onebit_to_eightbit = None, colormap_to_RGB = None, pixel_type = "8_BIT_UNSIGNED", scale_pixel_value = None,
                                           RGB_to_Colormap = None, format = None, transform = None, process_as_multidimensional = None,
                                           build_multidimensional_transpose = None)



print_message("{0} has been saved as a Mapbox tileset in {1}".format(InRaster, OutRaster))
print_message("Script Completed!")




