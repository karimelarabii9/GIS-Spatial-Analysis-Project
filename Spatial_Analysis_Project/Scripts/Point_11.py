import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True

points_time_zones_parameter=arcpy.GetParameterAsText(0)
minimum_number=arcpy.GetParameterAsText(1)
time_zone_cursor = arcpy.SearchCursor(points_time_zones_parameter, ['places', 'name'])
for x in time_zone_cursor:
    if x.getValue('zone') <float(minimum_number):
        arcpy.AddMessage("Success")
        arcpy.AddMessage(x.getValue('name'))
        arcpy.AddMessage(x.getValue('places'))