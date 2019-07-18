import os
import markovify
import re
import nltk
import tensorflow as tf
from tensorflow.keras.models import Sequential
import numpy as np
from tensorflow.keras.layers import Dense, Dropout, LSTM

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

def test():
    with open("ye", encoding="mbcs") as f:
        text = f.read()

    text_model = markovify.Text(text, 2)

    # for i in range(5):
    #     print(text_model.make_sentence())

    for i in range(3):
        print(text_model.make_short_sentence(140))


test()