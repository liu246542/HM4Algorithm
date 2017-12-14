#!/usr/bin/python3
#coding=utf-8

import nltk
from functools import reduce

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
			wordDict.setdefault(word.strip().lower(),[0.5,0.5]) # [垃圾邮件概率，正常邮件概率]
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


#-- 计算每个单词的条件概率
#++ 计算每封邮件的概率
def cotWordPro(ewords,wordDict):
	pro_res = []
	for sin_word in ewords:
		[pws,pwn] = wordDict.get(sin_word,[0.4,0.4])
		sin_res = 0 if (pws + pwn)==0 else pws+pwn
		# pws/(pws + pwn)
		pro_res.append(sin_res)
	pro_res.sort(reverse = True)
	pro_res = pro_res[0:15]
	pro_mup = reduce(lambda x,y: x*y,pro_res)
	ipr_res = list(map(lambda x: 1-x,pro_res))
	ipr_mup = reduce(lambda x,y: x*y,ipr_res)
	return (pro_mup / (pro_mup + ipr_mup))

# 预测
def predict(email_list,wordDict):
	email_words = splitWord(email_list)
	## 计算每个单词的概率
	## 如果没有的话，就
	th_value = 0.9
	pre_res = []
	for ewords in email_words:
		con_res = 1 if cotWordPro(ewords,wordDict) > th_value else 0
		pre_res.append(con_res)	
	return pre_res