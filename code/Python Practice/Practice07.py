#coding:utf-8

'''
题目：古典问题：有一对兔子，从出生后第 3 个月起每个月都生一对兔子，小兔子长到
第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？ 
'''

'''

'''
def RabbitNum(mouth):
	for x in range(0,mouth):
		if len(rabbit) < 3:
			rabbit.append(1)
		else:
			rabbit.append(rabbit[-1]+rabbit[-3])
	return rabbit[-1]

rabbit = []
mouth = int(input("请输入第几个月:"))
#mouth = 10
'''for x in range(1,mouth):
	if len(rabbit) < 3:
		rabbit.append(1)
	else:
		rabbit.append(rabbit[-1]+rabbit[-3])'''
print("一共有{0}只兔子".format(RabbitNum(mouth)))
