import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True

points_boundary_lines_land_parameter=arcpy.GetParameterAsText(0)
selected_country=arcpy.GetParameterAsText(1)
outpath=arcpy.GetParameterAsText(2)

with arcpy.da.SearchCursor(points_boundary_lines_land_parameter,['ADM0_LEFT','ADM0_RIGHT'],""" "ADM0_LEFT" IN ('Germany', 'Egypt', 'Brazil') OR  "ADM0_RIGHT" IN ('Germany', 'Egypt', 'Brazil')""") as cursor_border:
    for i in cursor_border:
            if ((selected_country == i[0]) | (selected_country == i[1]))&(selected_country in ('Germany', 'Egypt', 'Brazil')):
                arcpy.MakeFeatureLayer_management(points_boundary_lines_land_parameter,'borders_layer',""""ADM0_LEFT" = '{0}' AND "ADM0_RIGHT" = '{1}' """.format(i[0],i[1]))
                arcpy.FeatureClassToFeatureClass_conversion('borders_layer',outpath,'borders_{0}_{1}'.format(i[0],i[1]))
                arcpy.AddMessage("Success")