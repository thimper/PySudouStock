# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 20:08:43 2015

@author: Administrator
"""

from SudouMongo.MyMongoClient import MyMongoClient as mgClient
import tushare as ts
from  Tools import TimeTools


def SaveStockList():
    df = ts.get_stock_basics().reset_index()
    mgClient.saveData("stocklist",df)
    return df

def getStockList():
    df = ts.get_stock_basics().reset_index()
    return df

'''
获取个股历史交易数据（包括均线数据），可以通过参数设置获取日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据。本接口只能获取近3年的日线数据，适合搭配均线数据进行选股和分析，如果需要全部历史数据，请调用下一个接口get_h_data()。
参数说明：
code：股票代码，即6位数字代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
start：开始日期，格式YYYY-MM-DD
end：结束日期，格式YYYY-MM-DD
ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
retry_count：当网络异常后重试次数，默认为3
pause:重试时停顿秒数，默认为0

返回值说明：
date：日期
open：开盘价
high：最高价
close：收盘价
low：最低价
volume：成交量
price_change：价格变动
p_change：涨跌幅
ma5：5日均价
ma10：10日均价
ma20:20日均价
v_ma5:5日均量
v_ma10:10日均量
v_ma20:20日均量
turnover:换手率[注：指数无此项]
'''
'''
date          open    high   close     low     volume    p_change  ma5 \
2012-01-11   6.880   7.380   7.060   6.880   14129.96     2.62   7.060
2012-01-12   7.050   7.100   6.980   6.900    7895.19    -1.13   7.020
2012-01-13   6.950   7.000   6.700   6.690    6611.87    -4.01   6.913
2012-01-16   6.680   6.750   6.510   6.480    2941.63    -2.84   6.813
2012-01-17   6.660   6.880   6.860   6.460    8642.57     5.38   6.822
2012-01-18   7.000   7.300   6.890   6.880   13075.40     0.44   6.788
2012-01-19   6.690   6.950   6.890   6.680    6117.32     0.00   6.770
2012-01-20   6.870   7.080   7.010   6.870    6813.09     1.74   6.832
'''
def getHistData(code,ktype="D",start=None,end=None):
    if not start:
        start = TimeTools.get_day_fromcur(-2) 
    if not end:
        end = TimeTools.get_curday()
    print "getHistData:%s到%s" %(start,end)
    return ts.get_hist_data(code,str(start),str(end),ktype)


if __name__=="__main__":
    getStockList()
    print "done!!"