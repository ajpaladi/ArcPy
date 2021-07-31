import arcpy
import os
import shutil
import time
import webbrowser
from datetime import datetime
arcpy.env.workspace = r"Database Connections/SDE@311.sde"
arcpy.env.OverwriteOutput = True

print("\nResourcing Layers in MXD to the JBA SDE (Only if necessary)...")

#-----------------------Uncomment the below lines of code to batch change the datasource in a particular dataframe-----------------------#

#mxd = arcpy.mapping.MapDocument(r"F:\01- Maps & Imagery\MXD_Templates\dig_permit.mxd")
#mxd.replaceWorkspaces(r"F:\08- Software\AndrewsSDE_FGDB_5_2021\JBA_GDB_4_13.gdb", 'FILEGDB_WORKSPACE',
#                      r"Database Connections/SDE@311.sde", 'SDE_WORKSPACE')
#mxd.saveACopy(r"F:\01- Maps & Imagery\MXD_Templates\digpermit_test.mxd")

#----------------------add a new layer to the map representing the desired dig permit area-----------------------------------------------#

print("\nRemoving dig permit extent and saving a new MXD...")
print("\nRemoving preexisting deliverables within workspace...")
shutil.rmtree(r"F:\01- Maps & Imagery\MXD_Templates\deliverables")
shutil.rmtree(r"F:\01- Maps & Imagery\MXD_Templates\shapefiles")

#removing old layer from dig permit and saving a copy of the MXD
arcpy.env.workspace = r"F:\01- Maps & Imagery\MXD_Templates"
mxd = arcpy.mapping.MapDocument(r"F:\01- Maps & Imagery\MXD_Templates\digpermit_test2.mxd")
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyr in arcpy.mapping.ListLayers(mxd, "", df):
        if lyr.name.lower() == "test":
            arcpy.mapping.RemoveLayer(df, lyr)
arcpy.RefreshTOC()

#adding two new directories for the new workspace and deliverable folder
timestr = time.strftime("%Y%m%d-%H%M%S")
newpath = r"F:\01- Maps & Imagery\MXD_Templates\deliverables\\"
if not os.path.exists(newpath):
    os.makedirs(newpath)
mxd.saveACopy(newpath + timestr + ".mxd")
del mxd

newpath2 = r"F:\01- Maps & Imagery\MXD_Templates\shapefiles\\"
if not os.path.exists(newpath2):
    os.makedirs(newpath2)


#-------------------------------Creating Polygon in Empty Feature Class within a blank GeoDatabase-------------------------------#

arcpy.env.workspace = r"F:\01- Maps & Imagery\MXD_Templates\shapefiles"
arcpy.env.OverwriteOutput = True

#Creating Empty Geodatabase in folder path
GDBName = "digpolytesting"
FileGDB = arcpy.CreateFileGDB_management(newpath2, GDBName)
print(arcpy.Exists(FileGDB))

sr = arcpy.SpatialReference(4326)
fc = arcpy.CreateFeatureclass_management(FileGDB, "dpExtent", "POINT", "",
                                                "DISABLED", "DISABLED", sr)

#Adding 3 different fields into the feature class
fieldOne = arcpy.AddField_management(fc, 'NAME', 'STRING')
fieldTwo = arcpy.AddField_management(fc, 'LAT', 'DOUBLE')
fieldThree = arcpy.AddField_management(fc, 'LONG', 'DOUBLE')

#opening GeoJSON.IO so user can find lat/lon coordinates
print("Opening GeoJson.io...\n ...specify your boundary")
webbrowser.open("http://geojson.io/#map=15/38.8047/-76.8726")

#adding user input to all the copying/pasting list of each coordinate value
print("\nEnter 1 coordinate value [X,Y] in decimal degrees...")
print("\nCoordinate 1:  ")
coordOne = input()
print("\nCoordinate 2:  ")
coordTwo = input()

#creating a list of a list of the coordinate using list indexing
row_values = [('ANDREWS', (coordOne[0], coordOne[1])),
              ('ANDREWS', (coordTwo[0], coordTwo[1]))]

cursor = arcpy.da.InsertCursor(fc,['NAME', 'SHAPE@XY'])

for row in row_values:
    cursor.insertRow(row)
del cursor

#----------------------------------------------------------------------------------------#

print("\nAdding New Exent Layer to MXD based on input coordinates...")
arcpy.env.workspace = r"F:\01- Maps & Imagery\MXD_Templates\shapefiles\digpolytesting.gdb"

#using arcpy.da.mapping to add newly created layer
mxd2 = newpath + timestr + ".mxd"
mxd3 = arcpy.mapping.MapDocument(mxd2)
df = arcpy.mapping.ListDataFrames(mxd3)[0]
extentLayer = arcpy.mapping.Layer("dpExtent")
arcpy.mapping.AddLayer(df, extentLayer, "TOP")

print("\nZooming to new & specified map extent base in input coordinates...")

#zooming to layer extent
df.extent = extentLayer.getSelectedExtent(True)

#removing layer and saving maxd
for df in arcpy.mapping.ListDataFrames(mxd3):
    for lyr in arcpy.mapping.ListLayers(mxd3, "", df):
        if lyr.name.lower() == "dpextent":
            arcpy.mapping.RemoveLayer(df, lyr)
arcpy.RefreshTOC()
mxd3.save()


print("\nExporting MXD to PDF...")

#exporting Map to PDF
pdfExport = newpath + timestr + ".pdf"
arcpy.mapping.ExportToPDF(mxd3, pdfExport)
del mxd3, extentLayer

print("\nScript Completed! Dig Permit PDF has been saved @ the following location:  \n  {0}".format(pdfExport))
