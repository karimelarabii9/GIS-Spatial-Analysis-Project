import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True
points_lakes = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_lakes.shp"
#search cursos
#loop
#
arcpy.MakeFeatureLayer_management(points_lakes,"points_lakes_layer")
lakes_cursor=arcpy.SearchCursor("points_lakes_layer",['name','scalerank','wikidataid'])
for x in lakes_cursor:
    print (x.getValue('name'))
    print (x.getValue('scalerank'))
    print (x.getValue('wikidataid'))
    print ("--------------------------")