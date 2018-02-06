#!/usr/bin/env python
# encoding: utf-8

"""
@author: z00390414
@software: PyCharm
@file: vm01.py
@time: 2018/1/24 11:50
"""
import xlrd
import xlwt

ipVmStop = []
ipDel = []

def func():
    workbook = xlrd.open_workbook('vmInfo.xlsx')
    sheet2 = workbook.sheet_by_index(4)  # sheet索引从0开始
    rowNum = sheet2.nrows
    colNum = 1
    llst = []
    for i in range(rowNum):
        lst = []
        for j in range(colNum):
            lst.append(sheet2.cell_value(i, j))
        llst.append(lst)

    for i in range(rowNum):
        for j in range(colNum):
            ipVmStop.append(llst[i][j])
            # print llst[i][j], '\t\t',
        # print
def releaseInfo(workbook,sheetIndex):
    sheet2 = workbook.sheet_by_index(sheetIndex)  # sheet索引从0开始
    rowNum = sheet2.nrows
    colNum = sheet2.ncols
    llst = []
    for i in range(rowNum):
        lst = []
        for j in range(colNum):
            lst.append(sheet2.cell_value(i, j))
        llst.append(lst)

    for i in range(rowNum):
        for j in range(colNum):
            # print llst[i][j], '\t\t',
            ipDel.append(llst[i][j])
        # print

class Main(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    # func()
    workbook = xlrd.open_workbook('vmReleaseInfo.xlsx')
    sheets = workbook.sheets()
    # print  len(sheets)
    for sheetIndex in range(len(sheets)):
        releaseInfo(workbook,sheetIndex)
    func()
    # print ipDel
    # print ipVmStop
    # print len(ipVmStop)
    # print len(ipDel)
    for ip_del_info in ipDel:
        # print ip_del_info
        if isinstance(ip_del_info,basestring):
            # print ip_del_info
            for ip_stop_info in ipVmStop:
                if ip_del_info in ip_stop_info:
                    if ip_del_info.strip() == "":
                        pass
                    else:
                        print '%s \t\t can delete' % ip_del_info
                    # print ip_del_info
                    # pass
