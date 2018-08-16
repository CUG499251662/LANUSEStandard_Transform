#!/usr/bin/env python
# encoding: utf-8
'''
@author: Wanghan
@contact: panda@cug.edu.cn
@software: Pycharm
@file: FieldCaculator.py
@time: 2018/7/18 17:40
@desc:
'''
import arcpy
import sys
import datetime
import xlrd

LandUse_List1 =["LANDUSE_1996","LANDUSE_2000","LANDUSE_2001","LANDUSE_2002","LANDUSE_2003",
                "LANDUSE_2004","LANDUSE_2005","LANDUSE_2006","LANDUSE_2007","LANDUSE_2008"]
LandUse_List2 =["LANDUSE_2010","LANDUSE_2011","LANDUSE_2012","LANDUSE_2013","LANDUSE_2014",
                "LANDUSE_2015","LANDUSE_2016"]
Field_Dict1 ={"EJL_BM_07":"T_2007_BM_EJ","EJL_MC_07":"T_2007_MC_EJ","YJL_BM_07":"T_2007_BM_YJ","YJL_MC_07":"T_2007_MC_YJ","SDLMC":"TC_2007_1984_MC"}
Field_Dict2 ={"EJL_BM_07":"XHDLDM","EJL_MC_07":"XHDLMC","JDDM":"QSDWDM","JDMC":"QSDWMC","PZWH_":"PZWH","BGRQ_":"BGRQ"}
YJL_Dict ={"01":"耕地","02":"园地","03":"林地","04":"草地","05":"商服用地","06":"工矿仓储用地",
             "07":"住宅用地","08":"公共管理与公共服务用地","09":"特殊用地","10":"交通运输用地","11":"水域及水利设施用地","12":"其他土地"}
SDL_Dict={
"011":"农用地","012":"农用地","013":"农用地","021":"农用地","022":"农用地","023":"农用地",
"031":"农用地","032":"农用地","033":"农用地","041":"农用地","042":"农用地","104":"农用地",
"114":"农用地","117":"农用地","122":"农用地","123":"农用地","051":"建设用地","052":"建设用地",
"053":"建设用地","054":"建设用地","061":"建设用地","062":"建设用地","063":"建设用地","071":"建设用地",
"072":"建设用地","081":"建设用地","082":"建设用地","083":"建设用地","084":"建设用地","085":"建设用地",
"086":"建设用地","087":"建设用地","088":"建设用地","091":"建设用地","092":"建设用地","093":"建设用地",
"094":"建设用地","095":"建设用地","101":"建设用地","102":"建设用地","103":"建设用地","105":"建设用地",
"106":"建设用地","107":"建设用地","113":"建设用地","118":"建设用地","121":"建设用地","111":"未利用地",
"112":"未利用地","115":"未利用地","116":"未利用地","119":"未利用地","043":"未利用地","124":"未利用地",
"125":"未利用地","126":"未利用地","127":"未利用地"
}
JZ_Field_Dict={"LANDUSE_1996":"LANDS","LANDUSE_2000":"DM2","LANDUSE_2001":"DM2",
               "LANDUSE_2002":"XDL","LANDUSE_2003":"DM","LANDUSE_2004":"DM_X","LANDUSE_2005":"地类码","LANDUSE_2006":"DM_X","LANDUSE_2007":"DLDM","LANDUSE_2008":"WDLDM",
                "LANDUSE_2010":"XHDLBM","LANDUSE_2011":"XHDLBM","LANDUSE_2012":"XHDLBM","LANDUSE_2013":"XHDLBM","LANDUSE_2014":"XHDLBM","LANDUSE_2015":"XHDLBM","LANDUSE_2016":"XHDLBM"}
SheetName_Dict={"LANDUSE_1996":"S_1984_2007_DB","LANDUSE_2000":"S_1984_2007_DB","LANDUSE_2001":"S_1984_2007_DB",
               "LANDUSE_2002":"S_2001_2007_DB","LANDUSE_2003":"S_2001_2007_DB","LANDUSE_2004":"S_2001_2007_DB","LANDUSE_2005":"S_2001_2007_DB","LANDUSE_2006":"S_2001_2007_DB","LANDUSE_2007":"S_2001_2007_DB",
                "LANDUSE_2008":"S_2001_2007_DB",
              }
xlsfile = u'F:\Data\国土系统土地分类标准对照_07为基准.xls'

try:
    start_time = datetime.datetime.now()
    print("开始处理时间："+str(start_time)+";")
    arcpy.env.workspace = "F:\Data\SZ_LandUse_1.gdb"
    #1996-2008 字段处理[EJL_MC_07	EJL_BM_07	PZWH_	BGRQ_	SDLMC	JDDM	JDMC]
    code_block_duizhao ="""def getCacuValue(sheetName, FiledNameL, FiledR,Fild_jz,S):
        xlrd = __import__('xlrd')
        xlsfile = u"F:\Data\国土系统土地分类标准对照_07为基准.xls"
        data = xlrd.open_workbook(xlsfile)
        table = data.sheet_by_name(sheetName)
        def getColumnIndex(columnName):
            columnIndex = None
            # print table
            for i in range(table.ncols):
                # print columnName
                # print table.cell_value(0, i)
                if (table.cell_value(0, i) == columnName):
                    columnIndex = i
                    break
            return columnIndex
        def getRowNumberIndex84(GJ_Field, Fv):
            current_columnIndex = getColumnIndex(GJ_Field)
            nrows = table.nrows           
            v = str(Fv)[0:2]
            #print(nrows)
            #print(v)
            #print(type(v))
            current_rownum = -1
            for i in range(nrows):
                try:
                    if v == str(int(table.cell_value(i, getColumnIndex(GJ_Field)))):
                        current_rownum = i
                        break
                except:
                    current_rownum = -1
            return current_rownum
        def getRowNumberIndex01(GJ_Field, Fv):
            current_columnIndex = getColumnIndex(GJ_Field)
            nrows = table.nrows           
            v = str(Fv)[0:3]
            current_rownum = -1
            for i in range(nrows):
                try:
                   if v == str(int(table.cell_value(i, getColumnIndex(GJ_Field)))):
                        current_rownum = i
                        break
                except:
                    current_rownum = -1
            return current_rownum
        currernt_row=-1 
        if  str(S)=="84":
            currernt_row = getRowNumberIndex84(Fild_jz,str(FiledR))
            #print("row84:" + str(currernt_row))
        else:
            currernt_row = getRowNumberIndex01(Fild_jz,str(FiledR))
            #print("row01:" + str(currernt_row))
        value = ""
        if currernt_row != -1:
            value = table.cell_value(currernt_row, getColumnIndex(str(FiledNameL)))
        return value"""
    for LandUse in  LandUse_List1:
        inFeatures = LandUse
        # Set local variables
        if LandUse =="LANDUSE_2005":
            fieldName1 = "JDDM"
            expression = "!座落代码!"
            arcpy.CalculateField_management(inFeatures, fieldName1, expression, "PYTHON")
            fieldName1 = "JDMC"
            expression = "!座落名称!"
            arcpy.CalculateField_management(inFeatures, fieldName1, expression, "PYTHON")
            timenow = datetime.datetime.now()
            print("Messgae:"+str(timenow)+"   处理完成" + str(LandUse) + str(fieldName1) + "字段;")
        oriField = JZ_Field_Dict[LandUse]
        for F1,F2 in Field_Dict1.items():
            print(F1,F2)
            fieldName1 = F1
            expression =""
            if LandUse=="LANDUSE_1996" or LandUse=="LANDUSE_2000" or  LandUse=="LANDUSE_2001" :
                expression = "getCacuValue('"+SheetName_Dict[LandUse]+"','"+F2+"',!"+str(oriField)+"!,'T_1984_BM_EJ','"+str(84)+"')"
            else:
                expression = "getCacuValue('" + SheetName_Dict[LandUse] + "','" + F2 + "',!" + str(
                    oriField) + "!,'T_2001_BM_SJ','" + str(84) + "')"
            print(expression)
            arcpy.CalculateField_management(inFeatures, fieldName1,expression,"PYTHON",code_block_duizhao)
            print("Messgae:" + str(datetime.datetime.now()) + "   处理完成" + str(LandUse) + str(fieldName1) + "字段;")
    '''
    #2010-2016字段处理[EJL_MC_07	EJL_BM_07	PZWH_	BGRQ_	SDLMC	JDDM	JDMC]
    for LandUse in LandUse_List2:
        inFeatures = LandUse
        for F1, F2 in Field_Dict2.items():
            fieldName1 = F1
            expression = "!" + F2 + "!"
            arcpy.CalculateField_management(inFeatures, fieldName1, expression, "PYTHON")
            print("Messgae:" + str(datetime.datetime.now()) + "   处理完成" + str(LandUse) + "[" + str(fieldName1) + "]字段;")
    '''
    '''
    # 1996-2016字段处理 YJL_MC_07	YJL_BM_07  SDLMC
    code_block_YJLBM = """def GetYJLBM(EJLBM):
        EJL = str(EJLBM)
        YJLBM =EJL[0:2]
        return YJLBM"""
    code_block_YJL = """def GetYJL(YJLBM):
        YJL_Dict ={"01":"耕地","02":"园地","03":"林地","04":"草地","05":"商服用地","06":"工矿仓储用地","07":"住宅用地","08":"公共管理与公共服务用地","09":"特殊用地","10":"交通运输用地","11":"水域及水利设施用地","12":"其他土地"} 
        V = str(YJLBM)
        YJL = YJL_Dict[YJLBM]
        return YJL"""
    code_block_SDL = """def GetSDL(EJLBM):
        SDL_Dict={"011":"农用地","012":"农用地","013":"农用地","021":"农用地","022":"农用地","023":"农用地","031":"农用地","032":"农用地","033":"农用地","041":"农用地","042":"农用地","104":"农用地","114":"农用地","117":"农用地","122":"农用地","123":"农用地","051":"建设用地","052":"建设用地",
                    "053":"建设用地","054":"建设用地","061":"建设用地","062":"建设用地","063":"建设用地","071":"建设用地",
                    "072":"建设用地","081":"建设用地","082":"建设用地","083":"建设用地","084":"建设用地","085":"建设用地",
                    "086":"建设用地","087":"建设用地","088":"建设用地","091":"建设用地","092":"建设用地","093":"建设用地",
                    "094":"建设用地","095":"建设用地","101":"建设用地","102":"建设用地","103":"建设用地","105":"建设用地",
                    "106":"建设用地","107":"建设用地","113":"建设用地","118":"建设用地","121":"建设用地","111":"未利用地",
                    "112":"未利用地","115":"未利用地","116":"未利用地","119":"未利用地","043":"未利用地","124":"未利用地",
                    "125":"未利用地","126":"未利用地","127":"未利用地"} 
        V = str(EJLBM)[0:3]
        SDL = SDL_Dict[V]
        return SDL"""
    #1996-2008 YJL_MC_07	YJL_BM_07  SDLMC
    for LandUse in LandUse_List1:
        inFeatures = LandUse
        fieldName1 = "YJL_BM_07"
        expression = "GetYJLBM(!EJL_BM_07!)"
        arcpy.CalculateField_management(inFeatures, fieldName1, expression, "PYTHON",code_block_YJLBM)
        print("Messgae:" + str(timenow) + "   处理完成"+str(LandUse)+"[YJL_BM_07]"+"字段")

        fieldName1 = "YJL_MC_07"
        expression = "GetSDL(!YJL_BM_07!)"
        arcpy.CalculateField_management(inFeatures, fieldName1, expression, "PYTHON", code_block_YJL)
        print("Messgae:" + str(timenow) + "   处理完成" +str(LandUse) + "[YJL_MC_07]" + "字段")

        fieldName1 = "SDLMC"
        expression = "GetSDL(!EJL_BM_07!)"
        arcpy.CalculateField_management(inFeatures, fieldName1, expression, "PYTHON", code_block_SDL)
        print("Messgae:" + str(timenow) + "   处理完成" +str(LandUse) + "[SDLMC]" + "字段")
    #2010-2016 YJL_MC_07	YJL_BM_07  SDLMC
    '''   '''
    for LandUse in LandUse_List2:
        inFeatures = LandUse
        fieldName1 = "YJL_BM_07"
        expression = "GetYJLBM(!EJL_BM_07!)"
        arcpy.CalculateField_management(inFeatures, fieldName1, expression, "PYTHON", code_block_YJLBM)
        print("Messgae:" + str(datetime.datetime.now()) + "   处理完成" + LandUse + "[YJL_BM_07]" + "字段")

        fieldName1 = "YJL_MC_07"
        expression = "GetYJL(!YJL_BM_07!)"
        arcpy.CalculateField_management(inFeatures, fieldName1, expression, "PYTHON", code_block_YJL)
        print("Messgae:" + str(datetime.datetime.now()) + "   处理完成" + LandUse + "[YJL_MC_07]" + "字段")

        fieldName1 = "SDLMC"
        expression = "GetSDL(!EJL_BM_07!)"
        arcpy.CalculateField_management(inFeatures, fieldName1, expression, "PYTHON", code_block_SDL)
        print("Messgae:" + str(datetime.datetime.now()) + "   处理完成" + LandUse + "[SDLMC]" + "字段")
    '''
    end_time = datetime.datetime.now()
    print("结束处理时间：" + str(end_time) + ";")
    print("累计用时："+str(end_time-start_time))
except Exception:
    e = sys.exc_info()[1]
    print(e.args[0])