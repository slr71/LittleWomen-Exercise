#!/usr/bin/env python3

import csv
import os
from collections import Counter
import nltk
import pprint

nltk.download('punkt')

with open("LittleWomen.txt") as f:
    little_women = f.read()

little_women_tokens = nltk.word_tokenize(little_women)

only_alpha_tokens = [
    i for i in little_women_tokens if i.isalpha()
]

word_count = Counter(word for word in only_alpha_tokens)

characters = [
    "Kate",
    "Kitty",
    "Amy",
    "Marmee",
    "John",
    "Minnie",
    "Beth",
    "Laurie",
    "Hannah",
    "Jo"
]

for character in characters:
    print(character, word_count[character])

print("{0}.{1}.{2}".format(
    word_count["Jo"],
    word_count["Beth"],
    word_count["Amy"],
))
