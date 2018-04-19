
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("xyj.txt","r",encoding='utf-8',errors = 'ignore') as f:
	fr = f.read()
	
characters = []
stat = {}

for line in fr:
	line = line.strip()
	if len(line) == 0:
		continue
	for x in range(0,len(line)):
		if line[x] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……','[',']','/',':']:
			continue
		if not line[x] in characters:
			characters.append(line[x])
		if not line[x] in stat:
			stat[line[x]] = 0
		stat[line[x]] += 1

stat = sorted(stat.items(),key = lambda item:item[1],reverse=True)



with open("date.txt","w",encoding='utf-8') as f:
	for item in stat:
		f.write(item[0] + ":" + str(item[1]) + "\n")

'''
总结：
	文本中有错误符号：errors = 'ignore'
	读取中文字符：encoding='utf-8'
	文件读写：with open('txt','r/w',encoding='',errors='')as f:
			读： fr=f.read()
			写可以不赋值直接使用
	str.strip() 除去文本的空格()
	str.split() 字符串的切片
	sorted() 排序函数返回的是一个list
'''