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
   
   
   
   
   
# support function for scrabble, Suffix,Prefix and filter
      
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
    

    #check of string
def stringcheck(input):
    if(input.isalpha()):
        return 
    print("Enter only alphabet inputs")
    sys.exit()
    
    
    
    
    
    
# support functions for scrabble  
    #support filter
def prefilter(dic,value):
    resultset=[]
    for letter in value:
        for word in dic:
          if(word[:1]==letter):
            resultset.append(word)
    return resultset
      
# filter for unused alphabets
def filter(dic,inputletters):
   update=prefilter(dic,inputletters)# clalliung the prefilter
   updateddic=prefilter(dic,inputletters)# optimize the dictionary according to the input
   alphabets="abcdefghijklmnopqrstuvwxyz"
   alphalist=list(alphabets)
   for letters in alphalist:
       if(letters in inputletters):
           continue
       for words in update:
           if(letters in words):
               if(words in updateddic): 
                   updateddic.remove(words) 
   return updateddic  






#function for Scrabble,suffix and prefix
    
#selection of the words for alphabets
def scrabblefilter(input,updated):
    scrabble=[]
    inputlist=indexfind(input)
    for words in updated:
        templist=indexfind(words)
        flag=0
        check=len(words)
        for part in templist:
            if(part[1]>1):
                for inputs in inputlist:
                    if(part[0]==inputs[0]):
                        if(part[1]<=inputs[1]):
                             flag+=1
                        else:
                          continue
                    else:
                        continue
            if(part[0] in set(list(input))):
                flag +=1
        if(flag==check):
            scrabble.append(words)
    return scrabble         
        

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





#define the main according the user input
def main(arg):
    world=load()# creating one global reference for all functions 
    
    if(arg[0]=='--suffix'):# handling suffix input
         stringcheck(arg[1])
         result = create("Output\\suffixoutput.txt","w")
         result.write(arg[0]+"--")
         result.write(arg[1])
         result.write("\n")
         for word in suffix(world,arg[1]):
           result.write(word)
           result.write("\n")
           
    elif(arg[0]=="--prefix"):# handling prefix input
        stringcheck(arg[1])
        result =create("Output\\prefixoutput.txt","w") 
        result.write(arg[0]+"--")
        result.write(arg[1])
        result.write("\n")
        for word in prefix(world,arg[1]):
          result.write(word)
          result.write("\n")
           
    elif(arg[0].isalpha()): #handling scrabble input
        options=set(list(arg[0]))
        updated=filter(world,options)
        result =create("Output\\scrabble.txt","w")
        result.write("scrabble--")
        result.write(arg[0])
        result.write("\n")
        for word in scrabblefilter(arg[0],updated):
            result.write(word)
            result.write("\n")
    else:
        stringcheck("1")# to throw alphabet Error
 
       
                  
                             
                                                   
                    
#main   
if __name__ == "__main__":
   main(sys.argv[1:])