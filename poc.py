import spacy
import en_core_web_sm
import pprint
import numpy as np

def check_tuple_is(tup, nature):
    return tup[1] == nature

def search_sequence(arr):
    result = []
    max_iter = len(arr) if len(arr)%3 == 0 else len(arr) - (len(arr)%3) -1
    for index in range(max_iter):
        left = arr[index]
        center = arr[index+1]
        right = arr[index+2]

        if left[1] == 'NOUN' and center[1] == 'CCONJ' and right[1] == 'NOUN':
            result.append([left, center, right])
    
    return result

def extract_words(capture):
    return " ".join([ word[0] for word in capture ])
    

nlp = en_core_web_sm.load()

tolkien = open('CHAPTER_1.txt').read()

doc = nlp(tolkien)

raw_parsing = [(w.text, w.pos_) for w in doc]
pprint.pprint(raw_parsing)

pretty = np.array(raw_parsing)

noun_and_noun = search_sequence(raw_parsing)

result = [ extract_words(capture) for capture in noun_and_noun ]

pprint.pprint(result)