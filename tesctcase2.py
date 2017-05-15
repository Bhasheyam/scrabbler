import unittest
from scrabble import scrabblefilter,load
class scrabblertest(unittest.TestCase):
     def test5(self):
       dic=load()
       expected=['gs']
       actual=scrabblefilter(dic,"gs")
       assert(actual==expected)
def main():
    unittest.main()

if __name__ == "__main__":
    main()