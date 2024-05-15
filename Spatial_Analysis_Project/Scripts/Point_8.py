import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True
points_boundary_lines_land = r"C:\Users\kamma\Desktop\GISP\Data\ne_10m_admin_0_boundary_lines_land.shp"
outpath = r"C:\Users\kamma\Desktop\GISP\Output"

with arcpy.da.SearchCursor(points_boundary_lines_land,['ADM0_LEFT','ADM0_RIGHT'],""" "ADM0_LEFT" IN ('Germany', 'Egypt', 'Brazil') OR  "ADM0_RIGHT" IN ('Germany', 'Egypt', 'Brazil')""") as cursor_border:
    for i in cursor_border:
                arcpy.MakeFeatureLayer_management(points_boundary_lines_land,'borders_layer',""""ADM0_LEFT" = '{0}' AND "ADM0_RIGHT" = '{1}' """.format(i[0],i[1]))
                arcpy.FeatureClassToFeatureClass_conversion('borders_layer',outpath,'borders_{0}_{1}'.format(i[0],i[1]))