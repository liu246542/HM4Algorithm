#!/usr/bin/python3
# coding = utf-8

import nltk
import csv

# 文本处理函数
# 训练函数
# 测试函数

# 分词
def splitWord(listCont):
	# raw_words = set() # 不重复
	raw_words = [] # 重复
	for email in listCont:
		rule_word = nltk.RegexpTokenizer("[\w']{2,}")
		raw_lines = rule_word.tokenize(email)
		raw_lines.pop(0) # 去掉第一个Subject

		# raw_words.update(set(raw_lines)) # 不重复
		# raw_words.extend(raw_lines) # 重复
		raw_words.append(raw_lines) # 保证邮件
	# print(len(raw_words))
	return raw_words

# 构建
def constDict(listCont):
	wordDict = {}
	raw_words = splitWord(listCont)
	for email in raw_words:
		for word in email:
			wordDict.setdefault(word.strip().lower(),[0.5,0.5]) # [好概率，坏概率]
	# print(len(wordDict))
	return wordDict


# 计数
def count_num(ema_word,sin_word):
	count = 0
	for email in ema_word:
		if sin_word in email: count += 1
	return count

# 训练
def train(spaEmail,norEmail,wordDict):
	spa_Email = splitWord(spaEmail) # list(list())类型
	nor_Email = splitWord(norEmail)
	len_smail = len(spa_Email)
	len_nmail = len(nor_Email)
	for sin_word in wordDict:
		num_spa = count_num(spa_Email,sin_word)
		num_nor = count_num(nor_Email,sin_word)
		wordDict[sin_word] = [num_spa / len_smail, num_nor / len_nmail]
	return wordDict



if __name__ == '__main__':
	data_file = csv.reader(open('data/assignment1_data.csv','r'))
	spamEmail = [] # 垃圾邮件
	normalEmail = [] # 正常邮件
	for item in data_file:
		if item[1] == '0':
			normalEmail.append(item[0])
		elif item[1] == '1':
			spamEmail.append(item[0])

	# print(constDict(normalEmail[0:2]))
	# splitWord(spamEmail[0:2])	
	wordDict = constDict(normalEmail[0:2])
	wordDict = train(spamEmail[0:10],normalEmail[0:10],wordDict)
	print(wordDict)

#print(len(healEmail)) # 4360
#print(len(spamEmail)) # 1368

