#-*- coding:utf-8 -*-

import requests

def getHtmlText(url):
    try:
        r=requests.get(url,timeout=20)
        r.raise_for_status()
        print(r.apparent_encoding)
        r.encoding='utf-8'
        return r.text
    except:
        return "getHtmlERR"

from bs4 import BeautifulSoup
def parseHtml(rtext):
    try:
        soup=BeautifulSoup(rtext,'lxml')
        return soup.find_all('span','short')
    except:
        return "parseHtmlERR"    


import pandas
def saveDataInCsv(allData,path):
    comments = []
    for data in allData :
        comments.append(data.string)
    df=pandas.DataFrame(comments)

     # 解决保存到csv文件时出现乱码问题 encoding="utf_8_sig"
    df.to_csv(path,encoding="gbk")


if __name__=='__main__':
    url="https://book.douban.com/subject/26818878/comments/"
    # print (getHtmlText(url))
    rtext = getHtmlText(url)
    allData = parseHtml(rtext)
    saveDataInCsv(allData, 'DouBanComments.csv')