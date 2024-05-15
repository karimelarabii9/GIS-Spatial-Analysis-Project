import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True
countries = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_admin_0_countries.shp"
outpath = r"C:\Users\kamma\Desktop\GISP\Output"
points_populated_places = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_populated_places.shp"

arcpy.MakeFeatureLayer_management(points_populated_places,"points_populated_places_layer",""" "SOV0NAME"='United Kingdom' """)
arcpy.FeatureClassToFeatureClass_conversion("points_populated_places_layer",outpath,"SOV0NAME_United_Kingdom")

populated_places_cursor=arcpy.SearchCursor("points_populated_places_layer",['NAME','FID'])
print ("Cities_sovoname_in_uk")
print ("--------------------------")
for x in populated_places_cursor:
    print (x.getValue('NAME'))
print ("--------------------------")
