'''
题目：输入三个整数 x，y，z，请把这三个数由小到大输出。 
'''
'''
1.输入三个整数
2.可以将其放入一个list
3.用sorted对其进行排序
'''
Numbers = []
for i in range(0,3):
	number = int(input("Please input number:"))
	Numbers.append(number)
Numbers = sorted(Numbers)
print(Numbers)
'''
输入不一样可以用不同的解决办法，如果一次性输入
就用切片分开，组成list
'''