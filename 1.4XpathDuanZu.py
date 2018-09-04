import requests
from lxml import etree

def getHtmlPage(url):
    try:
        r=requests.get(url)
        return r.text
    except ValueError as err:
        print (err)
        print("GetPageErr")


'''
使用Xpath解析网页数据的步骤
    1.从lxml导入etree
    2.解析数据，返回xml结构
    3.使用.xpath()寻找和定位数据
'''
def parsePageByXpath(html, path):

    s=etree.HTML(html)
    #print(path)
    #print(s.xpath(path))
    return s.xpath(path)


if __name__=="__main__":
    url='http://sz.xiaozhu.com/'
    path='//div[@id="page_list"]/ul/li/div[2]/span[1]/i/text()'   

    html=getHtmlPage(url)
    print(parsePageByXpath(html,path))