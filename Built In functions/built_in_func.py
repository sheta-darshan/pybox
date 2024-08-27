# Built-in Functions Examples with Explanations

# A
print("abs(-5):", abs(-5))  
# Output: 5
# abs() returns the absolute value of the given number.

print("all([True, True, False]):", all([True, True, False]))  
# Output: False
# all() returns True if all elements in the iterable are true. Otherwise, it returns False.

print("any([False, False, True]):", any([False, False, True]))  
# Output: True
# any() returns True if any element in the iterable is true. Otherwise, it returns False.

# B
print("bin(8):", bin(8))  
# Output: '0b1000'
# bin() converts an integer to a binary string prefixed with '0b'.

print("bool(0):", bool(0))  
# Output: False
# bool() converts a value to a Boolean value (False or True). 0 is False, non-zero values are True.

print("bool(1):", bool(1))  
# Output: True

# C
print("chr(65):", chr(65))  
# Output: 'A'
# chr() converts an ASCII (or Unicode) code point to a string character.

code = compile('a = 5\nb = 10\nprint(a + b)', '', 'exec')
exec(code)  
# Output: 15
# compile() compiles a source code into a code object, which can be executed using exec().

# D
print("divmod(10, 3):", divmod(10, 3))  
# Output: (3, 1)
# divmod() returns a tuple of the quotient and remainder of dividing the first number by the second.

# E
for index, value in enumerate(['a', 'b', 'c']):
    print("enumerate:", index, value)
# Output:
# 0 a
# 1 b
# 2 c
# enumerate() adds a counter to an iterable and returns it in the form of an enumerate object.

print("eval('5 + 10'):", eval('5 + 10'))  
# Output: 15
# eval() evaluates a string as a Python expression and returns the result.

# F
def is_even(n):
    return n % 2 == 0

print("filter(is_even, [1, 2, 3, 4]):", list(filter(is_even, [1, 2, 3, 4])))  
# Output: [2, 4]
# filter() filters elements of an iterable based on a function that returns True or False.

# G
class MyClass:
    attribute = 'Hello'

obj = MyClass()
print("getattr(obj, 'attribute'):", getattr(obj, 'attribute'))  
# Output: 'Hello'
# getattr() retrieves the value of an attribute from an object.

# H
print("hex(255):", hex(255))  
# Output: '0xff'
# hex() converts an integer to a hexadecimal string prefixed with '0x'.

# I
# Uncomment the next lines to test input
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

print("int('10'):", int('10'))  
# Output: 10
# int() converts a string or other type to an integer.

print("int('A', 16):", int('A', 16))  
# Output: 10
# int() with a base converts a string in that base to an integer.

# L
print("len([1, 2, 3]):", len([1, 2, 3]))  
# Output: 3
# len() returns the number of items in an iterable.

# M
print("max([1, 2, 3]):", max([1, 2, 3]))  
# Output: 3
# max() returns the largest item from an iterable or among two or more arguments.

print("min([1, 2, 3]):", min([1, 2, 3]))  
# Output: 1
# min() returns the smallest item from an iterable or among two or more arguments.

# N
it = iter([1, 2, 3])
print("next(it):", next(it))  
# Output: 1
# next() retrieves the next item from an iterator.

print("next(it):", next(it))  
# Output: 2

# O
print("ord('A'):", ord('A'))  
# Output: 65
# ord() converts a single character to its ASCII (or Unicode) code point.

# P
print("pow(2, 3):", pow(2, 3))  
# Output: 8
# pow() returns the result of raising the first number to the power of the second number.

print("pow(2, 3, 5):", pow(2, 3, 5))  
# Output: 3
# pow() with a third argument returns the result modulo the third number.

# R
print("list(range(3)):", list(range(3)))  
# Output: [0, 1, 2]
# range() returns an iterable sequence of numbers.

print("list(reversed([1, 2, 3])):", list(reversed([1, 2, 3])))  
# Output: [3, 2, 1]
# reversed() returns an iterator that accesses the given sequence in reverse order.

# S
print("sorted([3, 1, 2]):", sorted([3, 1, 2]))  
# Output: [1, 2, 3]
# sorted() returns a new list containing all items from the iterable in ascending order.

# T
print("type(123):", type(123))  
# Output: <class 'int'>
# type() returns the type of an object.

# Z
print("list(zip([1, 2, 3], ['a', 'b', 'c'])):", list(zip([1, 2, 3], ['a', 'b', 'c'])))  
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# zip() aggregates elements from two or more iterables into tuples.

# Underscore
math = __import__('math')
print("math.sqrt(4):", math.sqrt(4))  
# Output: 2.0
# __import__() is a built-in function used to import a module dynamically.
