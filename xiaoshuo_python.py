# -*- coding: gb2312 -*-
import requests,os
from bs4 import BeautifulSoup
'''
    扒取笔趣网小说站小说
'''
__author__ = "作者"

# requests 工具
def request_tool(url):
    response = requests.get(url)
    # 转换编码
    response.encoding = 'gbk'
    return response.text

# 获取所有章节
def section_fun():
    # 章节列表
    section_list = []
    soup = BeautifulSoup(request_tool("http://www.cangqionglongqi.com/hunwushuangxiu/"),"html.parser")
    divList = soup.find_all(id="list")
    base_url = "http://www.cangqionglongqi.com/hunwushuangxiu/"
    for div in divList:
        for a in div.find_all("a"):
            section_list.append({"title":a.text,"src":base_url + a.get("href")})
    return section_list

# 获取章节内容
def crawl_text(path):
    soup = BeautifulSoup(request_tool(path),"html.parser")
    return soup.find(attrs={"id":"content"}).text

# 主函数
if __name__ == "__main__":
    for section in section_fun():
        # 创建一个目录存放小说
        if os.path.exists("xs") == False:
            os.mkdir("xs")
        print("正在下载 =====> %s" % (section.get("title")))
        # 为每一章创建一个文本
        try:
            # print(crawl_text(section.get("src")))
            with open("xs/"+section.get("title") +".txt","w",encoding="utf-8") as f:
                f.write(crawl_text(section.get("src")))
        except Exception as e:
            print("创建文件异常：%s " % e)
