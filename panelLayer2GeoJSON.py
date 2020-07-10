#Summary: project and convert an All Panel damage layer to GeoJSON
#Goal: Easily share Solar Panel damage layers on Web Maps or Rest API's
#Script by Andrew Paladino Copyright July 2020

import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"W:\Operations\Inovateus\HenryVille"

SpatialReference = arcpy.SpatialReference(4326)

print("\nProjecting damage layer(s) in WGS84...")

#Input path to shapefile
inputLayer = r"W:\Operations\Inovateus\HenryVille\ArcGIS\Panels\Step9_PanelFinal.shp"
#Output path to save the Shapfile
OutputPath = r"W:\Operations\Inovateus\HenryVille\GeoJSON"

OutputLayer = OutputPath + "/" + "WGS84panels.shp"
projectedpanels = arcpy.management.Project(inputLayer, OutputLayer, SpatialReference) 

print("\nDamage Layer converted and saved to {0}".format(OutputPath))
print("\nConverting panels in GeoJSON format...")

OutputJSON = OutputPath + "/" + "panels"
GeoJSONLayer = arcpy.FeaturesToJSON_conversion(OutputLayer, OutputJSON, None, None, None, "GEOJSON")

print("\nPanels coverted to GeoJSON and saved to {0}".format(OutputPath))
print("\nScript Completed!")



    
