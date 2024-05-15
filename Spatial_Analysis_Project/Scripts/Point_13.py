import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True
outpath = r"C:\Users\kamma\Desktop\GISP\Output"
countries = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_admin_0_countries.shp"
points_time_zones = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_time_zones.shp"

time_zone_cursor=arcpy.SearchCursor(points_time_zones,['places','zone'])
llist=[]
for x in time_zone_cursor:
    if (((x.getValue('zone') == 2) or (x.getValue('zone') == -2))and(x.getValue('places')not in llist)):
        llist.append(x.getValue('places'))
print (llist)
print (len(llist))