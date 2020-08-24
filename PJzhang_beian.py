#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests,sys,time
from bs4 import BeautifulSoup

def get_dingjiicp(dingjiicp):
    url="http://icp.chinaz.com/"+dingjiicp
    req=requests.get(url)
    soup=BeautifulSoup(req.text,"html.parser")
    result=soup.find("ul",attrs={"class":"bor-t1s IcpMain01"})
    if result:
        print(dingjiicp,result.strong.text,result.a.text,result.font.text)
    else:
        print(dingjiicp,"未查询到相关备案网站")

def get_dingji(dingji):
    result=[]
    for i in dingji:
        field=i.split(".")
        dingji1=field[-2]+"."+field[-1]
        if dingji1=="com.cn":
            dingji1=field[-3]+"."+dingji1
        result.append(dingji1)
    for i in list(set(result)):
        get_dingjiicp(i)
        time.sleep(10)
        
if __name__=="__main__":
    dingjiicp=sys.argv[1]
    with open(dingjiicp,'r') as f:
        fin=f.read().splitlines()
    get_dingji(fin)