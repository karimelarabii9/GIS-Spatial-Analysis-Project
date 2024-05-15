import arcpy
arcpy.env.workspace = r"C:\Users\kamma\Desktop\GISP\Data"
SOV0NAME_UK=r"C:\Users\kamma\Desktop\GISP\Output\SOV0NAME_United_Kingdom.shp"

arcpy.MakeFeatureLayer_management(SOV0NAME_UK,"SOV0NAME_UK_layer")
with arcpy.da.UpdateCursor("SOV0NAME_UK_layer",['SOV0NAME']) as SOV0NAME_UK_cursor:
    for x in SOV0NAME_UK_cursor:
        x[0]="Britain"
        SOV0NAME_UK_cursor.updateRow(x)