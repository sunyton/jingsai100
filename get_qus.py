#!/usr/lib/python2.7
#coding=utf-8



import requests
from lxml import etree


fil1 = open("test_dic.json")
all_qu = fil1.read()
all_qujs = eval(all_qu)
print type(all_qujs)


id_val = 1
list1 = []
userid = "xxxxxxxxx"
headers = {
	
	"Host": "www.jsbys.com.cn",
"Cache-Control": "max-age=0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
"Accept-Encoding": "gzip, deflate, sdch",
"Accept-Language": "en,zh;q=0.8,zh-CN;q=0.6,en-US;q=0.4,zh-TW;q=0.2",
"Connection": "close"


}

while id_val < 51:

	url = "http://www.jsbys.com.cn/exam/MyPaper.aspx?id="+ str(id_val) +"&userid=" + userid

	r2 = requests.get(url=url,headers=headers)

	doc2 = etree.HTML(r2.text)

	qu = doc2.xpath('//tr[2]/td/b/text()')

	qu_str = qu[0]

	print all_qujs.has_key(qu_str)

	# print qu
	haha = all_qujs.get(qu_str)
	print str(id_val) + " OK!"
	list1.append(str(id_val)+": " + haha)

	id_val = id_val + 1

print list1









