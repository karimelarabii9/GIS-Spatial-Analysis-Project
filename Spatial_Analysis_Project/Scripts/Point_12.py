import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True
outpath = r"C:\Users\kamma\Desktop\GISP\Output"
points_geographic_lines = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_geographic_lines.shp"
points_populated_places = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_admin_0_countries.shp"

arcpy.MakeFeatureLayer_management(points_geographic_lines, "points_geographic_lines_layer", """ "name_long"='Equator' """)

arcpy.MakeFeatureLayer_management(countries, "countries_layer")
arcpy.SelectLayerByLocation_management("countries_layer", "INTERSECT", "points_geographic_lines_layer")
arcpy.FeatureClassToFeatureClass_conversion("countries_layer",outpath,"Intersect_countries")

arcpy.MakeFeatureLayer_management(points_populated_places, "points_populated_places_layer")
arcpy.SelectLayerByLocation_management("points_populated_places_layer", "WITHIN", "countries_layer")
arcpy.FeatureClassToFeatureClass_conversion("points_populated_places_layer",outpath,"intersecct_cities")
