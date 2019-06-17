

import itertools

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
def generate_possible_acroynms(list_of_words):
	possible_acronyms = []
	synonyms = [get_synonyms(w) for w in list_of_words]
	synonym_sets = itertools.product(*synonyms)
	for s in synonym_sets:
		acronym = {
			'name': "".join([w[0] for w in s]).lower(),
			'words': s,
			}
		possible_acronyms += [acronym]
	return possible_acronyms



# check to see what acronyms are words