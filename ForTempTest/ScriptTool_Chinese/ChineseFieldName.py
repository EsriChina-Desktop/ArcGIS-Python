# -*- coding: cp936 -*-

import arcpy
input = arcpy.GetParameterAsText(0)
fieldName = "�����ֶ�"
arcpy.AddField_management(input, fieldName, "TEXT")
