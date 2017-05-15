
import unittest
from scrabble import suffix,prefix,filter,indexfind,load,prefilter,stringcheck,scrabblefilter
class scrabbletest(unittest.TestCase):
    
    #to Test Prefix
    def test1(self):
        expected=["paler"]
        dic=load()
        actual=prefix(dic,"paler")
        assert(actual==expected)
        
       #to Test suffix 
    def test2(self):
        expected=["abuzz"]
        dic=load()
        actualt=suffix(dic,"z")
        actual=[]
        actual.append(actualt[0])
        assert(actual==expected)
        
 #to Test Filter which used for finding scrabble
    def test3(self): 
        dic=load()
        expected=['abaft', 'abandon', 'abandoned']
        actual1=filter(dic,"abftndoe")
        actual=actual1[:3]
        assert(actual==expected)
        
         #to Test indexfind which is used in finding scrabble result
    def test4(self): 
        expected=[['a',2]]
        actual=indexfind("aa")
        assert(actual==expected)
        
         #to Test prefilter which is used by Filter
    def test5(self): 
        dic=load()
        expected=False
        check="base"
        actualt=prefilter(dic,"a")
        actual=check in actualt
        assert(actual==expected)
        
         #to Test stringcheck , Check the Input
    def test6(self): 
        expected=1
        check="base"
        stringcheck(check)
        actual=1
        assert(actual==expected)
        
         #to Test Scrabble
    def test7(self): 
        dic=load()
        options=set(list("gs"))
        expected=["gs"]
        update=filter(dic,options)
        actual=scrabblefilter("gs",update)
        assert(actual==expected)
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
    