import argparse
import nltk, re, string
import pandas as pd
from collections import Counter

def letter_only(input):
	r = re.match('^[a-zA-Z]+$', input)
	if r == None:
		return False
	else:
		return True


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--infile', default='content.txt', help='input filename')
ap.add_argument('-o', '--output', default='cnt.csv', help='output filename')
args = vars(ap.parse_args())

infile = args['infile']
output = args['output']

filename = open(infile, 'r')
words = re.findall(r'\w+', open(infile).read().lower())
wordfreqs = Counter(words)
filename.close()

word_lst = []
count_lst = []
output_dict = {}

for word, count in wordfreqs.items():
	word_lst.append(word)
	count_lst.append(count)
	
output_dict = { 'word': word_lst,
				'count': count_lst }

df = pd.DataFrame.from_dict(output_dict)
df = df.sort_values(by=['count'], ascending=False)
df.to_csv(output, index=False)
