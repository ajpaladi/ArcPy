#KML to Layer and Find Area
#This script will run KML to Layer and return the area of that KML
#Script by Andrew Paladino

import arcpy
arcpy.env.overwriteOutput = True

print("converting KML...")

#path to KML
kml = r"W:\Operations\Holstein\Mission_Planning_Good\IR_6.kml"

#path to save directory
savePath = r"W:\Operations\Holstein\Mission_Planning_Good\kml2layer"

output = savePath + "/"
kmltolayer = arcpy.KMLToLayer_conversion(kml, output, 'test')

print("Conversion successful...")
print("layer saved to:" + "\n" + savePath + "/test.gdb")
print("Calculating area of Polygon(s)...")

arcpy.env.workspace = savePath + "/test.gdb"

units = input("\nSpecify desired units...choose between 'SQUAREFEET', 'SQUAREMILES' or 'ACRES':\n")
if units == 'SQUAREFEET':
    with arcpy.da.SearchCursor("Polygons", ['NAME','SHAPE@']) as cursor:
        for row in cursor:
            print("\nthe area of {0} is {1} SQUAREFEET".format(row[0], row[1].getArea('GEODESIC', 'SQUAREFEET')))
            #one can substitide SQUAREFEET or SQUAREMILES or ACRES for units^ 
elif units == 'ACRES':
    with arcpy.da.SearchCursor("Polygons", ['NAME','SHAPE@']) as cursor:
        for row in cursor:
            print("\nthe area of {0} is {1} ACRES".format(row[0], row[1].getArea('GEODESIC', 'ACRES')))
            #one can substitide SQUAREFEET or SQUAREMILES or ACRES for units^
elif units == 'SQUAREMILES':
    with arcpy.da.SearchCursor("Polygons", ['NAME','SHAPE@']) as cursor:
        for row in cursor:
            print("\nthe area of {0} is {1} SQUAREMILES".format(row[0], row[1].getArea('GEODESIC', 'SQUAREMILES')))
            #one can substitide SQUAREFEET or SQUAREMILES or ACRES for units^ 

print("\nScript Completed!")
