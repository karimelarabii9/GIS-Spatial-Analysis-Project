import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
arcpy.env.overwriteOutput = True
feature_list=arcpy.ListFeatureClasses()
print(feature_list)