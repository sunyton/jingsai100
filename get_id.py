#!/usr/lib/python2.7
#coding=utf-8

import re

fil1 = open("test_dic.json")
all_qu = fil1.read()
all_qujs = eval(all_qu)

fil2 = open("ques_list.json")
all_ans = fil2.read()
all_ansls = all_ans

print all_ans


