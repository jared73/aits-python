import importlib

import requests
import re
#下面三行是将windows控制台的编码形式转换成utf-8编码
import sys
importlib.reload(sys)
#创建spider爬虫类
class spider(object) :
    def __init__(self):
        print( u'开始搞事')
    #获取每个页面的源代码
    def getSource(self,url):
        html = requests.get(url)
        #将获得的源代码以utf-8的格式解析
        html.encoding = "utf-8"
        return html.text
    #得到连续的多个课程网页
    def getPages(self,url,total):
        urls=[]
        init_page=int(re.search('page=(\d+)',url,re.S).group(1))
        for i in range(init_page,total+1) :
            #将页面通过正则表达式来替换
            link=re.sub('page=\d+','page=%d'%i,url)
            urls.append(link)
        return urls
    #得到每个课程页中的多个课程
    def getCourses(self,html):
        Courses=re.findall(r'<ul class="clearfix">(.*?)</ul>',html,re.S)
        return Courses

        # 利用正则表达式筛选课程信息
    def getCourseInfo(self, Course):
        info = {}
        # r"pattern" 匹配模式的前面加上r,就不必在转义里面的字符
        info['title'] = re.search(r'<h3 class="course-card-name">(.*?)</h3>',Course, re.S).group(1)
        info['decoration'] =re.search(r'class="course-card-desc">(.*?)</p>',Course, re.S).group(1)
        # 去除字符串两边和中间的空白字符
        peoples = re.search('<span><i class="icon-set_sns"></i>(.*?)</span>',Course,re.S).group(1).strip()
        info['peoples'] = re.sub('\s+', ',', peoples)
        return info

        # 存储课程信息
    def saveAllInfo(self, allInfo):
        f = open("info.txt", 'a')
        for each in allInfo:
            f.writelines('title:' + each['title'] + '\n')
            f.writelines('decoration:' + each['decoration'] + '\n')
            f.writelines('peoples:' + each['peoples'] + '\n\n')
        f.close()

if __name__ == '__main__':
        allInfo = []
        spider = spider()
        url = 'http://www.imooc.com/course/list?page=1'
        urls = spider.getPages(url, 10)
        for each in urls:
            print(u'正在处理%s' % each + '\n')
            content = spider.getSource(each)
            Courses = spider.getCourses(content)
            for Course in Courses:
                info = spider.getCourseInfo(Course)
                allInfo.append(info)
        spider.saveAllInfo(allInfo)