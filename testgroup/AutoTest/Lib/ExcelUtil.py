#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : 

from __future__ import division
import xlrd
from xlutils.copy import copy


class ExcelUtil(object):
    def __init__(self, excelPath, sheetName):
        # 打开文件,在读取时要添加formatting_info=True参数，默认是False，表示原样读取,在读取时要添加formatting_info只支持xls文件
        self.book = xlrd.open_workbook(excelPath, formatting_info=True)
        self.table = self.book.sheet_by_name(sheetName)

        # get titles
        self.row = self.table.row_values(0)

        # get rows number
        self.rowNum = self.table.nrows

        # get columns number
        self.colNum = self.table.ncols

        # the current column
        self.curRowNo = 1

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        self.curRowNo = 0
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

    def copy_book(self):
        return copy(self.book)

    def modify(self, book, sheetname, data):
        """
        {'测试点': '', '实际结果': '0', '测试用例': '非法值校验（空、边界外值、负值、小数、非int型、None、NULL）',
        '是否执行(T/F)': 'T', '测试模块': '', '描述': 'success', '测试数据': 'keyword:{STRING}\nip:{IP}\nlocation:{STRING}\nstartIndex:{INT_F}\nfetchNum:{INT}',
         '是否通过(T/F)': 'F', '用例编号': 'case_006', '请求方式(POST/GET)': 'GET', '接口地址': '/xs_api/video/possible',
         '预期结果': '104\\105\\106'}
         """
        sheet = book.get_sheet(sheetname)
        while self.hasNext():
            col = self.table.row_values(self.curRowNo)
            if data["用例编号"] == col[0]:
                for i in range(self.colNum):
                    for key, value in data.items():
                        if self.row[i] == key:
                            sheet.write(self.curRowNo, i, value)
            self.curRowNo += 1
        self.curRowNo = 0

    def read_merged_excel(self):
        colspan = {}
        r = []
        if self.table.merged_cells:
            for item in self.table.merged_cells:
                # 通过循环进行组合，从而得出所有的合并单元格的坐标
                for row in range(item[0], item[1]):
                    for col in range(item[2], item[3]):
                        # 合并单元格的首格是有值的，所以在这里进行了去重
                        if (row, col) != (item[0], item[2]):
                            colspan.update({(row, col): (item[0], item[2])})

        # 开始循环读取excel中的每一行的数据
        for i in range(1, self.table.nrows):
            s = {}
            for j in range(self.table.ncols):
                # 假如碰见合并的单元格坐标，取合并的首格的值即可
                if colspan.get((i, j)):
                    d = self.table.cell_value(*colspan.get((i, j)))
                else:
                    d = self.table.cell_value(i, j)
                s[self.row[j]] = d
            r.append(s)
        return r

    def get_merged_cells(self, sheetName):
        """
            获取所有的合并单元格，格式如下：
            [(4, 5, 2, 4), (5, 6, 2, 4), (1, 4, 3, 4)]
            (4, 5, 2, 4) 的含义为：行 从下标4开始，到下标5（不包含） 列 从下标2开始，到下标4（不包含），为合并单元格
            :param sheetName:
            :return:
            """
        return sheetName.merged_cells

    def get_merged_cells_value(self, sheetName, row_index, col_index):
        """
        先判断给定的单元格，是否属于合并单元格；
        如果是合并单元格，就返回合并单元格的内容
        :return:
        """
        merged = self.get_merged_cells(sheetName)
        for (rlow, rhigh, clow, chigh) in merged:
            if (row_index >= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    cell_value = sheetName.cell_value(rlow, clow)
                    # print('该单元格[%d,%d]属于合并单元格，值为[%s]' % (row_index, col_index, cell_value))
                    return cell_value
                    break
        return None

if __name__ == '__main__':
    # test: modify()
    aa = {'用例编号': 'case_001', '是否执行(T/F)': 'T', '测试模块': '疑似记录接口', '测试点': 'keyword参数值校验', '测试用例': 'keyword字段合法值校验(中文、英文、特殊字符、None、NULL)', '接口地址': '/xs_api/video/possible', '请求方式(POST/GET)': 'GET', '测试数据': 'keyword:{STRING}\nip:{IP}\nlocation:{STRING}\nstartIndex:{INT}\nfetchNum:{INT}', '预期结果': '0', '实际结果': '', '描述': 'aaa', '是否通过(T/F)': ''}
    # print([value for value in aa.values()])
    EXCEL = ExcelUtil("E:/测试用例.xls", "接口测试用例（手工+自动化）")
    qq = EXCEL.copy_book()
    EXCEL.modify(qq, "接口测试用例（手工+自动化）", aa)
    qq.save('E:/123.xls')
    # test end
