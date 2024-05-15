import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True

points_time_zones_parameter=arcpy.GetParameterAsText(0)
compared_value=arcpy.GetParameterAsText(1)

time_zone_cursor=arcpy.SearchCursor(points_time_zones_parameter,['places','zone'])
llist=[]
for x in time_zone_cursor:
    if (((x.getValue('zone') == float(compared_value)) or (x.getValue('zone') == float(compared_value)*-1))and(x.getValue('places')not in llist)):
        arcpy.AddMessage("Success")
        llist.append(x.getValue('places'))
arcpy.AddMessage(llist)
arcpy.AddMessage(len(llist))