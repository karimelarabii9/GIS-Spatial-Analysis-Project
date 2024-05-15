#IMPORTS AND CONFIGURATION
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True
countries = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_admin_0_countries.shp"
points_boundary_lines_land = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_admin_0_boundary_lines_land.shp"
points_disputed_areas = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_admin_0_disputed_areas.shp"
points_geographic_lines = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_geographic_lines.shp"
points_lakes = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_lakes.shp"
points_populated_places = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_populated_places.shp"
points_time_zones = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_time_zones.shp"
outpath = r"C:\Users\kamma\Desktop\GISP\Output"
#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Select Equator geographic line
arcpy.MakeFeatureLayer_management(points_geographic_lines, "points_geographic_lines_layer", """ "name_long"='Equator' """)

# Select countries intersecting with the Equator
arcpy.MakeFeatureLayer_management(countries, "countries_layer")
arcpy.SelectLayerByLocation_management("countries_layer", "INTERSECT", "points_geographic_lines_layer")
arcpy.MakeFeatureLayer_management(points_populated_places, "points_populated_places_layer")
arcpy.SelectLayerByLocation_management("points_populated_places_layer", "WITHIN", "countries_layer")
arcpy.FeatureClassToFeatureClass_conversion("countries_layer",outpath,"intersecct_cities")
arcpy.FeatureClassToFeatureClass_conversion("points_populated_places_layer",outpath,"intersecct_cities_points")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#POINT 13
'''time_zone_cursor=arcpy.SearchCursor(points_time_zones,['places','zone'])
llist=[]
for x in time_zone_cursor:
    if (((x.getValue('zone') == 2) or (x.getValue('zone') == -2))and(x.getValue('places')not in llist)):
        llist.append(x.getValue('places'))
print (llist)
print (len(llist))'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#POINT 14
points_time_zones_parameter=arcpy.GetParameterAsText(0)
compared_value=arcpy.GetParameterAsText(1)
time_zone_cursor=arcpy.SearchCursor(points_time_zones_parameter,['places','zone'])
llist=[]
for x in time_zone_cursor:
    if (((x.getValue('zone') == float(compared_value)) or (x.getValue('zone') == float(compared_value)*-1))and(x.getValue('places')not in llist)):
        arcpy.AddMessage("Success")
        llist.append(x.getValue('places'))
print (llist)
print (len(llist))
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#POINT 15
