#!/usr/bin/env python
# encoding: utf-8
'''
@author: Wanghan
@contact: panda@cug.edu.cn
@software: Pycharm
@file: Functions.py
@time: 2018/7/24 19:02
@desc:
'''
#coding=utf-8
def GetYJL(value):
    V = int(value)
    S = 0
    if V < 100:
        S= str(V)[0:1]
    elif 100<V<900:
        S= str(V)[0:2]
    else:
        if V== 901:
            S= str(0)
        elif V==902:
            S= str(8)
        elif V==903:
            S= str(11)
        elif V==904:
            S= str(11)
        elif V==905:
            S=str(0)
        elif V==906:
            S=str(0)
        elif V==907:
            S=str(0)
        else:
            S=str(0)
    return int(S)
#3DL
def GetYJL(value):
    SDL_Dict = {
        "11": "1", "12": "1", "13": "1", "21": "1", "22": "1", "23": "1",
        "31": "1", "32": "1", "33": "1", "41": "1", "42": "1", "104": "1",
        "114": "1", "117": "1", "122": "1", "123": "1", "51": "2", "52": "2",
        "53": "2", "54": "2", "61": "2", "62": "2", "63": "2", "71": "2",
        "72": "2", "81": "2", "82": "2", "83": "2", "84": "2", "85": "2",
        "86": "2", "87": "2", "88": "2", "91": "2", "92": "2", "93": "2",
        "94": "2", "95": "2", "101": "2", "102": "2", "103": "2", "105": "2",
        "106": "2", "107": "2", "113": "2", "118": "2", "121": "2", "111": "3",
        "112": "3", "115": "3", "116": "3", "119": "3", "43": "3", "124": "3",
        "125": "3", "126": "3", "127": "3", "901":"0","902":"2","903":"1","904":"3",
        "905":"2","906":"2","907":"3"
    }
    V = str(int(value))
    S =SDL_Dict[V]
    return int(S)

#coding=utf-8
def GetTYBM(YJL_BM_07,EJL_BM_07,SDLMC):
	sys =__import__('sys')
	reload(sys)
	sys.setdefaultencoding('utf-8')
	YJL_BM = str(YJL_BM_07)
	EJL_BM= str(EJL_BM_07)
	if EJL_BM!='':
		return str(EJL_BM)[0:3]
	else:
		if YJL_BM=='' and EJL_BM=='' and SDLMC=='':
			return '901'
		if YJL_BM=='08' and EJL_BM=='' and SDLMC=='建设用地':
			return '902'
		if YJL_BM=='11' and EJL_BM=='' and SDLMC=='农用地':
			return '903'
		if YJL_BM=='11' and EJL_BM=='' and SDLMC=='未利用地':
			return '904'
		if YJL_BM=='06' and EJL_BM=='' and SDLMC=='建设用地':
			return '905'
		if YJL_BM=='' and EJL_BM=='' and SDLMC=='建设用地':
			return '906'
		if YJL_BM=='' and EJL_BM=='' and SDLMC=='未利用地':
			return '907'
		else:
			return 'ERROR'
