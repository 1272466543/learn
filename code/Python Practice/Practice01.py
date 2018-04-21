#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
题目：有 1、2、3、4 个数字，能组成多少个互不相同且无重复数字的三位数？都是多
少？ 
'''
'''
第一次的想法:把所有的可能列出来并用set去重
'''

'''
Numbers = [1, 2, 3, 4]
Number = []
for x in Numbers:
	for y in Numbers:
		for z in Numbers:
			Number.append(x*100+y*10+z)
Number = set(Number)
print(Number)
'''

'''
利用生成器来生成
是不是可以用利用函数
'''
def ListNum(Numbers):
	Number = []
	for x in Numbers:
		for y in Numbers:
			for z in Numbers:
				Number.append(x*100+y*10+z)
	return Number
	
Numbers = range(1, 5)
Number = set(ListNum(Numbers))	
print(Number)
'''
但好像变得更复杂了....
'''		