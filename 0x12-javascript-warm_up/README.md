# Javascript - Warm up

This marked my inaugural JavaScript project at ALX. The tasks primarily encompassed crafting introductory-level JavaScript scripts using Node.js.

Tests :heavy_check_mark:
tests: Directory containing test files provided by ALX.
Function Prototypes :floppy_disk:
Function prototypes for this project are outlined below:

File	Prototype
13-add.js	exports.add = (a, b)
101-call_me_moby.js	function (x, theFunction)
102-add_me_maybe.js	function (number, theFunction)
Tasks :page_with_curl:
0. First constant, first print

0-javascript_is_amazing.js: A JavaScript script that establishes a constant variable myVar with the value 'Javascript is amazing'.
Usage: ./0-javascript_is_amazing.js
1. 3 languages

1-multi_languages.js: A JavaScript script printing three lines.
Usage: ./1-multi_languages.js
Line 1: 'C is fun'.
Line 2: 'Python is cool'.
Line 3: 'Javascript is amazing'.
2. Arguments

2-arguments.js: A JavaScript script printing a message based on the number of arguments provided.
Usage: ./2-arguments.js <arg 1> <arg 2> ...
If no arguments are supplied, prints 'No argument'.
If one argument is given, prints 'Argument found'.
Otherwise, prints 'Arguments found'.
3. Value of my argument

3-value_argument.js: A JavaScript script printing the first argument passed to it.
Usage: ./3-value_argument.js <arg>
If no argument is provided, prints 'No argument'.
4. Create a sentence

4-concat.js: A JavaScript script printing two arguments in the format <arg 1> is <arg 2>.
Usage: ./4-concat.js <arg1> <arg2>
5. An Integer

5-to_integer.js: A JavaScript script printing My number: <first argument converted to integer> if the first argument can be converted to an integer.
Usage: ./5-to_integer.js
If the argument cannot be converted to an integer, prints 'Not a number'.
6. Loop to languages

6-multi_languages_loop.js: A JavaScript script printing three lines using an array and a loop.
Usage: ./6-multi_languages_loop.js
First line: 'C is fun'.
Second line: 'Python is cool'.
Third line: 'Javascript is awesome'.
7. I love C

7-multi_c.js: A JavaScript script printing 'C is fun' x times.
Usage: ./7-multi_c.js <x>
If the first argument cannot be converted to a number, prints 'Missing number of occurrences'.
8. Square

8-square.js: A JavaScript script printing a square.
Usage: ./8-square.js <size>
If the first argument cannot be converted to a number, prints 'Missing size'.
Utilizes the X character to depict the square.
9. Add

9-add.js: A JavaScript script printing the addition of two numbers passed as arguments.
Usage: ./9-add.js <number 1> <number 2>
Prototype: function add(a, b)
10. Factorial

10-factorial.js: A JavaScript script computing and printing a factorial.
Usage: ./10-factorial.js <number to compute factorial of>
11. Second biggest!

11-second_biggest.js: A JavaScript script identifying the second largest number in the provided arguments.
Usage: ./11-second_biggest.js <arg 1> <arg 2> ...
If no arguments are given or the number of arguments is 1, prints 0.
12. Object

12-object.js: Modification of a script to replace the value 12 with 89.
javascript
Copy code
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);
13. Add file

13-add.js: A JavaScript function add returning the addition of two numbers.
14. Const or not const

100-let_me_const.js: A JavaScript script altering the value of myVar in the following file to 333.
javascript
Copy code
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
15. Call me Moby

101-call_me_moby.js: A JavaScript function executing a given function x times.
16. Add me maybe

102-add_me_maybe.js: A JavaScript function incrementing a given number and invoking a specified function.
17. Increment object

103-object_fct.js: Enhancement of a JavaScript script by introducing a new function incr that increments the value number.
javascript
Copy code
#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);




Message ChatGPT…

ChatGPT can make mistakes.