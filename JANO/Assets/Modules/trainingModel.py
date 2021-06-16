import json
import random
import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

with open('Assets/Modules/data.json', 'r') as f:
    intents = json.load(f)


#with open('data.json', 'r') as f:
    #intents = json.load(f)

ignoreList = ["?", ".", ",", "!", "a", "the", "and"]


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

def remove_duplicates(arr):

    dupList = []
    for i in range(len(arr)):
        if arr[i] in dupList:
            pass
        else:
            dupList.append(arr[i])

    return dupList



# ------------------------------------------------------- #
def respond(inp, intents):


    probabilities = []
    print(inp)
    for i in range(len(intents['intents'])):


        all_words = []
        for j in range(len(intents['intents'][i]['patterns'])):
            processed_phrase = process(intents['intents'][i]['patterns'][j])
            all_words.extend(processed_phrase)
        all_words.sort()

        all_words = remove_duplicates(all_words)

        output_array = []
        for j in range(len(all_words)):
            if all_words[j] in inp:
                output_array.append(1)
            else:
                output_array.append(0)

        prob = 0
        for j in range(len(output_array)):
            if output_array[j] == 1:
                prob += 1
        probabilities.append(prob)

    final = -1
    finalValue = -1
    for i in range(len(probabilities)):
        if probabilities[i] >= finalValue:
            finalValue = probabilities[i]
            final = i

    if final == -1:
        final = 0

    rand = random.uniform(0, 1)
    rand = np.floor(rand * len(intents['intents'][final]['responses']))


    return intents['intents'][final]['responses'][int(rand)], intents['intents'][final]['tag']



def respondB(inp, intents):

    probabilities = []
    print(inp)
    for i in range(len(intents['intents'])):


        phrases = []
        prob = -1
        for j in range(len(intents['intents'][i]['patterns'])):
            processed_phrase = process(intents['intents'][i]['patterns'][j])
            phrases.append(processed_phrase)

        print('INTENT', intents['intents'][i]['tag'])

        for j in range(len(phrases)):
            similarity = 0
            tot = 1

            for k in range(len(phrases[j])):
                if phrases[j][k] in inp:
                    similarity += 1
                tot = len(inp) + len(phrases[j])
                tot = tot / 2

            if similarity/tot > prob:
                prob = similarity/tot
        probabilities.append(prob)
    print(probabilities)
    final = -1
    finalValue = -1
    for i in range(len(probabilities)):
        if probabilities[i] >= finalValue:
            finalValue = probabilities[i]
            final = i

    if final == -1:
        final = 0

    rand = random.uniform(0, 1)
    rand = np.floor(rand * len(intents['intents'][final]['responses']))

    return intents['intents'][final]['responses'][int(rand)], intents['intents'][final]['tag']

