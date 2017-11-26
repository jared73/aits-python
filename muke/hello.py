# -*- coding:utf-8 -*-

import requests,sys,os
from bs4 import BeautifulSoup
# 用来存放图片等信息
img_list = []
# 只下载前8页
for i in range(1,8):
    r = requests.get("http://www.58pic.com/piccate/9-188-887-default-5_2_0_0_default_0-%s.html" % i)
    soup = BeautifulSoup(r.text,"html.parser")
    img_cls = soup.find_all("div",class_="card-img")
    for img in img_cls:
        img_bean = {"title":"","src":""}
        #print("标题：%s" % img.img["alt"])
        img_bean["title"] = img.img["alt"]
        if img.img["src"][:4] == "data":
            #print(img.img["data-original"])
            img_bean["src"] = img.img["data-original"][:-6]
        else:
            #print(img.img["src"])
            img_bean["src"] = img.img["src"][:-6]
            img_list.append(img_bean)

for imag in img_list:
    print("标题：%s" % imag["title"])
    print("地址：%s" % imag["src"])

    # 存储在本地
    ir = requests.get(imag["src"])
    if ir.status_code == 200:
        open("E:\\img\\%s.%s" % (imag["title"],imag["src"][-3:]),"wb").write(ir.content)