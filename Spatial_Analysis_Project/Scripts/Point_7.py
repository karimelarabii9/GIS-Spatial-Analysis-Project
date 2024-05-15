import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True
points_lakes = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_lakes.shp"

arcpy.MakeFeatureLayer_management(points_lakes,"points_lakes_layer")

with arcpy.da.UpdateCursor("points_lakes_layer",['wikidataid','note']) as points_lakes_cursor:
    for x in points_lakes_cursor:
        if(x[0]==' '):
            x[0] = "undifined"
            x[1]='this row is updated'
            points_lakes_cursor.updateRow(x)