# -*- coding: utf-8 -*-

#getting the words in the text file in an array, to use it as a dictionary.

import sys
import os


#fixing the path and creating file
def create(path,mode):
    working_path = os.path.dirname(__file__) 
    data_path = path
    file_loc = os.path.join(working_path, data_path)
    fileloc = open(file_loc,mode)
    return fileloc
   
    
      
#getting the dictionary words in an list
def load():
    words=create("words\\words.txt","r")
    dictionarywords=[]
    for i in words:
	dictionarywords.append((i.split())[0])
    return dictionarywords
    
    
    
# find the given list count
def indexfind(input):
    countindex=[]
    inputlist=list(input)
    for l in inputlist:
     temp=[]
     temp.append(l)
     temp.append(inputlist.count(l))
     if(temp in countindex):
        continue
     countindex.append(temp)
    return countindex
    
   
    
      
# filter for unused alphabets
def filter(dic,inputletters):
   print(len(dic))
   update=prefilter(dic,inputletters)# clalliung the prefilter
   updateddic=prefilter(dic,inputletters)# optimize the dictionary according to the input
   print(len(update))
   alphabets="abcdefghijklmnopqrstuvwxyz"
   alphalist=list(alphabets)
   for letters in alphalist:
       if(letters in inputletters):
           continue
       for words in update:
           if(letters in words):
               if(words in updateddic): 
                   updateddic.remove(words) 
   print(len(updateddic))
   return updateddic  

#support filter
def prefilter(dic,value):
    resultset=[]
    for letter in value:
        for word in dic:
          if(word[:1]==letter):
            resultset.append(word)
    return resultset

    
#selection of the words for alphabets
def scrabble(indexlist,updated):
    return




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
    world=load()# creating one global reference for all functions 
    
    if(arg[0]=='--suffix'):# handling suffix input
         stringcheck(arg[1])
         result = create("Output\\suffixoutput.txt","w")
         for word in suffix(world,arg[1]):
           result.write(word)
           result.write("\n")
           
    elif(arg[0]=="--prefix"):# handling prefix input
        stringcheck(arg[1])
        result =create("Output\\prefixoutput.txt","w") 
        for word in prefix(world,arg[1]):
          result.write(word)
          result.write("\n")
           
    elif(arg[0].isalpha()): #handling scrabble input
        indexlist=indexfind(arg[0])
        options=set(list(arg[0]))
        updated=filter(world,options)
        print(len(updated))
        print(indexlist)
        print(updated)
        #scrabble(indexlist,updated)
        
    else:
      
        stringcheck("1")# to throw alphabet Error
 
                  
                    
#main   
if __name__ == "__main__":
   main(sys.argv[1:])