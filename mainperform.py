import string
import os
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
    
    
    
def filter(inputletters):
   dic=load()#to run all the files
   updateddic=load()# optimize the dictionary according to the input
  
   alphabets="abcdefghijklmnopqrstuvwxyz"
   alphalist=list(alphabets)
   for letters in alphalist:
       if(letters in inputletters):
           continue
       for words in dic:
           if(letters in words):
               if(words in updateddic): 
                   updateddic.remove(words) 
   print(len(updateddic))
   return updateddic  
print(filter("abftndoet"))