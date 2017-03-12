from collections import Counter
file=open("C:/Users/user/Desktop/作業二/building_global_community.txt","r")
wordCounter= {}
for line in file:
	word_list = line.replace(',',' ,').replace('?',' ?').replace('.',' .').replace(':',' : ').replace('"',' " ').replace(';',' ; ').replace('\'',' \'').lower().split()
	for word in word_list:
		if word not in wordCounter:
			wordCounter[word]= 1
		else:
			wordCounter[word]+=1
wordCounter= Counter(wordCounter)
wordCounter.most_common(20)
file.close()
