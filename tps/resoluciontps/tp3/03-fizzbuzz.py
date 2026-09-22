import unittest

def esFizz(numero: int) -> str:
    salida = ""
    if numero % 3 == 0 and numero % 5 == 0:
        salida = "FizzBuzz"
    elif numero % 3 == 0:
        salida = "Fizz"
    elif numero % 5 == 0:
        salida = "Buzz"
    return salida

class testFizz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(esFizz(15), "FizzBuzz")
        self.assertEqual(esFizz(3), "Fizz")
        self.assertEqual(esFizz(5), "Buzz")
        self.assertEqual(esFizz(7), "")

    
if __name__ == "__main__":
    unittest.main()