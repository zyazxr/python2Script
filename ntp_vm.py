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

snNum = []
snNumAll = []
excelFile = 'ntp2.xlsx'


def func():
    workbook = xlrd.open_workbook(excelFile)
    sheet2 = workbook.sheet_by_index(0)  # sheet索引从0开始
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
            snNum.append(llst[i][j])
            # print llst[i][j], '\t\t',
            # print


def releaseInfo(workbook, sheetIndex):
    sheet2 = workbook.sheet_by_index(sheetIndex)  # sheet索引从0开始
    rowNum = sheet2.nrows
    colNum = sheet2.ncols
    llst = []
    for i in range(rowNum):
        lst = []
        for j in range(colNum):
            lst.append(sheet2.cell_value(i, j))
        llst.append(lst)
        # for k in  snNum:
        #     if k == llst[i][j]:
        #         print llst[i][:]
        #         print

        # print snNum[0]
    # snNumAll = llst
    # for i in range(rowNum):
    all_info_error = []
    for k in range(rowNum):
        # print k , llst[k][:]
        # print llst[i][j], '\t\t',
        # snNumAll.append(llst[i][j])
        for m in snNum:
            if m == llst[k][10]:
                # print llst[k][:]
                all_info_error.append(llst[k][:])
                # print
                # if llst[i][j] in snNum:
                #     print llst[i][j]
    print all_info_error
    return all_info_error


def writeIn(all_info_error):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('My Worksheet')
    worksheet.write(1, 0, label='this is test')
    # workbook.save('Excel_test.xls')
    x = 0
    y = 0

    for a in all_info_error:
        x = x + 1
        y = 0
        for b in a:
            y = y + 1
            print x, y
            worksheet.write(x, y, label=b)
            print b
    workbook.save('Excel_test5.xlsx')


class Main(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    # func()
    workbook = xlrd.open_workbook(excelFile)
    sheets = workbook.sheets()
    # print  len(sheets)
    # for sheetIndex in range(len(sheets)):
    #     releaseInfo(workbook,sheetIndex)
    func()
    all_info_error = releaseInfo(workbook, 1)
    print all_info_error
    writeIn(all_info_error)
    # print snNumAll[:][7]
    # print snNumAll[11]
    # print ipVmStop
    # print len(ipVmStop)
    # print len(ipDel)
    # for snTemp in snNum:
    #     # print snTemp
    #     for snAllTemp in snNumAll:
    #         # print snAllTemp
    #         if snTemp == snAllTemp:
    #             # print sn
    #             print snAllTemp
