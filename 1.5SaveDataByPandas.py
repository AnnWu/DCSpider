import requests
from lxml import  etree
url = "https://book.douban.com/subject/1084336/comments/"


#使用get方法发送请求，返回包含网页数据的Response并存储到Response对象r中,返回文本内容
r = requests.get(url).text
#解析数据，返回xml结构
s = etree.HTML(r)

file = s.xpath('//div[@class="comment"]/p/span/text()')

import pandas as pd
df = pd.DataFrame(file)
df.to_excel('pinglun.xlsx')