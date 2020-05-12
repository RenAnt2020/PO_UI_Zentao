#!/usr/bin/env python
# encoding:utf-8
# @author:Rensh
#@file:excel_utils.py
#@time:2020/5/12  14:53
#@desc:
import os
import xlrd
from common.config import Config
from common.log_utils import logger

class ExcelUtils(object):
    """
        判断是否是excel文件再进行处理 xls  xlsx  并且 文件存在
    """

    def __init__(self,excel_path,sheet_name=None):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.sheet_data = self.__get_sheet_date

    @property
    def __get_sheet_date(self):
        workbook = xlrd.open_workbook(self.excel_path)
        if self.sheet_name:
            sheet = workbook.sheet_by_name(self.sheet_name)
            logger.info("读取名为：%s sheet的数据"%self.sheet_name)
        else:
            sheet = workbook.sheet_by_index(0)
            logger.info("读取第一个sheet的数据")
        return sheet
    @property
    def get_row_count(self):
        row_count = self.sheet_data.nrows
        logger.info("Excel有：%s行"%row_count)
        return row_count
    @property
    def get_col_count(self):
        col_count = self.sheet_data.ncols
        logger.info("Excel有：%s列" %col_count)
        return col_count
    @property
    def get_sheet_data_by_list(self):#把excel的数据通过列表返回 [ [] , [] , [] ]
        all_excel_data=[]
        for rownum in range(self.get_row_count):
            row_excel_data = []
            for colnum in range(self.get_col_count):
                cell_value = self.sheet_data.cell_value(rownum,colnum)
                logger.info("读取第：%s行，%s列" % (rownum,colnum))
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        logger.info("Excel数据列表：%s"%all_excel_data)
        return all_excel_data

if __name__ == "__main__":
    current_path = os.path.abspath(os.path.dirname(__file__))
    test_data_path = os.path.join(current_path,'..',Config().element_info_path,'element_infos_r.xlsx')
    sheet_infos = ExcelUtils(test_data_path).get_sheet_data_by_list
    print(sheet_infos)