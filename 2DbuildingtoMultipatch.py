#BuildingFootprint to Multipatch
#Script by Andrew Paladino 11/23/2020

import arcpy
import os
import arcinfo
import arcpy.mapping 
arcpy.env.workspace = r"Database Connections/SDE.sde"
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension('3D')

#Step 1: Create Workspace

print("\nCreating File Geodatabase...")
GDBName = "BuildingtoMultipatch"
GDBSave = r"C:\Users\1594783367E\Desktop\Andy_GIO\Scripts\Building2Multipatch"
FileGDB = arcpy.CreateFileGDB_management(GDBSave, GDBName)
print(arcpy.Exists(FileGDB))
print("\nGeodatabase created in: \n {0}".format(GDBSave))

#Step Two: Copy Features in SDE to new FC

print("\nCopying features class to: \n {0}...".format(FileGDB))
FCInput = "GIO.Building_A"
FCName = "Building_A_Copy"
FCSave = str(FileGDB) + "/" + str(FCName)
buildingFC = arcpy.CopyFeatures_management(FCInput, FCSave)

#Step Three: Generate Random Points for the DSM and DEM

print("\nGenerating Random Points on: \n {0} for the DSM".format(buildingFC))
RandomPointsDSM = "PointsDSM"
DistanceApart1 = "1 FEET"
DSMPoints = arcpy.CreateRandomPoints_management(FileGDB, RandomPointsDSM, buildingFC, "", 200, DistanceApart1, "MULTIPOINT")
print("\nRandom points generated for DSM...")

print("\nGenerating Random Points on: \n {0} for the DEM".format(buildingFC))
RandomPointsDEM = "PointsDEM"
DistanceApart2 = "1 FEET"
DEMPoints = arcpy.CreateRandomPoints_management(FileGDB, RandomPointsDEM, buildingFC, "", 200, DistanceApart2, "MULTIPOINT")
print("\nRandom points generated for DEM...")

#Step 4: Adding Surface Information to both Point Feature Classes

print("\nAdding Surface information to DSM points...")
PointsDSM = DSMPoints
elevationSurfaceDSM = r"C:\Users\1594783367E\Desktop\Andy_GIO\Projects\Multipatch_Buildings\Mosaic2NewRaster\Andrews_DSM_ALLMERGE.tif"
OutputProperty1 = ['Z_MIN', 'Z_MAX', 'Z_MEAN']
surfaceDSM = arcpy.AddSurfaceInformation_3d(PointsDSM, elevationSurfaceDSM, OutputProperty1)

print("\nAdding Surface information to DEM Points...")
PointsDEM = DEMPoints
elevationSurfaceDEM = r"C:\Users\1594783367E\Desktop\Andy_GIO\Projects\Multipatch_Buildings\Mosaic2NewRaster\Andrews_DEM_ALLMERGE.tif"
OutputProperty2 = ['Z_MIN', 'Z_MAX', 'Z_MEAN']
surfaceDEM = arcpy.AddSurfaceInformation_3d(PointsDEM, elevationSurfaceDEM, OutputProperty2)

arcpy.CheckInExtension('3D')

#Step 5: Do a Spatial Join on both DEM Points and DSM Points

print("\nJoining DSM Points with Building Features...")
TargetFC = buildingFC
OutputName = "BuildingsDSM"
OutputFC1 = str(FileGDB) + "/" + str(OutputName)
BuildingDSM = arcpy.SpatialJoin_analysis(buildingFC, surfaceDSM, OutputFC1, "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "COMPLETELY_CONTAINS")

print("\nJoining DEM Points with Building Features...")
TargetFC = BuildingDSM
OutputName = "BuildingsDSMDEM"
OutputFC2 = str(FileGDB) + "/" + str(OutputName)
BuildingDEM = arcpy.SpatialJoin_analysis(BuildingDSM, surfaceDEM, OutputFC2, "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "COMPLETELY_CONTAINS")

#Step 6: Add a new Height Field to the Feature Class (Z Max - Z Min 1)

print("\nAdding Height Field and Calculating Z Values...")
newField = arcpy.AddField_management(BuildingDEM, "HEIGHT", "FLOAT")
Expression = '[Z_Max] - [Z_Min_1]'
arcpy.CalculateField_management(BuildingDEM, "HEIGHT", Expression)

print("\n{0} has been created and saved to:\n{1}".format(BuildingDEM, FileGDB))

print("Script Completed !")


###Step 7: Open blank SXD document from folder and save as new into your project folder 
##sxd = arcpy.mapping.MapDocument(r"C:\Users\1594783367E\Desktop\Andy_GIO\Projects\Multipatch_Buildings\Feature_Testing.sxd")
##sxd.saveACopy(r"C:\Users\1594783367E\Desktop\Andy_GIO\Projects\Multipatch_Buildings\Feature_Testing2.sxd")
