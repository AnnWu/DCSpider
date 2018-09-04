import requests
from lxml import etree

url="https://book.douban.com/subject/1084336/comments/"

r=requests.get(url).text

s=etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/span/text()')
#file=s.xpath('//*[@id="comments"]/ul/li/div[2]/p/span/text()')
#print(file)
with open('comments.txt','w',encoding='utf-8') as f :
    for i in file :
	    #print(i)
	    f.write(i+'\n')
