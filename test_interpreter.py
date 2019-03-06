from interpreter import Interpreter
import unittest

class TestInterpreter(unittest.TestCase):

    def test_empty(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram(''), '', 'Should be nothing')

    def test_string(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('"Hello World!"'), 'Hello World!', 'Should be Hello World!')

    def test_addition(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('35+'), '8', 'Should be 8')

    def test_subtraction(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('35-'), '-2', 'Should be -2')

    def test_multiplication(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('35*'), '15', 'Should be 15')

    def test_division(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('35/'), '0.6', 'Should be 0.6')

    def test_modulus(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('53%'), '2', 'Should be 2')

    def test_power(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('53^'), '125', 'Should be 125')

    def test_square(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('5#'), '25', 'Should be 25')

    def test_square_root(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('4\\'), '2', 'Should be 2')

    def test_greater_than(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('53>'), 'True', 'Should be True')

    def test_less_than(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('53<'), 'False', 'Should be False')

    def test_equals(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('55='), 'True', 'Should be True')

    def test_ceiling_function(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('35/('), '1', 'Should be 1')

    def test_floor_function(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('35/)'), '0', 'Should be 0')

    def test_absolute_value(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('12-|'), '1', 'Should be 1')

    def test_factorial(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('5!'), '120', 'Should be 120')

    def test_logarithm_base_10(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('2l'), '0.3010299956639812', 'Should be 0.3010299956639812')

    def test_prime(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('8v'), 'False', 'Should be False')
        self.assertEqual(interpreter.runProgram('1v'), 'False', 'Should be False')
        self.assertEqual(interpreter.runProgram('0v'), 'False', 'Should be False')
        self.assertEqual(interpreter.runProgram('12-v'), 'False', 'Should be False')
        self.assertEqual(interpreter.runProgram('2v'), 'True', 'Should be True')
        self.assertEqual(interpreter.runProgram('7v'), 'True', 'Should be True')

if __name__ == '__main__':
    unittest.main()