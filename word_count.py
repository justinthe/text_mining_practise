import argparse
import nltk
import re, string
import pandas as pd
from collections import Counter
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def letter_only(input):
	r = re.match('^[a-zA-Z]+$', input)
	if r == None:
		return False
	else:
		return True

factory = StemmerFactory()
stemmer = factory.create_stemmer()

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--infile', default='content.txt', help='input filename')
ap.add_argument('-o', '--output', default='cnt.csv', help='output filename')
args = vars(ap.parse_args())

infile = args['infile']
output = args['output']

# filename = open(infile, 'r')
words = re.findall(r'\w+', open(infile, encoding='utf-8').read().lower())

for idx, word in enumerate(words):
	words[idx] = stemmer.stem(word)
	# word = stemmer.stem(word)
# words = [stemmer.stem(word) for word in words]

wordfreqs = Counter(words)
# filename.close()

word_lst = []
count_lst = []
output_dict = {}

for word, count in wordfreqs.items():
	# if count < 3, discard -> unimportant
	if word not in nltk.corpus.stopwords.words('indonesian') and len(word) > 1 and count > 3:
		word = word.strip(string.punctuation).lower()
		word_lst.append(word)
		count_lst.append(count)
	
output_dict = { 'word': word_lst,
				'count': count_lst }

df = pd.DataFrame.from_dict(output_dict)
df = df.sort_values(by=['count'], ascending=False)
df.to_csv(output, index=False)
