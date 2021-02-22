from typing import Counter
import time


def WordCount(paragraph):
    bow = paragraph.split()
    return (len(bow))

def wordsplit_opt(sentance , delimiters=['?','1','=','^','%','$','/' ,'(','*',' ', ',', '\n', '\t']):
    before = time.time()*1000
    bow = []
    pt1=0
    de_set=set(delimiters)
    print(len(sentance))
    #hello World
    #h
    for i in range(len(sentance)):
        if(sentance[i] in de_set):
            if (sentance[pt1] not in de_set):
                bow.append(sentance[pt1:i])
            pt1=i+1
    bow.append(sentance[pt1:len(sentance)])
    print(time.time()*1000-before)
    return bow

def wordsplit(sentance , delimiters=['?','1','=','^','%','$', '/' ,'(','*',' ', ',', '\n', '\t']):
    before = time.time()*1000
    bow = []
    temp=""
    de_set=set(delimiters)
    for i in range(len(sentance)):
        if(sentance[i] in de_set):
            if(temp):
                bow.append(temp)
                temp=""
        else:
            temp +=sentance[i]
    bow.append(temp)
    print(time.time()*1000-before)
    return bow



x="Heloow / HI, *Wor*ld"
before = time.time()*1000
# print(wordsplit2(x))
print(wordsplit_opt(x))
print(len(wordsplit_opt(x)))
#print(len(wordsplit(x)))