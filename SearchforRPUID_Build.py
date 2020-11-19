#search for Building Numbers, RPUID codes, and FACILITYID's in the SDE, and return database path to that feature
#Script by Andrew Paladino 11/5/2020

import arcpy
import os
arcpy.env.workspace = r"Database Connections/SDE.sde"
arcpy.env.OverwriteOutput = True

ListFeatures = input("\nDo you want to list all feature classes in the specified dataset? Y or N: \n")
                     
if ListFeatures == "Y":
    InputDataset = input("\nWhich Feature Dataset did you want to Look in? \n FeatureDataset:")
    if InputDataset == 'GIO.Pavements':
        print("\nListing feature classes in speciifed dataset...")
        datasets = arcpy.ListDatasets(InputDataset)
        datasets = [''] + datasets if datasets is not None else []

        for ds in datasets:
            for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
                path = os.path.join(arcpy.env.workspace, ds, fc)
                print(path)
    else:
        print("\nListing feature classes in speciifed dataset...")
        datasets = arcpy.ListDatasets(InputDataset)
        datasets = [''] + datasets if datasets is not None else []
        
        for ds in datasets:
            for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
                path = os.path.join(arcpy.env.workspace, ds, fc)
                print(path)

elif ListFeatures == "N":
    print("\nMoving On...")

InputFC = input("\nWhat Feature class would you like to search ? \n FC:   ")

searchingfor  = input("\nWhat are you searching for? \n RPUID, BUILDINGNUMBER, or FACILITYID:  ")
value1 = '"REALPROPERTYUNIQUEIDENTIFIER" = \'1055\''
value2 = '"BUILDINGNUMBER" = \'1163\'' 
value3 = '"FACILITYID" = \'1163\''
print(value1)

if searchingfor == "RPUID":
    inputRPUID = value1[:-5] + input("\nRPUID Value:  ") + "'"
    print(inputRPUID)
    if inputRPUID == value1:
        #Search for RPUID in feature class
        print("\nSearching Geodatabase for RPUID...")
        fc = InputFC
        field = 'REALPROPERTYUNIQUEIDENTIFIER'
        lat = 'LATITUDE'
        lon = 'LONGITUDE'
        featureName = 'SDSFEATURENAME'
        featureDesc = 'SDSFEATUREDESCRIPTION'
        value = inputRPUID
        cursor = arcpy.SearchCursor(fc, value)
        row = cursor.next()
        while row:
            print("\n RPUID:  " + str(row.getValue(field)) + "  exists in {0}".format(fc)) + "\n@ latitude:  " + str(row.getValue(lat)) + "\n@ longitude:  " + str(row.getValue(lon)) + "\n@ Feature Name:  " + str(row.getValue(featureName)) + "\n@ Feature Desc:  " + str(row.getValue(featureDesc))
            row = cursor.next()
    else:
        #Search for RPUID in feature class
        print("\nSearching Geodatabase for RPUID...")
        fc = InputFC
        field = 'REALPROPERTYUNIQUEIDENTIFIER'
        lat = 'LATITUDE'
        lon = 'LONGITUDE'
        featureName = 'SDSFEATURENAME'
        featureDesc = 'SDSFEATUREDESCRIPTION'
        value = inputRPUID
        cursor = arcpy.SearchCursor(fc, value)
        row = cursor.next()
        while row:
            print("\n RPUID:  " + str(row.getValue(field)) + "  exists in {0}".format(fc)) + "\n@ latitude:  " + str(row.getValue(lat)) + "\n@ longitude:  " + str(row.getValue(lon)) + "\n@ Feature Name:  " + str(row.getValue(featureName)) + "\n@ Feature Desc:  " + str(row.getValue(featureDesc))
            row = cursor.next()

elif searchingfor == "BUILDINGNUMBER":
    inputBuildingNumber = value2[:-5] + input("\nBuilding Number Value:  ") + "'"
    print(inputBuildingNumber)
    if inputBuildingNumber == value2:
        #Search for Buidling Number in Feature Class
        print("\nSearching Geodatabase for BuildingNumber...")
        fc = InputFC
        field = "BUILDINGNUMBER"
        lat = 'LATITUDE'
        lon = 'LONGITUDE'
        status = 'BUILDINGSTATUS'
        RPUID = 'REALPROPERTYUNIQUEIDENTIFIER'
        value = inputBuildingNumber
        cursor = arcpy.SearchCursor(fc, value)
        row = cursor.next()
        while row:
            print("\n BuildingNumber:  " + str(row.getValue(field)) + "  exists in {0}".format(fc)) + "\n@ latitude:  " + str(row.getValue(lat)) + "\n@ longitude:  " + str(row.getValue(lon)) + "\n@ Status:  " + str(row.getValue(status)) + "\n@ RPUID:  " + str(row.getValue(RPUID))
            row = cursor.next()
    else:
        #Search for Buidling Number in Feature Class
        print("\nSearching Geodatabase for BuildingNumber...")
        fc = InputFC
        field = "BUILDINGNUMBER"
        lat = 'LATITUDE'
        lon = 'LONGITUDE'
        status = 'BUILDINGSTATUS'
        RPUID = 'REALPROPERTYUNIQUEIDENTIFIER'
        value = inputBuildingNumber
        cursor = arcpy.SearchCursor(fc, value)
        row = cursor.next()
        while row:
            print("\n BuildingNumber:  " + str(row.getValue(field)) + "  exists in {0}".format(fc)) + "\n@ latitude:  " + str(row.getValue(lat)) + "\n@ longitude:  " + str(row.getValue(lon)) + "\n@ Status:  " + str(row.getValue(status)) + "\n@ RPUID:  " + str(row.getValue(RPUID))
            row = cursor.next()
        
elif searchingfor == "FACILITYID":
    inputFacilityID = value3[:-5] + input("\nFacilityID Value:  ") + "'"
    print(inputFacilityID)
    if inputFacilityID == value3:
        #Search for Fac'"FACILITYID" = \'1163\''ilityID in Feature Class
        print("\nSearching Geodatabase for facilityID/BuildingNumber...")
        fc = InputFC
        field = "FACILITYID"
        lat = 'LATITUDE'
        lon = 'LONGITUDE'
        value = inputFacilityID
        cursor = arcpy.SearchCursor(fc, value)
        row = cursor.next()
        while row:
            print("\n BuildingNumber:  " + str(row.getValue(field)) + "  exists in {0}".format(fc)) + "\n@ latitude:  " + str(row.getValue(lat)) + "\n@ longitude:  " + str(row.getValue(lon))
            row = cursor.next()
    else:
        #Search for FacilityID in Feature Class
        print("\nSearching Geodatabase for facilityID/BuildingNumber...")
        fc = InputFC
        field = "FACILITYID"
        lat = 'LATITUDE'
        lon = 'LONGITUDE'
        value = inputFacilityID
        cursor = arcpy.SearchCursor(fc, value)
        row = cursor.next()
        while row:
            print("\n BuildingNumber:  " + str(row.getValue(field)) + "  exists in {0}".format(fc)) + "\n@ latitude:  " + str(row.getValue(lat)) + "\n@ longitude:  " + str(row.getValue(lon))
            row = cursor.next()
        

print("\nScript Completed!")
