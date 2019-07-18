# Build a Markov chain that abides to Kolmogorov's criterion.
from textwrap import wrap

text = "Dear Sister, by the time you're reading this I'll probably be dead. This is how I think it's gonna happen. Mark will shoot me, then I'll shoot Mark, then Matt will shoot me, then I'll shoot Matt." \
       "P.S. Two cops are going to come in here and read this and shoot each other."

def createNgrams(string, count):
    ngrams = wrap(string, count)

    dict = {}
    for value in range(len(ngrams)):
        if(value != len(ngrams)-1):
            keyArray = []
            print("BUMBO")
            for char in ngrams[value+1]:
                print(char)
                keyArray.append(char)
                entry = {ngrams[value]:keyArray}
                dict.update(entry)


    print(ngrams)


def main():
    createNgrams(text, 4)

main()
