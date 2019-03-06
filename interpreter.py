import sys
import math

class Interpreter:
    def runProgram(self, program):
        stack = []
        readingList = False
        currentList = []
        for character in program:
            if character is '\"':
                if readingList:
                    stack.append(currentList)
                    currentList = []
                readingList = not readingList
            elif readingList:
                currentList.append(character)
            elif character.isspace():
                pass
            elif character.isdigit():
                stack.append(int(character))
            elif character is '+': # Addition
                values = self.getValues(stack, 2)
                stack.append(values[0] + values[1])
            elif character is '-': # Subtraction
                values = self.getValues(stack, 2)
                stack.append(values[0] - values[1])
            elif character is '*': # Multiplication
                values = self.getValues(stack, 2)
                stack.append(values[0] * values[1])
            elif character is '/': # Division
                values = self.getValues(stack, 2)
                stack.append(values[0] / values[1])
            elif character is '%': # Modulus
                values = self.getValues(stack, 2)
                stack.append(values[0] % values[1])
            elif character is '^': # Power
                values = self.getValues(stack, 2)
                stack.append(values[0] ** values[1])
            elif character is '#': # Square
                values = self.getValues(stack, 1)
                stack.append(values[0] ** 2)
            elif character is '\\': # Square root
                values = self.getValues(stack, 1)
                stack.append(math.sqrt(values[0]))
            elif character is '>': # Greater than
                values = self.getValues(stack, 2)
                stack.append(values[0] > values[1])
            elif character is '<': # Less than
                values = self.getValues(stack, 2)
                stack.append(values[0] < values[1])
            elif character is '=': # Equals
                values = self.getValues(stack, 2)
                stack.append(values[0] == values[1])
            elif character is '(': # Ceiling funciton
                values = self.getValues(stack, 1)
                stack.append(math.ceil(values[0]))
            elif character is ')': # Floor function
                values = self.getValues(stack, 1)
                stack.append(math.floor(values[0]))
            elif character is '|': # Absolute value
                values = self.getValues(stack, 1)
                stack.append(math.fabs(values[0]))
            elif character is '!': # Factorial
                values = self.getValues(stack, 1)
                stack.append(math.factorial(values[0]))
            elif character is 'l': # Logarithm base-10
                values = self.getValues(stack, 1)
                stack.append(math.log10(values[0]))
            elif character is 'n': # Natural logarithm
                values = self.getValues(stack, 1)
                stack.append(math.log(values[0]))
            elif character is 'b': # Logarithm
                values = self.getValues(stack, 2)
                stack.append(math.log(values[0], values[1]))
            elif character is 'r': # Root
                values = self.getValues(stack, 2)
                stack.append(math.pow(values[0], 1.0/values[1]))
            elif character is 'p': # Pushes pi onto stack
                stack.append(math.pi)
            elif character is 'e': # Pushes e onto stack
                stack.append(math.e)
            elif character is 'v': # Checks if number is prime
                values = self.getValues(stack, 1)
                if values[0] < 2:
                    stack.append(False)
                elif not float(values[0]).is_integer():
                    stack.append(False)
                else:
                    isPrime = True
                    for i in range(2, int(int(values[0]) / 2) + 1):
                        if int(values[0]) % i == 0:
                            isPrime = False
                            break
                    stack.append(isPrime)
            elif character is 'd': # Calculates Euclidean distance between two points
                values = self.getValues(stack, 4)
                stack.append(math.sqrt((values[0] - values[1]) ** 2 + (values[2] - values[3]) ** 2))
            elif character is 'P': # Calculates number of permutations
                values = self.getValues(stack, 2)
                stack.append(math.factorial(values[0]) / math.factorial(values[0] - values[1]))
            elif character is 'C': # Calculates number of combinations
                values = self.getValues(stack, 2)
                stack.append(math.factorial(values[0]) / (math.factorial(values[1]) * math.factorial(values[0] - values[1])))
            elif character is 'y': # Pops last element of stack
                self.getValues(stack, 1)
            elif character is ';': # Swaps top two elements of stack
                values = self.getValues(stack, 2)
                stack.append(values[1])
                stack.append(values[0])
            elif character is '_': # Duplicates top element of stack
                values = self.getValues(stack, 1)
                stack.append(values[0])
                stack.append(values[0])
            else:
                self.throwError("Invalid character: " + character)
        output = ''
        for i in stack:
            if type(i) is list:
                for j in i:
                    output += str(j)
            else:
                output += str(self.trimTrailingZeroes(i))
        return output

    def getValues(self, stack, num):
        values = []
        for i in range(num):
            if len(stack) == 0:
                self.throwError("Attempted to pop value from empty stack")
            values.insert(0, stack.pop())
        return values

    def throwError(self, message):
        print("ERROR: " + message)
        sys.exit(0)

    def trimTrailingZeroes(self, num):
        try:
            if num is True or num is False:
                return num
            if float(num).is_integer():
                return int(num)
            return num
        except ValueError:
            return num

def main():
    if len(sys.argv) is not 2:
        sys.exit()

    program = ''
    f = open(sys.argv[1], 'r')
    program = f.read()
    f.close()

    output = Interpreter().runProgram(program)
    print(output)

if __name__ == '__main__':
    main()
