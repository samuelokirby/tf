"Reverse markov chain attempt #2"
from textwrap import wrap
import random

string = "Outside the wind was rising, clawing at the shutters of his chamber. Ser Kevan pushed himself to " \
    "his feet. Time to face the lioness in her den. We have pulled her claws. Jaime, though … But no, he would " \
    "that not that brood that on that that"

hashmap = {}

with open('rap_archive.txt', 'r') as file:
    text = file.read()

def reverseOrder(string):
    a=string.split()
    a.reverse()
    result = " ".join(a)
    list = []
    print(list)
    return result

"generateLine starts to build the sentence backwards with a starting word."
def generateLine(startWord):
    string = startWord

    next = random.choice(hashmap.get(string))
    for i in range(10):
        string += " " + next
        next = random.choice(hashmap.get(next))




def createChain(source):
    reversed = reverseOrder(source)
    a = reversed.split()
    bigrams = []
    print(a)
    # for i in range(len(a)-1):
    #     bigram = a[i] + " " + a[i+1]
    #     bigrams.append(bigram)
    # print(bigrams)


    for i in range(len(a)-1):
        b = a[i].lower()
        if(b not in hashmap):
            newList = []
            newEntry = {b:newList}
            hashmap.update(newEntry)
        else:
            # grab the array list
            print(hashmap.get(b))
            values = hashmap.get(b)
            values.append(a[i+1])

        # get the next word as the next ngram
    print("PEBIS")
    print(hashmap.get("you"))




def main():
    createChain(text)
    generateLine("you")
    #reverseOrder(string)

main()