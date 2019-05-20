

import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet as wn


# get synonyms for each word
def get_synonyms(word):
	synonyms = []
	synonym_data = wn.synsets(word)
	for s in synonym_data:
		synonyms.append(s.lemmas()[0].name())
	synonyms = list(set(synonyms))
	return synonyms


def get_all_synonyms(words):
	synonyms = {}
	for w in words:
		synonyms[w]:get_synonyms(w)
	return synonyms


# generate all possible acronyms


# check to see what acronyms are words