#!/usr/bin/env python
# encoding: utf-8
'''
@author: Wanghan
@contact: panda@cug.edu.cn
@software: Pycharm
@file: Statics.py
@time: 2018/7/20 15:19
@desc:
'''
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "LANDUSE_2008"
import arcpy
import sys
import datetime
start_time = datetime.datetime.now()
arcpy.env.workspace = "F:\Data\SZ_LandUse_1.gdb"
'''LandUse_List=["LANDUSE_1996","LANDUSE_2000","LANDUSE_2001","LANDUSE_2002","LANDUSE_2003","LANDUSE_2004","LANDUSE_2005","LANDUSE_2006",
              "LANDUSE_2007","LANDUSE_2008","LANDUSE_2010","LANDUSE_2011","LANDUSE_2012","LANDUSE_2013","LANDUSE_2014","LANDUSE_2015","LANDUSE_2016"]'''
LandUse_List=["LANDUSE_2005"]
'''LandUse_List=["LANDUSE_1996","LANDUSE_2000","LANDUSE_2001","LANDUSE_2002","LANDUSE_2003","LANDUSE_2004","LANDUSE_2006",
              "LANDUSE_2007","LANDUSE_2008","LANDUSE_2010","LANDUSE_2011","LANDUSE_2012","LANDUSE_2013","LANDUSE_2014","LANDUSE_2015","LANDUSE_2016"]'''
print("开始处理时间：" + str(datetime.datetime.now()) + ";")
for LandUse in  LandUse_List:
    arcpy.Frequency_analysis(in_table=LandUse, out_table="C:/Users/lenovo/Documents/ArcGIS/Default.gdb/"+LandUse+"_Frequency",
                         frequency_fields="YJL_MC_07;YJL_BM_07;EJL_MC_07;EJL_BM_07;PZWH_;BGRQ_;SDLMC;JDDM;JDMC",summary_fields="Shape_Area")
    print("Message:"+str(datetime.datetime.now())+"    ["+LandUse+"]统计计算完成")

end_time = datetime.datetime.now()
print("结束处理时间：" + str(end_time) + ";")
print("累计用时：" + str(end_time-start_time) + ";")