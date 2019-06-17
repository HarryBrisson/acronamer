

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
			'abbr': "".join([w[0] for w in s]).lower(),
			'words': s,
			}
		possible_acronyms += [acronym]
	return possible_acronyms


# check to see what acronyms are words
def filter_out_non_words(possible_acronyms):
	final_acronym_list = []
	for a in possible_acronyms:
		word_details = wn.synsets(a['abbr'])
		if len(word_details)>0:
			final_acronym_list += [a]
	return final_acronym_list


def acronamer(list_of_words):
	possible_acronyms = generate_possible_acroynms(list_of_words)
	final_acronym_list = filter_out_non_words(possible_acronyms)
	return final_acronym_list

