# -*- coding: utf-8 -*-

#getting the words in the text file in an array, to use it as a dictionary.

import sys
import os

#getting the dictionary words in an list
def load():
    working_path = os.path.dirname(__file__) 
    data_path = "words\\words.txt"
    word_loc = os.path.join(working_path, data_path)
    words = open(word_loc)
    dictionarywords=[]
    for i in words:
	dictionarywords.append((i.split())[0])
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
    return resultset
    
    
#check of string
def stringcheck(input):
    print(input)
    if(input.isalpha()):
        return 
    print("Enter only alphabet inputs")
    sys.exit()


#define the main according the user input
def main(arg):
    world=load() 
    if(arg[0]=='--suffix'):
         stringcheck(arg[1])
         working_path = os.path.dirname(__file__) 
         data_path = "Output\\suffixoutput.txt"
         word_loc = os.path.join(working_path, data_path)
         result = open(word_loc,"w")
         for word in suffix(world,arg[1]):
           result.write(word)
           result.write("\n")
           
    elif(arg[0]=="--prefix"):
        stringcheck(arg[1])
        working_path = os.path.dirname(__file__) 
        data_path = "Output\\prefixoutput.txt"
        word_loc = os.path.join(working_path, data_path)
        result = open(word_loc,"w")
        for word in prefix(world,arg[1]):
          result.write(word)
          result.write("\n")
           
    elif(arg[0].isalpha()):
        print("working")
    else:
        stringcheck("1")# to throw alphaber Error
 
                     
   
   
          
    
  
        
                    
#main   
if __name__ == "__main__":
   main(sys.argv[1:])