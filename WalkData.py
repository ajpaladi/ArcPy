import arcpy

#workspace = r"C:\arcgis\ArcTutor\BuildingaGeodatabase"
workspace = r"C:\arcgis\ArcTutor"


dataList = []
for dirpath, dirnames, filenames in arcpy.da.Walk(workspace,
                                                  datatype="RasterDataset",
                                                  type=["JPG", "PNG", "TIF"]):
    for filename in filenames:
        dataList.append(r"{0}\{1}".format(dirpath, filename))
print(dataList)
print("\nFound {0} data elements in {1}".format(len(dataList), workspace))

print("\nScript Completed!")
