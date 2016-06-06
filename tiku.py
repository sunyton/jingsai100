#!/usr/lib/python2.7
#coding=utf-8

import requests
from lxml import etree


id = 1


while id <736 :
	qus_url = "http://www.jsbys.com.cn/exam/know.aspx?id=" + str(id)
	r = requests.get(qus_url)

	doc = etree.HTML(r.text)
	try:
		ques = doc.xpath("//tr[2]/td/b/text()")
		anse = doc.xpath("//tr[4]/td/font/b/text()")
		id_ti = doc.xpath("//tr[2]/td/b/font/text()")
		ti_id = id_ti[0]
		ques_id = ques[0]
		ans_id = anse[0][5:len(anse[0])]
		all_str = ti_id + ques_id + '\n'+ ans_id + '\n'
		# print all_str
		# print ti_id + ques_id + ans_id

		fl = open("test2.txt","a+")
		fl.write(all_str.encode('utf-8'))
		print str(id) + "finished"
		id = id + 1
	except:

		id = id + 1

fl.close()

