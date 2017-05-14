

import os
import collections
def load():
    working_path = os.path.dirname(__file__) 
    data_path = "words\\words.txt"
    word_loc = os.path.join(working_path, data_path)
    words = open(word_loc)
    dictionarywords=[]
    for i in words:
	dictionarywords.append((i.split())[0])
    return dictionarywords
word=load()
updated=[]
def create(a):
    count1=[]
    b=list(a)
    for l in b:
     c=[]
     c.append(l)
     c.append(b.count(l))
     if(c in count1):
        continue
     count1.append(c)
    print(count1)
    
create("nfjsfnanfawndfonew")
    
