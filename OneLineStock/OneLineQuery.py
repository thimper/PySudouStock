# -*- coding: utf-8 -*-
'''
Created on 2016年4月17日

@author: liuxiqing
'''

from Tools import TimeTools
from SudouTushare import TuShareAdapter


'''
谷峰距 =  山谷点 与 山峰点的距离，天数
山谷点：一定谷峰距的左边与右边收盘价都在他之上。
山峰点：一定谷峰距的左边与右边收盘价都在他之上
箱体形态：
箱体震荡，大阳线：
山峰点容差：
山峰斜角度：

'''
class OneLineQuery(object):
    
    bottom_top_interval = 5 
    
    '''
    OneLine
    '''
    def __init__(self):
        '''
        Constructor
        '''
    
    '''
           获取区间价格，山峰点，山谷点，
           默认处理两个时间 的    
    '''
    def getSectionPrice(self,data,start=None,end=None):
        if not start:
            start = TimeTools.get_day_fromcur(-2) 
        if not end:
            end = TimeTools.get_curday()
        print "get Section Price:%s到%s" %(start,end)
        
        
        
if __name__ == "__main__":
    print "start------"
    
    oneLine = OneLineQuery()
    data = TuShareAdapter.getHistData('300222')
    print data
    oneLine.getSectionPrice(data)
    