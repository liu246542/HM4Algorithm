#!/usr/bin/python3
# coding = utf-8

import nltk
import csv

# 文本处理函数
# 训练函数
# 测试函数

# 分词
def splitWord(listCont):
	raw_words = []
	for address in listCont:
		rule_word = nltk.RegexpTokenizer("[\w']{2,}")
		raw_lines = rule_word.tokenize(address)
		raw_lines.pop(0) # 去掉第一个Subject
		raw_words.append(raw_lines)
	return raw_words

def constDict(listCont):
	wordDict = {}
	raw_lines = splitWord(listCont)
	for word in raw_lines:
		wordDict.setdefault(word.strip().lower(),'0.4')
	return wordDict

# 训练
def train(spaEmail,norEmail):
	pass



	


if __name__ == '__main__':
	data_file = csv.reader(open('data/assignment1_data.csv','r'))
	spamEmail = [] # 垃圾邮件
	normalEmail = [] # 正常邮件
	for item in data_file:
		if item[1] == '0':
			normalEmail.append(item[0])
		elif item[1] == '1':
			spamEmail.append(item[1])

	print(splitWord(normalEmail[0:2]))

#print(len(healEmail)) # 4360
#print(len(spamEmail)) # 1368

