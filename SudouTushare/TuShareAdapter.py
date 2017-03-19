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
'''
参数说明：

code:string,股票代码 e.g. 600848
start:string,开始日期 format：YYYY-MM-DD 为空时取当前日期
end:string,结束日期 format：YYYY-MM-DD 为空时取去年今日
autype:string,复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
index:Boolean，是否是大盘指数，默认为False
retry_count : int, 默认3,如遇网络等问题重复执行的次数
pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
返回值说明：

date : 交易日期 (index)
open : 开盘价
high : 最高价
close : 收盘价
low : 最低价
volume : 成交量
amount : 成交金额
'''
def getAllHistData(code,ktype='D',start=None,end=None):
    if not start:
        start = TimeTools.get_day_fromcur(-2) 
    if not end:
        end = TimeTools.get_curday()
    print "getHistData:%s到%s" %(start,end)
    return ts.get_h_data(code,str(start),str(end),ktype)
'''
code：代码
name:名称
changepercent:涨跌幅
trade:现价
open:开盘价
high:最高价
low:最低价
settlement:昨日收盘价
volume:成交量
turnoverratio:换手率
amount:成交量
per:市盈率
pb:市净率
mktcap:总市值
nmc:流通市值
'''
def getTodayAll():
    return ts.get_today_all()

'''
time：时间
price：成交价格
change：价格变动
volume：成交手
amount：成交金额(元)
type：买卖类型【买盘、卖盘、中性盘】
'''
def getTickData(code,date):
    if not date:
        date = TimeTools.get_day_fromcur(-2) 
    return ts.get_tick_data(code,date)

'''
0：name，股票名字
1：open，今日开盘价
2：pre_close，昨日收盘价
3：price，当前价格
4：high，今日最高价
5：low，今日最低价
6：bid，竞买价，即“买一”报价
7：ask，竞卖价，即“卖一”报价
8：volume，成交量 maybe you need do volume/100
9：amount，成交金额（元 CNY）
10：b1_v，委买一（笔数 bid volume）
11：b1_p，委买一（价格 bid price）
12：b2_v，“买二”
13：b2_p，“买二”
14：b3_v，“买三”
15：b3_p，“买三”
16：b4_v，“买四”
17：b4_p，“买四”
18：b5_v，“买五”
19：b5_p，“买五”
20：a1_v，委卖一（笔数 ask volume）
21：a1_p，委卖一（价格 ask price）
...
30：date，日期；
31：time，时间；
'''
def getRealTimeQuotes(code):
    return ts.get_realtime_quotes()
'''
time：时间
price：当前价格
pchange:涨跌幅
change：价格变动
volume：成交手
amount：成交金额(元)
type：买卖类型【买盘、卖盘、中性盘】
'''
def getTodayTick(code):
    return ts.get_today_ticks()

'''
code:指数代码
name:指数名称
change:涨跌幅
open:开盘点位
preclose:昨日收盘点位
close:收盘点位
high:最高点位
low:最低点位
volume:成交量(手)
amount:成交金额（亿元）
'''
def getIndex():
    return ts.get_index()

'''
参数说明：

code：股票代码，即6位数字代码
date:日期，格式YYYY-MM-DD
vol:手数，默认为400手，输入数值型参数
retry_count : int, 默认3,如遇网络等问题重复执行的次数
pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
返回值说明：

code：代码
name：名称
time：时间
price：当前价格
volume：成交手
preprice ：上一笔价格
type：买卖类型【买盘、卖盘、中性盘】
'''
def getSinaDD(code, date, vol, retry_count, pause):
    return ts.get_sina_dd(code, date, vol, retry_count, pause)

def getStockInfo(code):
    data = ts.get_stock_basics()
    return data.ix[code]
if __name__=="__main__":
    getStockList()
    print "done!!"