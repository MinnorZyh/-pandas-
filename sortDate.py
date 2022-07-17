'''
Author: Zyh
Date: 2022-07-17 00:49:07
LastEditors: Zyh
LastEditTime: 2022-07-17 10:35:36
Description: 数据排序操作
FilePath: \Pandas\sortDate.py
'''

import pandas as pd

class sortDates():
    def __init__(self, path):
        self.path = path

    # TAG 按行排序
    def sortIndexDates1(self):
        dates = pd.read_excel(self.path)
        date = dates.sort_index()
        return date

    # TAG 按照行标签，倒序排序
    def ascendingDates(self):
        dates = pd.read_excel(self.path)
        date = dates.sort_index(ascending=False)
        return date

    # TAG 按列排序
    def sortIndexDates2(self):
        dates = pd.read_excel(self.path)
        date = dates.sort_index(axis=1)
        return date

    # TAG 指定值排序
    def sortValuesDates(self):
        dates = pd.read_excel(self.path)
        date = dates.sort_values(by=['值1', '值2', ..., '值n'])
        return date

    # TAG 归并算法
    def amergesortDates(self):
        dates = pd.read_excel(self.path)
        date = dates.sort_values(by='值1', kind='mergesort')
        return date

    # TAG 堆排序
    def heapsortDates(self):
        dates = pd.read_excel(self.path)
        date = dates.sort_values(by='值1', kind='heapsort')
        return date

    # TAG 快速排序
    def quicksortDates(self):
        dates = pd.read_excel(self.path)
        date = dates.sort_values(by='值1', kind='quicksort')
        return date
