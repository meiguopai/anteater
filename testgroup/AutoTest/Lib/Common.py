# _*_ coding=utf-8 _*_

import sys
import os

rootpath = sys.path[0]
flag=os.sep
# 将当前路径加入搜索路径
testplanfilepath = rootpath + flag+'TestPlan'+ flag+'TestConfig.xlsx'
configfilepath = rootpath + flag+r'Config'+ flag+'Config.xlsx'
resultfilepath = rootpath + flag+'Result'+ flag
testcasefilepath = rootpath + flag+'TestCase'+ flag
logfilepath = rootpath + flag+'Result'+ flag+'TestResult.xlsx'
toolfolderpath = rootpath + flag+'Tool'+ flag
screenshotpath = rootpath + flag+'Screenshot'+ flag
logpath = rootpath + flag+'log'+ flag
screenpath = rootpath + flag+'Screenshot'+ flag+'screen'+ flag
differpath = rootpath + flag+'Screenshot'+ flag+'differ'+ flag
testdatapath = rootpath + flag + 'TestData' + flag
# 执行结果
ACTIONFAIL = 'FAIL'
ACTIONPASS = 'PASS'
ACTIONERROR='ERROR'
REVARSTR=r'[lgLG][Vv]_[0-9a-zA-Z_]+'
REVARATTACHSTR=r'[$]{0,1}([0-9a-zA-Z,_$]*)'
TIMEOUT = 20