'''
Author: Zyh
Date: 2022-07-16 17:38:11
LastEditTime: 2022-07-16 23:51:26
Description: 描述性统计类，主要用于简单的统计计算数据
FilePath: \1 - Pandas\statisticsDate.py
'''

import pandas as pd

class statisticsDates():
    def __init__(self, path):
        self.path = path

    # TAG:统计某个非空值的数量
    def countDates(self):
        dates = pd.read_excel(self.path)
        date = dates.count()
        return date
    
    # TAG:求和
    def sumDates(self):
        dates = pd.read_excel(self.path)
        date = dates.sum()
        return date

    # TAG:求均值
    def meanDates(self):
        dates = pd.read_excel(self.path)
        date = dates.mean()
        return date

    # TAG:求中位数
    def medianDates(self):
        dates = pd.read_excel(self.path)
        date = dates.median()
        return date

    # TAG:求众数
    def modeDates(self):
        dates = pd.read_excel(self.path)
        date = dates.mode()
        return date

    # TAG:求标准差
    def stdDates(self):
        dates = pd.read_excel(self.path)
        date = dates.std()
        return date

    # TAG:求最小值
    def minDates(self):
        dates = pd.read_excel(self.path)
        date = dates.min()
        return date

    # TAG:求最大值
    def maxDates(self):
        dates = pd.read_excel(self.path)
        date = dates.max()
        return date

    # TAG:求绝对值
    def absDates(self):
        dates = pd.read_excel(self.path)
        date = dates.abs()
        return date

    # TAG:求最大值
    def maxDates(self):
        dates = pd.read_excel(self.path)
        date = dates.max()
        return date

    # TAG:求所有数值的乘积
    def prodDates(self):
        dates = pd.read_excel(self.path)
        date = dates.prod()
        return date

    # TAG:按照行累加
    def cumsunDates_0(self):
        dates = pd.read_excel(self.path)
        date = dates.cumsun(axis=0)
        return date

    # TAG:按照列累加
    def cumsunDates_1(self):
        dates = pd.read_excel(self.path)
        date = dates.cumsun(axis=1)
        return date

    # TAG:按照行累积
    def cumprodDates_0(self):
        dates = pd.read_excel(self.path)
        date = dates.cumprod(axis=0)
        return date

    # TAG:按照列累积
    def cumprodDates_1(self):
        dates = pd.read_excel(self.path)
        date = dates.cumprod(axis=1)
        return date

    # TAG:计算数列或变量之间的相关系数，取值-1到1，值越大表示关联性越强
    def corrDates(self):
        dates = pd.read_excel(self.path)
        date = dates.corr()
        return date

    # TAG:数据汇总描述
    def describeDates(self):
        dates = pd.read_excel(self.path)
        date = dates.describe()
        return date

    # TAG:数据汇总描述，对字符列进行统计信息描述
    def describeDates(self):
        dates = pd.read_excel(self.path)
        date = dates.describe(include=['object'])
        return date

    # TAG:数据汇总描述，对数字列进行统计信息描述
    def describeDates(self):
        dates = pd.read_excel(self.path)
        date = dates.describe(include='number')
        return date

    # TAG:数据汇总描述，汇总所有列的统计信息
    def describeDates(self):
        dates = pd.read_excel(self.path)
        date = dates.describe(include='all')
        return date
