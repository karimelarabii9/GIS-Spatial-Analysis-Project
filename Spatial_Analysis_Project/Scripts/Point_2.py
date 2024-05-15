import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True
countries = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_admin_0_countries.shp"
points_disputed_areas = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_admin_0_disputed_areas.shp"
points_populated_places = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_populated_places.shp"
outpath = r"C:\Users\kamma\Desktop\GISP\Output"

arcpy.MakeFeatureLayer_management(points_populated_places,"points_populated_places_layer")
arcpy.MakeFeatureLayer_management(points_disputed_areas,"points_disputed_areas_layer")
arcpy.MakeFeatureLayer_management(countries,"countries_layer","""  "NAME"='Morocco'  """)

arcpy.SelectLayerByLocation_management("points_populated_places_layer","WITHIN","countries_layer")
arcpy.SelectLayerByLocation_management("points_disputed_areas_layer","WITHIN","countries_layer")

arcpy.FeatureClassToFeatureClass_conversion("points_populated_places_layer",outpath,"Cities_in_Morocco")
arcpy.FeatureClassToFeatureClass_conversion("points_disputed_areas_layer",outpath,"disputed_areas_in_Morocco")

populated_places_cursor=arcpy.SearchCursor("points_populated_places_layer",['NAME'])
disputed_areas_layer_cursor=arcpy.SearchCursor("points_disputed_areas_layer",['NAME_SORT'])
print ("Cities_in_Morocco")
print ("--------------------------")
for x in populated_places_cursor:
    print (x.getValue('NAME'))
print ("--------------------------")
print ("Disputed_areas_in_Morocco")
print ("--------------------------")
for x in disputed_areas_layer_cursor:
    print (x.getValue('NAME_SORT'))
