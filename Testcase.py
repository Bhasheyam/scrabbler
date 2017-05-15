
import unittest
from oracle import suffix,prefix,filter,load
class scarblertest(unittest.TestCase):
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
        actual1=filter("abftndoe")
        actual=actual1[:3]
        assert(actual==expected)
def main():
    unittest.main()

if __name__ == "__main__":
    main()
    