# -*- coding: utf-8 -*-
'''
Created on 2016年4月17日

@author: Administrator
'''
import time,datetime,calendar

def get_curday():
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))


def get_day_fromcur(months):
    date1 = datetime.date.today()
    return add_months(date1, months)
'''
'''
def add_months(sourcedate,months):
    month = sourcedate.month - 1 + months
    year = int(sourcedate.year + month / 12 )
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return datetime.date(year,month,day)

if __name__=="__main__":
    print add_months(datetime.date.today(), 12)