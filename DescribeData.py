import arcpy

#dataElement = r"C:\arcgis\ArcTutor\BuildingaGeodatabase\Montgomery.gdb\LandBase"
#dataElement = r"W:\Operations\Inovateus\HenryVille\RawData\Henryville_Solar_EO\Henryville_Solar_EO"
#dataElement = r"C:\arcgis\ArcTutor\Editing\Zion.gdb"
dataElement = r"C:\arcgis\ArcTutor\Geocoding\Atlanta.gdb"
#dataElement = r"C:\arcgis\ArcTutor\Geocoding\Atlanta.gdb\streets"

##descDictionary = arcpy.da.Describe(dataElement)
##for i, key in enumerate(descDictionary):
##    print("{0}. {1}: {2}".format(i, key, descDictionary[key]))

#assign a variable to the arcpy.Describe 
desc = arcpy.Describe(dataElement)
print("Decribing {0}...".format(dataElement))
print("Name:           " + desc.name)
print("DataType:       " + desc.dataType)
print("CatalogPath:    " + desc.catalogPath)

#examine the children of the above specified file using the code below
print("Children:")
for child in desc.children:
    if hasattr(child, "shapeType"):
        print("  {0} is a {1} of shapeType {2}".format(child.name, child.dataType, child.shapeType))
        print("  with Extent of {0}".format(child.extent))
    else:
        print("  {0} is a {1}".format(child.name, child.dataType))
    print("  and Fields:")
    for field in child.fields:
        print("  {0} of type {1}".format(field.name, field.type))

print("\nScript Completed!")
