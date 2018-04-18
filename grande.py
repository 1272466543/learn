#!/usr/bin/env python3
# -*- coding: utf-8 -*-
grande={'first':50,'second':65,'third':80}
exit=int(input('欢迎使用大学成绩登记查询系统！进入系统请按1，请按任意键课退出\n'))
while exit == 1:
	meau=('1.录入','2.查询','3.修改','4.成绩删除','5.退出')
	for x in meau:
		print(x)
	org = int(input('请输入你想操作的序号:'))
	if org == 1:
		name = input('请输入姓名:')
		grande[name] = int(input('请输入成绩:'))
		print('录入成功\n正在返回菜单')
	elif org == 2:
		name = input('请输入你想查询的姓名:')
		if name in grande:
			print('成绩是:',grande[name],'\n正在返回菜单')
		else:
			print('没有这个人的成绩')
			continue
	elif org == 3:
		name = input('请输入你想修改成绩的姓名:')
		if name in grande:
			grande[name] = int(input('请输入要修改的成绩:'))
			print('已修改成功\n正在返回菜单')
		else:
			print('没有这个人的成绩')
			continue
	elif org == 4:
		name = input('请输入你想删除成绩的姓名:')
		if name in grande:
			grande.pop(name)
			print('已删除成功\n正在返回菜单')
		else:
			print('没有这个人的成绩')
			continue
	else:
		print('系统正在退出。。。')
		break