#!/usr/bin/python3
#coding=utf-8

import nltk
from functools import reduce

# text processing
def splitWord(listCont):
	raw_words = []
	for email in listCont:
		rule_word = nltk.RegexpTokenizer("[\w']{2,}")
		raw_lines = rule_word.tokenize(email)
		raw_lines.pop(0) # discard the string 'Subject'
		raw_words.append(raw_lines)
	return raw_words

# construct dictionary
def constDict(listCont):
	wordDict = {}
	raw_words = splitWord(listCont)
	for email in raw_words:
		for word in email:
			wordDict.setdefault(word.strip().lower(),[0.5,0.5]) # [spam，normal]
	# print(len(wordDict))
	return wordDict

# count the words frequency
def count_num(ema_word,sin_word):
	count = 0
	for email in ema_word:
		if sin_word in email: count += 1
	return count

# train
def train(spaEmail,norEmail,wordDict):
	spa_Email = splitWord(spaEmail) # list(list())类型
	nor_Email = splitWord(norEmail)
	len_smail = len(spa_Email)
	len_nmail = len(nor_Email)
	for sin_word in list(wordDict):
		num_spa = count_num(spa_Email,sin_word)
		num_nor = count_num(nor_Email,sin_word)
		# wordDict[sin_word] = [(num_spa) / (len_smail), (num_nor) / (len_nmail)]
		# wordDict[sin_word] = [(num_spa + 1) / (num_spa + len_smail), (num_nor + 1) / (num_nor + len_nmail)]
		if ((num_spa + num_nor) == (len_smail + len_nmail)) or (num_spa + num_nor < 5):
			wordDict.pop(sin_word)
		else :
			wordDict[sin_word] = [(num_spa + 1) / (num_spa + len_smail), (num_nor + 1) / (num_nor + len_nmail)]
	return wordDict

# count the joint probability
def cotWordPro(ewords,wordDict):
	pro_res = []
	for sin_word in ewords:
		[pws,pwn] = wordDict.get(sin_word,[0.4,0.4])
		sin_res = pws / (pws + pwn)
		pro_res.append(sin_res)
	pro_mup = reduce(lambda x,y: x*y,pro_res)
	ipr_res = list(map(lambda x: 1-x,pro_res))
	ipr_mup = reduce(lambda x,y: x*y,ipr_res)
	return 1 if  (pro_mup + ipr_mup) ==0 else pro_mup / (pro_mup + ipr_mup)

# predict
def predict(email_list,wordDict):
	email_words = splitWord(email_list)
	th_value = 0.9 # threshold value
	pre_res = []
	for ewords in email_words:
		con_res = 1 if cotWordPro(ewords,wordDict) > th_value else 0
		pre_res.append(con_res)	
	return pre_res