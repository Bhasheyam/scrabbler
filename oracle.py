# -*- coding: utf-8 -*-

#getting the words in the text file in an array, to use it as a dictionary.

import sys


#getting the dictionary words in an list
def load():
    words = open("B:\Oracle\words.txt")
    dictionarywords=[]
    for i in words:
	dictionarywords.append((i.split())[0])
    print("came")
    return dictionarywords
    
    
    
# SPecial filter for dupication



#selection of the words for alphabets



#pre-fix
def prefix(dic,keyref):
    resultset=[]
    key=list(keyref)
    length=len(key)
    for word in dic:
        if(list(word[:length])==key):
            resultset.append(word)
    
    return resultset



#Suffix
def suffix(dic,keyref):
    resultset=[]
    key=list(keyref)
    length=len(key)
    for word in dic:
        if(list(word[-length:])==key):
            resultset.append(word)
    print("called")
    return resultset



#define the main according the user input
def main(arg):
    world=load()
    if(arg[0]=='--suffix'):
        result = open("B:\Oracle\output.txt","w")
        for word in suffix(world,arg[1]):
          result.write(word)
          result.write("\n")
    if(arg[0]=="--prefix"):
        result = open("B:\Oracle\output.txt","w")
        for word in prefix(world,arg[1]):
          result.write(word)
          result.write("\n")
  
        
                    
#main   
if __name__ == "__main__":
   main(sys.argv[1:])