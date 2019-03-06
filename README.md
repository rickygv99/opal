# What is Opal?
Opal is a stack-based programming language for code golf.

# Syntax
All the program memory is contained in a single stack called the *program stack*. Programs are read by the interpreter one character at a time. Numbers consisting of a single digit are appended to the program stack as is. If you want to add a multidigit number to the program stack, you must end the number with the character *@*. Anything enclosed in double quotes *""* is treated as a string. Any values left in the program stack at the end of the program will be concatenated together and outputted as a single string.

The character *q* is a special character which takes input from the user and stores it in the program stack. Operators which manipulate the values in the program stack are defined below.

## Operators

| Operation | Operator | Example program | Example output |
| ----------- | ----------- | ----------- | ----------- |
| Concatenation | @ | 123@1+ | 124 |
| Negation | ~ | 3~ | -3 |
| Addition | + | 34+ | 7 |
| Subtraction | - | 23- | -1 |
| Multiplication | * | 23* | 6 |
| Division | / | 35/ | 0.6 |
| Modulus | % | 53% | 2 |
| Power | ^ | 23^ | 8 |
| Square | # | 2# | 4 |
| Square root | \ | 4\ | 2 |
| Root | r | 83r | 2 |
| Is greater than? | > | 53> | True |
| Is less than? | < | 53< | False |
| Is equal? | = | 44= | True |
| Ceiling function | ( | 0.6( | 1 |
| Floor function | ) | 0.6) | 0 |
| Absolute value | a | 3~a | 3 |
| Factorial | ! | 5! | 120 |
| Logarithm base-10 | l | 2l | 0.3010299956639812 |
| Natural logarithm | n | 2n | 0.69314718056 |
| Logarithm | b | 82b | 3 |
| Pi | p | p | 3.141592653589793 |
| e | e | e | 2.71828182846 |
| Generate random float in [0, 1) | R | R | 0.6745571862859855 |
| Is prime? | v | 7v | True |
| Euclidean distance | d | 0043d | 5 |
| TRUE | T | T | True |
| FALSE | F | F | False |
| Boolean OR | &#124; | TF&#124; | True |
| Boolean AND | & | TF& | False |

## Example programs
### hello_world
Program: `"Hello World!"`

> Prints "Hello World!"

Output:
`Hello World!`

### sum
Program: `12+`

> Computes sum of 1 and 2

Output:
`3`

### square_root
Program: `9\`

> Computes square root of 9

Output:
`3`

### distance
Program: `0043d`

> Computes Euclidean distance between points (0, 0) and (4, 3)

Output:
`5`

### convert_to_fahrenheit
Program: `q1.8*32@+`

> Takes input from the user representing temperature in degrees Celsius. Converts to temperature in degrees Fahrenheit.

Example input:
`37.5`

Example output:
`99.5`

### random
Program: `R10@*)`

> Generates random integer in [0, 9]

Example output:
`6`
