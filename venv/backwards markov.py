import markovify
import random
#
# def reverseOrder(string):
#
#     a=string.split()
#     a.reverse()
#     result = " ".join(a)
#     print(result)
#     return result
#
# def openFile(fileName):
#
#     with open(fileName, 'r') as file:
#         data = reverseOrder(file.read())
#     print(data)
#     return data
#
# def makeChainWithStarter(word, string):
#     print(string)
#     text_model = markovify.Text(string)
#     print((text_model.make_sentence(10)))
#
#
# def main():
#     makeChainWithStarter("You", openFile("rap_archive.txt"))

text_model = markovify.Text("End motherfucking The is this listing, for all you Thank bend the around down winding it's now but start, the since here been They Billy Labes, Kimu, IceBox, Durbsman, Midgey, Clark, B yanno KaseyBark, he's why That's all and dawg my is Kasey End The here's now")
print(text_model.make_sentence())
