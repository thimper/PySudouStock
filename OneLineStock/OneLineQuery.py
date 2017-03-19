# -*- coding: utf-8 -*-
'''
Created on 2016年4月17日

@author: liuxiqing
'''
import time
from Tools import TimeTools
from SudouTushare import TuShareAdapter as ta
from progressbar import ProgressBar, SimpleProgress

'''

谷峰距 =  山谷点 与 山峰点的距离，天数

山谷点：一定谷峰距的左边与右边收盘价都在他之上。
山峰点：一定谷峰距的左边与右边收盘价都在他之上
箱体形态：
箱体震荡，大阳线：

山峰点容差：
山峰斜角度：


1.往前找两三个，谷点，与峰点


'''
class OneLineStrategy(object):
    
    bottom_top_interval = 5 
    __code = ''
    __data = None
    '''
    OneLine
    '''
    def __init__(self,code):
        '''
        Constructor
        '''
        self.__code = code
        self.__data = ta.getHistData(self.__code)
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
        
        print 'done'
    
    def getAreaPrice(self):
        self.getSectionPrice(self.__data)
        
    def execute(self):
        pbar = ProgressBar(widgets=[SimpleProgress()], maxval=17).start()
        for i in range(17):
            #time.sleep(0.2)
            pbar.update(i + 1)
        pbar.finish()
        
    '''
          得到N日均线
    '''
    def getKAvg(self,dayNum):
        code  = self.__code
        return self.__data.head(dayNum)['close'].sum/dayNum
        pass
        
if __name__ == "__main__":
    print "start------"
    oneLine = OneLineStrategy()
    oneLine.getAreaPrice('3000222')
    