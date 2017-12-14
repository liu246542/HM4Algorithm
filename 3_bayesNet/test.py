#!/usr/bin/python3
# coding = utf-8

import csv
from email_filter import constDict,train,predict

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
	wordDict = constDict(normalEmail[0:100] + spamEmail[0:100])
	wordDict = train(normalEmail[0:100],normalEmail[0:100],wordDict)
	# pre_result = predict(spamEmail[101:200],wordDict)
	pre_result = predict(spamEmail[200:300],wordDict)
	print(len(pre_result))
	print(pre_result.count(1))
	print(pre_result.count(1) / len(pre_result))
	# print(wordDict)

#print(len(healEmail)) # 4360
#print(len(spamEmail)) # 1368