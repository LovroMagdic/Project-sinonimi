import nltk
import string
from nltk.corpus import wordnet

words = []
words1 = []
words2 = []
words3 = []
words4 = []
final = []
text=''

art = [word.strip(string.punctuation) for word in text.split()]

with open('novo.txt','r', encoding="utf8") as f:
    mylist = list(f)
    for line in mylist:
        text = [word.strip(string.punctuation) for word in line.split()]
        for word in text:
            if word not in words:
                words.append(word)
for each in words:
    syns = wordnet.synsets(each)
    i = 0
    for each1 in syns:
        i = i + 1
    for i in range(i):
        tmp = syns[i].lemmas()[0].name()
        tmp1 = str(each)
        words3.append(tmp)
        if str(tmp) != str(tmp1):
            words1.append(syns[i].lemmas()[0].name())
    for e in words1:
        if e in words:
            words4.append(e)
            words4.append(each)
        words1.clear()

t = len(words4)

for i in range(0, t, 2):
    if (i < t):
        print(words4[i], "  ---> ", words4[i+1])
    else:
        print("Kraj.")




'''with open('tekst.txt','r') as f:
    for line in f:
        for word in line.split():
            if word not in words:
                words.append(word)

from nltk.corpus import wordnet
for each in words:
    syns = wordnet.synsets(each)
    i = 0
    for each1 in syns:
        i = i + 1
    for i in range(i):
        tmp = syns[i].lemmas()[0].name()
        tmp1 = str(each)
        if str(tmp) != str(tmp1):
            words1.append(syns[i].lemmas()[0].name())
print(words)      
for each in words:
    if each in words1:
        final.append(each)

print(words1)
print(words2)'''