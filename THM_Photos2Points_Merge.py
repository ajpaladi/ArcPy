#Script by Andrew Paladino, 2020, Measure UAS
#Geotagged Photos to Points Script with mulitple paths
#The script will create a geodatabase, run Geotagged Photos to Points on each specified thm folders, merge the output point layers into one feature class, and then delete the individual layers so your left with one feature class

import arcpy

arcpy.env.workspace = r"W:\Operations\Holstein\ArcGIS\P2P\12_18_19_20\Photos2Points.gdb"
arcpy.env.overwriteOutput = True

print("Creating Geodatabase...")

#specify geodatabase 
arcpy.CreateFileGDB_management(r"W:\Operations\Holstein\ArcGIS\P2P\12_18_19_20", "Photos2Points")
geodatabase = r"W:\Operations\Holstein\ArcGIS\P2P\12_18_19_20\Photos2Points.gdb"
print(arcpy.Exists(geodatabase))

print("Translating geotagged photos into point features...")

#Set Local Variables
rawfolder1 = r"W:\Operations\Holstein\RawData1\BLK_12_18_19_20\BLK12\DCIM\IX-02-71420_0045\thm"
#rawfolder2 = r"W:\Operations\Holstein\RawData1\BLK_12_18_19_20\BLK18\BLK18\BLK18\DCIM\IX-02-71420_0046\thm"
#rawfolder3 = r"W:\Operations\Holstein\RawData1\BLK_12_18_19_20\BLK18\BLK18\BLK18\DCIM\IX-02-71420_0047\thm"
#rawfolder4 = r"W:\Operations\Holstein\RawData1\BLK_12_18_19_20\BLK19\BLK 19\BLK 19\DCIM\IX-02-71420_0042\thm"
#rawfolder5 = r"W:\Operations\Holstein\RawData1\BLK_12_18_19_20\BLK20\BLK 20.1\BLK 20\DCIM\IX-02-71420_0039\thm"

#name your output feature layers
savedir1 = geodatabase + "/thm_45"
#savedir2 = geodatabase + "/thm_46"
#savedir3 = geodatabase + "/thm_47"
#savedir4 = geodatabase + "/thm_42"
#savedir5 = geodatabase + "/thm_39"

Photos2Points1 = arcpy.GeoTaggedPhotosToPoints_management(rawfolder1, savedir1)
#Photos2Points2 = arcpy.GeoTaggedPhotosToPoints_management(rawfolder2, savedir2)
#Photos2Points3 = arcpy.GeoTaggedPhotosToPoints_management(rawfolder3, savedir3)
#Photos2Points4 = arcpy.GeoTaggedPhotosToPoints_management(rawfolder4, savedir4)
#Photos2Points5 = arcpy.GeoTaggedPhotosToPoints_management(rawfolder5, savedir5)

print("All photos converted into points & saved to {0}".format(geodatabase))

print("Merging points...")

MergeOutput = geodatabase + "/thm_ALL" 

arcpy.Merge_management([Photos2Points1, Photos2Points2, Photos2Points3, Photos2Points4, Photos2Points5], 
                       MergeOutput, "", "ADD_SOURCE_INFO")

print("Merge Completed! Output Feature Class saved to {0}".format(MergeOutput))
print("Script Completed!")

#-----------if you want to delete the specific point layers from the input, uncomment the section below--------#

print("Deleting Individual Feature Layers...")

#delete_features = ["thm_45", "thm_46", "thm_47", "thm_42", "thm_39"]
#arcpy.Delete_management(delete_features)

arcpy.management.Delete(r"'thm_45';'thm_46';'thm_47';'thm_42';'thm_39'")

print("Individual Features Deleted!")
print("Script Completed!")
