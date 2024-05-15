import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True
countries = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_admin_0_countries.shp"
points_lakes = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_lakes.shp"
outpath = r"C:\Users\kamma\Desktop\GISP\Output"

lakes_count=0
arcpy.MakeFeatureLayer_management(points_lakes,"points_lakes_layer")
arcpy.MakeFeatureLayer_management(countries,"countries_layer",""""CONTINENT"='Africa'""")

arcpy.SelectLayerByLocation_management("points_lakes_layer","WITHIN","countries_layer")

arcpy.FeatureClassToFeatureClass_conversion("points_lakes_layer",outpath,"Lakes_in_Africa")

lakes_cursor=arcpy.SearchCursor("points_lakes_layer",['name','FID'])
print ("Lakes_in_Africa")
print ("--------------------------")

for x in lakes_cursor:
    lakes_count+=1
    ##print(str(x.getValue('FID')) + ") " + x.getValue('name'))
    print(x.getValue('name'))
print ("--------------------------")
print("Total Number of lakes in Africa is " + str(lakes_count))
print ("--------------------------")