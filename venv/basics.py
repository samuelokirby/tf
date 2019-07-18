import datamuse
import nltk
import markovify

string = "you bald fool watch your mouth I'll throw your plastic ass down south"
ye = "rap_archive.txt"

api = datamuse.Datamuse()

def markovChain(file):
    with open(file, encoding="mbcs") as f:
        text = f.read()
    text_model = markovify.NewlineText(text)

    for i in range(10):
        print(text_model.make_sentence())
        print(text_model.make_sentence_with_start("You"))


def findRelatedWords(word):
    related = api.words(ml=word, max=25)
    print(related)

# def findRelatedWords(word):
#     text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
#
#     related = text.similar(word, 5)
#     #print(related)

def stripPOS(kit, pos):
    selectedList = []
    for var in kit:
        if(var[1] == "JJ" or var[1] == "VBP" or var[1] == 'NN'):
            selectedList.append(var[0])
    print(selectedList)
    return(selectedList)

def findNLTKSubject(userPhrase):
    #ex = "what's up g back it up"
    word = nltk.word_tokenize(userPhrase)
    kit = nltk.pos_tag(word)
    print(kit)
    return(kit)


def main():
    #stripPOS(findNLTKSubject(string))
    findRelatedWords("mouth")


main()
markovChain(ye)