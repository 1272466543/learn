#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''

'''
1.将输入的年月份进行匹配并切片
2.转化为struct_time并提取其中的tm_yday中的参数并输出
'''

import time
import re
year = str(input("Please input your time(xxxx.xx.xx):"))
if re.match(r'\d{4}.\d{1-2}.\d{1-2}&',year):
	year = year.split()
	StrTime = time.strptime('{0}-{1}-{2}'.format(year[0],year[1],year[2]),'%Y-%m-%d').tm_yday
	print(StrTime)
else:
	print("连个日期的输不对,你是猪吗?")
	time.sleep(3)
	exit()

'''
如果需要重新输入的话，外面套一个永真循环在输出的时候break退出循环
'''