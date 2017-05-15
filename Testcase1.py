
import unittest
from scrabble import suffix,prefix,filter,indexfind,load
class scrabbletest(unittest.TestCase):
    def test1(self):
        expected=["paler"]
        dic=load()
        actual=prefix(dic,"paler")
        assert(actual==expected)
        
    def test2(self):
        expected=["abuzz"]
        dic=load()
        actualt=suffix(dic,"z")
        actual=[]
        actual.append(actualt[0])
        assert(actual==expected)

    def test4(self): 
        dic=load()
        expected=['abaft', 'abandon', 'abandoned']
        actual1=filter(dic,"abftndoe")
        actual=actual1[:3]
        assert(actual==expected)
    def test5(self): 
        expected=[['a','2']]
        actual=indexfind("aa")
        print(actual)
        print(expected)
        print(actual==expected)
        assert(actual==expected)
   
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
    