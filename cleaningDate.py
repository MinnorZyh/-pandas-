'''
Author: Zyh
Date: 2022-07-17 10:49:13
LastEditors: Zyh
LastEditTime: 2022-07-17 11:37:09
Description: 数据清洗
FilePath: \Pandas\cleaningDate.py
'''

import pandas as pd


'''数据去重'''
class dropDuplicatesDatas():
    def __init__(self, path):
        self.path = path

    # TAG：保留第一出现的重复项
    def dropDuplicatesFirstDate(self):
        dates = pd.read_excel(self.path)
        date = dates.drop_duplicates()
        # 重置索引，从0重新开始
        date = date.reset_index(drop=True)
        return date

    # TAG：删除所有重复项
    def dropDuplicatesALLDate(self):
        dates = pd.read_excel(self.path)
        date = dates.drop_duplicates(keep=False)
        # 重置索引，从0重新开始
        date = date.reset_index(drop=True)
        return date

    # TAG：指定列去重
    def dropDuplicatesColumnDate(self):
        dates = pd.read_excel(self.path)
        date = dates.drop_duplicates(subset=['列名'] ,keep=False)
        # 重置索引，从0重新开始
        date = date.reset_index(drop=True)
        return date

    # TAG：指定多列同时去重
    def dropDuplicatesMoreColumnDate(self):
        dates = pd.read_excel(self.path)
        date = dates.drop_duplicates(['列名1', '列名2'] ,keep=False)
        # 重置索引，从0重新开始
        date = date.reset_index(drop=True)
        return date

'''缺省值处理'''
class defaultValueDates():
    def __init__(self, path):
        self.path = path

    # TAG：检查缺省值 1
    def reindexDateIsnull(self):
        dates = pd.read_excel(self.path)
        date = dates.reindex(['索引值'])
        print(date.isnull())

    # TAG：检查缺省值 2
    def reindexDateNotnull(self):
        dates = pd.read_excel(self.path)
        date = dates.reindex(['索引值'])
        print(date.notnull())

    # TAG：缺失数据计算
    def sumNullDate(self):
        dates = pd.read_excel(self.path)
        date = dates.reindex(['索引值'])
        date = date['列名'].sum()
        return date
    
    # TAG：清理并填充缺失值 - 用标量值替换缺省值
    def fillNaDate(self):
        dates = pd.read_excel(self.path)
        date = dates.reindex(['索引值'])
        # 用0填充缺省值
        date = date.fillna(0)
        return date

    # TAG：清理并填充缺失值 - 向前填充缺省值
    def ffillDate(self):
        dates = pd.read_excel(self.path)
        date = dates.reindex(['索引值'])
        # 将数据向前填充
        date = date.fillna(method='ffill')
        return date

    # TAG：清理并填充缺失值 - 向后填充缺省值
    def bfillDate(self):
        dates = pd.read_excel(self.path)
        date = dates.reindex(['索引值'])
        # 将数据向后填充
        date = date.fillna(method='bfill')
        return date

    # TAG：使用replace替换通用值
    def replaceDate(self):
        dates = pd.read_excel(self.path)
        date = dates.reindex(['索引值'])
        date = date.replace('值')
        return date

    # TAG：整行删除缺省值
    def dropNaDate(self):
        dates = pd.read_excel(self.path)
        date = dates.reindex(['索引值'])
        date = date.dropna()
        return date

    # TAG：整列删除缺省值
    def dropNaDate(self):
        dates = pd.read_excel(self.path)
        date = dates.reindex(['索引值'])
        date = date.dropna(axis=1)
        return date














