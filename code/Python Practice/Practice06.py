# -*- coding: utf-8 -*-

'''
题目：输出 9*9 口诀表。 
'''
for x in range(1,10):
	for y in range(1,x+1):
		print("{0}*{1}={2}".format(y,x,x*y),end='\t')
	print('\n')

'''
知道了end参数是以什么为标志换行....
'''