'''
题目：一个整数，它加上 100 后是一个完全平方数，再加上 168 又是一个完全平方数，
请问该数是多少？ 
'''
'''
sqrt(x+100)=m
sqrt(x+168)=n

m,n 取余为0 
'''
import math
x = 0
while 1:
	if math.sqrt(x+100)%1 == 0 and math.sqrt(x+168)%1 == 0:
		print(x)
		break
	else:
		x += 1