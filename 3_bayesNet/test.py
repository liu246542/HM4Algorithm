#!/usr/bin/python3
# coding = utf-8

import csv
from email_filter import constDict,train,predict

if __name__ == '__main__':
	data_file = csv.reader(open('data/assignment1_data.csv','r'))
	spamEmail = [] # spam emails list
	normalEmail = [] # normal emails list
	for item in data_file:
		if item[1] == '0':
			normalEmail.append(item[0])
		elif item[1] == '1':
			spamEmail.append(item[0])
	print('---text processing---')
	wordDict = constDict(normalEmail[0:1000] + spamEmail[0:1000])
	print('---training----------')
	wordDict = train(spamEmail[0:1000],normalEmail[0:1000],wordDict)
	print('---predicting--------')
	nor_pre_result = predict(normalEmail[4160:4360],wordDict)
	spa_pre_result = predict(spamEmail[1168:1368],wordDict)

	a = spa_pre_result.count(1)
	b = nor_pre_result.count(1)
	c = spa_pre_result.count(0)

	print('Recall Rate : {:.2}'.format(a/(a + c)))
	print('Precision Rate: {:.2}'.format(a/(a + b)))

#print(len(healEmail)) # 4360
#print(len(spamEmail)) # 1368