from interpreter import Interpreter
import unittest

class TestInterpreter(unittest.TestCase):

    def test_empty(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram(''), '', 'Should be nothing')

    def test_string(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('"Hello World!"'), 'Hello World!', 'Should be Hello World!')

    def test_concat_numbers(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('123@'), '123', '123')
        self.assertEqual(interpreter.runProgram('123@1+'), '124', '124')

    def test_decimals(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('3.45 1+'), '4.45', '4.45')

    def test_negation(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('3~'), '-3', 'Should be -3')

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
        self.assertEqual(interpreter.runProgram('0.6('), '1', 'Should be 1')

    def test_floor_function(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('0.6)'), '0', 'Should be 0')

    def test_absolute_value(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('3~a'), '3', 'Should be 3')

    def test_factorial(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('5!'), '120', 'Should be 120')

    def test_logarithm_base_10(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('2l'), '0.3010299956639812', 'Should be 0.3010299956639812')

    def test_pi(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('p'), '3.141592653589793', 'Should be 3.141592653589793')

    def test_e(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('e'), '2.718281828459045', 'Should be 2.718281828459045')

    def test_prime(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('21@v'), 'False', 'Should be False')
        self.assertEqual(interpreter.runProgram('1v'), 'False', 'Should be False')
        self.assertEqual(interpreter.runProgram('0v'), 'False', 'Should be False')
        self.assertEqual(interpreter.runProgram('1~v'), 'False', 'Should be False')
        self.assertEqual(interpreter.runProgram('2v'), 'True', 'Should be True')
        self.assertEqual(interpreter.runProgram('29@v'), 'True', 'Should be True')

    def test_num_permutations(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('53P'), '60', 'Should be 60')

    def test_num_combinations(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('53C'), '10', 'Should be 10')

    def test_gcd(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('60@48@G'), '12', 'Should be 12')

    def test_pop_stack(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('"a""b"y'), 'a', 'Should be a')

    def test_swap_top_stack(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('"a""b";'), 'ba', 'Should be ba')

    def test_duplicate_top_stack(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('"a"_'), 'aa', 'Should be aa')

    def test_true(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('T'), 'True', 'Should be True')

    def test_false(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('F'), 'False', 'Should be False')

    def test_boolean_or(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('TT|'), 'True', 'Should be True')
        self.assertEqual(interpreter.runProgram('TF|'), 'True', 'Should be True')
        self.assertEqual(interpreter.runProgram('FT|'), 'True', 'Should be True')
        self.assertEqual(interpreter.runProgram('FF|'), 'False', 'Should be False')

    def test_boolean_and(self):
        interpreter = Interpreter()
        self.assertEqual(interpreter.runProgram('TT&'), 'True', 'Should be True')
        self.assertEqual(interpreter.runProgram('TF&'), 'False', 'Should be False')
        self.assertEqual(interpreter.runProgram('FT&'), 'False', 'Should be False')
        self.assertEqual(interpreter.runProgram('FF&'), 'False', 'Should be False')

if __name__ == '__main__':
    unittest.main()
