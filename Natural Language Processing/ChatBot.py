import json
import random
import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()




with open('data.json', 'r') as f:
    intents = json.load(f)

ignoreList = ["?", ".", ",", "!"]


def tokenize(inp):
    return nltk.word_tokenize(inp)

def toLower(inp):
    for i in range(len(inp)):
        inp[i] = inp[i].lower()
    return inp

def ignore(inp):
    indicies = []
    for i in range(len(inp)):
        ignored = False
        for j in range(len(ignoreList)):
            if ignored == False:
                if inp[i] == ignoreList[j]:
                    ignored = True
        if ignored == True:
            indicies.append(i)

    for i, e in reversed(list(enumerate(indicies))):
        inp.pop(e)

    return inp

def stem(inp):
    for i in range(len(inp)):
        inp[i] = stemmer.stem(inp[i])

    return inp


def process(inp):
    input = tokenize(inp)
    input = toLower(input)
    input = ignore(input)
    input = stem(input)
    return input

text = "How you doing?"
print(process(text))
