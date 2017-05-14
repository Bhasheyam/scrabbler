
import unittest
from test import suma
class LearningCase(unittest.TestCase):
    def test_starting_out(self):
        self.assertEqual(suma(1), 3)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
    