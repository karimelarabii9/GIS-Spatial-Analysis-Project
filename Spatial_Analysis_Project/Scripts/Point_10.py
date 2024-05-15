import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True
outpath = r"C:\Users\kamma\Desktop\GISP\Output"
points_time_zones = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_time_zones.shp"
time_zone_cursor = arcpy.SearchCursor(points_time_zones, ['places', 'name'])
for x in time_zone_cursor:
    if x.getValue('zone') <0:
        print(x.getValue('places'))
        print(x.getValue('name'))