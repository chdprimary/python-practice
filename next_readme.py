# MY PROBLEM SOLVING METHOD: I/OWP-STEO

# ======
# GENERAL PYTHON STUFF
# ======

# !!!
# FUNCTION SCOPE
# LEGB (local scope, enclosing local scopes, global scope, builtin scope)

# !!!
# *ARGS AND **KWARGS
# *args batches following non-keyword args into a tuple
# **kwargs turns keywords into kv's in a dict
# can use * operator to unpack a tuple/list/set (like spread syntax in JS)
# can use ** operator to unpack a map such as a dict

# !!!
# USEFUL BUILTINS
# TYPES: int(), float(), list(), bool(), chr(), dict(), set(), str(), tuple()
#! MISC: all(),any(),enumerate(),open(),zip(),reversed(),input(),round(),isinstance(),hash()
#! - `with open(<path>) as f:`
#! MATH: abs(), pow(), max(), min() 
# - non-builtin math functions: math.ceil(), math.floor(), math.sqrt() - (same as **(1/2))
# FUNCTIONAL (non-pythonic, don't use): filter(), map()

# !!!
# DUCK TYPING
# "Duck typing" is the pythonic way of checking type - basically try/except instead of 
# checking type. "Ask for forgiveness rather than permission".
#! Remember, it's try/except, not try/catch
#! Format is try/except(s)/else/finally

# !!!
# DEFAULT ARGS
# A mutable default argument in a function definition is MEMBER DATA of the function -
# functions are first class objects! - so the state is retained ACROSS function calls.

# !!!
# CONTAINERS
# Lists < Dicts < Sets (in terms of speed). Use a set or dict if you need lower time complx.
# from collections import Counter; Counter(<iter>) # => yields <dict> where val is num occurr.
# Set and dictionary comprehensions are a thing
# Elements of a set have to be immutable
# Keys of a dictionary have to be immutable
# Tuple elements can't be mutated 
# - but an entire tuple can be reassigned (bc just changing label name, see pass-by=sharing)
# Internally, a list is handled as an fixed-size array that grows when full. 
# - len and subscripting are O(1), copy is O(n) as is insert/del (have to shift elements)
# - sorting is O(nlogn), algorithm is timsort
# - https://wiki.python.org/moin/TimeComplexity

# !!!
# SORTING
# sorted() is a stable sort. This is useful when doing secondary,tertiary,etc sorts.
# sorted() also takes an optional comparison function of one arg - sorted(key=fn|lambda)

# !!!
# COMMENTS
# Multi-line comments are triple-quotes-delimited ("""), single-liners use a pound sign (#)

# !!!
# TRUTHINESS & FALSINESS
# None, False, 0, 0.0, '', and empty containers are all falsy; all other values are truthy
# But falsy doesn't necessarily mean False.
'' == {}    # => False
'' == False # => False
0 == False  # => True
1 == True   # => True
2 == True   # => False
# ^^^ as you can see, True/1 and False/0 are "value-equivalent" (but not object-equiv as with `is` keyword)

# PASS-BY-SHARING
# Python is neither "pass-by-value" or "pass-by-reference".
# It is a combination of the two, often called "pass-by-sharing" or "pass-by-object-reference"
# It is like pass by ref for mutations and pass by val for assignments.
# Javascript is also pass-by-sharing.

# LAMBDAS
lambda x: x > 0
lambda y: isinstance(y,int)

# METASYNTACTIC VAR NAMES
# 'li' for lists
# 'foo'/'bar' for functions
# 'a', 'b', 'x', 'y' for other variables
# 'res', 'ret' for return values

# LOOPING
# Use 'while' instead of 'for .. in' if modifying loop boundaries.
# Also, remember, range doesn't change! Ex: you can't del a value coming from a range object.

# PEP-8 STYLING
# vars should use underscores between words unless pre-established convention (consistency!)
# '_name' for internal use (these objects won't be imported by 'import')
# 'name_' to avoid keyword conflicts
# CamelCase for class names
# constants in ALL CAPS

# BITWISE OPERATIONS
# Can shift around with <<, >>, <<=, >>=
# | (OR), & (AND), ^ (XOR)
# bool(x&1) returns True for odd x ints and False for even x ints
# Ex: 5 & 1 is interpreted as: 0b101 & 0b001 => 1 (0b1)
# Ex: 7 ^ 2 is interpreted as: 0b111 ^ 0b010 => 5 (0b101)
# Python uses two's complement for negative numbers (bitops become more diff with neg nums)

# MISC
# In Python, everything is an object (this means everything can be assigned to vars or passed as fn arg)
# import cProfile and cProfile.run('<code>') are useful for timing.
# can return multiple values (implicit tuple - no parens needed)
# can use comma for multiple assignment anywhere you imght normally use a 'tmp' variable to switch 2 values



# ======
# STRINGS
# ======

# !!!
# .FORMAT()
# <str>.format() is very useful, curly braces can take names as well
'{}: {}'.format(0, 'hi')
'{0} be nimble, {0} be quick, {0} jump over the {1}'.format('Jack', 'candle stick')
'{idx}: {val}'.format(idx=0, val='hi')
'{:02d}'.format(3.14159) # => 3.14
# https://pyformat.info/ is very useful

# Remember strings are immutable - can't use subscript or 'del' operators
s = 'abc' 
# s[1] = 'd'
# TypeError 'str' object does not support assignment
# del s[1] 
# TypeError 'str' object does not support deletion

# lists are not strings (BUT both ARE iterable types)
'abc' == ['a','b','c']
# => False

# Strings are immutable but you can use +, *, += and *= on them
'a' * 2
# => 'aa'

# Since strings are immutable, they can be used as dictionary keys, since the hash won't change

# METHODS
# .upper(), .lower(), .title()
# .strip()
# .count()
# .index(<substr>), .find(<substr>)
# .split(<substr>), .join(<iter>)
# .replace(<old>,<new>), .translate(<map>[, delChars])


# ======
# DICTIONARIES
# ======

# Keys have to be immutable types - numerics or strings will work, but a list won't work

# When you iterate over a dictionary, you iterate over the keys by default, not the values
# - can specify .keys(), .values(), .items()

# Use <dict>.get(<key>) to avoid KeyError on an unexpected missing key
# Use <dict>.setdefault(<k>,<v>) to set a val only if key isn't already present



# ======
# GENERATORS / GENERATOR EXPRESSIONS
# ======

# Generator expressions are much like list comprehensions
x = [i for i in range(1000000)]
# ^^^ the entire list is created in memory all at once

y = (i for i in range(1000000))
# ^^^ this is a generator expression. you use the builtin function next()
# to gen next value on-the-fly, which can be more time & space efficient
next(y) # => 0
next(y) # => 1
next(y) # => 2
# ^^^ with generators, python keeps track of state on its own

