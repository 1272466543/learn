#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
题目：企业发放的奖金根据利润提成。利润 (I) ： 
低于或等于 10 万元时，奖金可提 10%； 
高于 10万元，低于 20 万元时，低于 10 万元的部分按 10%提成，高于 10
万元的部分，可提成 7.5%； 
20 万到 40 万之间时，高于 20 万元的部分，可提成 5%； 
40 万到 60 万之间时，高于 40 万元的部分，可提成 3%； 
60 万到 100 万之间时，高于 60万元的部分，可提成 1.5%， 
高于 100万元时， 
超过 100万元的部分按 1%提成， 
从键盘输入当月利润 I ，求应发放奖金总数？ 
'''
'''
1.分段：想到if....elif...else
2.奖金超过的，一下的提成都是固定的
3.我们要接收利润数，决定以万为单位
'''
#计算奖金数的一个方法

'''
def Bonus(money):
	if money <= 10:
		bonus = money*0.1
	elif money > 10 and money <= 20:
		bonus = 10*0.1+(money-10)*0.075
	elif money > 20 and money <= 40:
		bonus = 10*0.1+10*0.075+(money-20)*0.05
	elif money > 40 and money <= 60:
		bonus = 10*0.1+10*0.075+20*0.05+(money-40)*0.03
	elif money > 60 and money <= 100:
		bonus = 10*0.1+10*0.075+20*0.05+20*0.03+(money-60)*0.015
	else:
		bonus = 10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(money-100)*0.01
	return bonus

money = int(input("请输入利润:"))
print(Bonus(money))
'''

'''
确实自己看的也有点烦，这代码也没谁了
在网上看到另一种解法，方便很多:
'''
#更好的
InMoney = int(input("请输入利润:"))
extract = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
money = [100, 60, 40, 20, 10, 0]
Bonus = 0
for i in range(0,6):
	if InMoney > money[i]:
		Bonus += (InMoney-money[i])*extract[i]
		InMoney = money[i]

print(Bonus)