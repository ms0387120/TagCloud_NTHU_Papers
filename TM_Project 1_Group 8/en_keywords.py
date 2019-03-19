# -*- coding: UTF-8 -*-
import json

theses = json.load(open('nthu_thesis20170330.json'))
idx = theses[0].index('外文關鍵詞')

# Count the frequency of each department
all_department = [thesis[2] for thesis in theses[1:]]
from collections import Counter
dept_count= Counter(all_department)

# Convert the list of five most common dept. to the dictionary in order to get its key.
# Then convert it back to list.  
target_dept = list(dict(dept_count.most_common(5)).keys())
target_dept.append("服務科學研究所")


def compute_frequency(dept):
	en_keywords = [thesis[idx] for thesis in theses[1:] if thesis[2] == dept]
	en_KWterms = []
	for thesis_KW in en_keywords:
		for keyword in thesis_KW.split("\n"):
			en_KWterms.append(keyword)
	en_KWterms_count = Counter(en_KWterms)
	return(en_KWterms_count)

for dept in target_dept:
	keywords_freq = compute_frequency(dept)
	file = open(dept, 'w', encoding = 'UTF-8')
	for k,v in keywords_freq.most_common():
		file.write('%s %s\n' % (v, k))
	file.close()
	