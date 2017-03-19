# -*- coding: utf-8 -*-
"""
Created on Sun Jan 03 09:26:58 2016

@author: Administrator
"""

from pymongo import MongoClient
import tushare as ts
import json

mongoClient = MongoClient("mongodb://mystock:123.@127.0.0.1/stock",port=27017)

class MyMongoClient:
    @staticmethod
    def saveData(collectionName,data):
        mongoClient.stock[collectionName].insert(json.loads(data.to_json(orient="records")))

if __name__== "__main__":
    df = ts.get_tick_data("300033",date="2015-12-31")
    MyMongoClient.saveData("tickdata300033",df.to_json(orient="records"))
    print "done"