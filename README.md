strings
	
	<str>.upper()
	<str>.lower()
	<str>.title()
	<str>.strip()
	<str>.count(<char>) - returns number of occurrences of character
	string slicing <str>[start:end]
	str() - type conversion to string type
	<str>.index(<char>) - will throw ValueError if <char> not found
	<str>.find(<char>) - will return -1 if <char> not found
	<str>.join(<list>) - str can also be a char, or the empty string, of course, e.g. ''.join(listOfChars)

builtins

	abs()
	// - integer division
	pow()
	len()
	print()
	range(x,y,[skip_amount]) #includes x but not y

'random' package

	random.shuffle(<list>)
	random.sample(<list>, <num_of_samples>)
	random.choice(<list>) // chooses one item randomly
	random.randint(<min>,<max_inclusive>)

'math' package

	math.floor()

OOP

	class Thing(object)
		def __init__(self, name="default_name"):
			self.name = name
			self.quantity = 5
			pass
	inheritance
	super().__init__(...)

conditionals

	'and' takes place of &&
	'or' takes place of ||
	<x> in <list>
	<x> not in <list>
	if-elif-else

loops

	for item in items:
	for idx, val in enumerate(<list>):

lists

	* enclosed in []
	access last element with index -1
	<list>.append(<item>)
	<list>.insert(<idx>,<item>)
	<list>.index(<item>)
	del <list>[<idx>]
	<list>.remove(<item>)
	<list>.pop(<idx>)
	<list>.sort([reverse=True]) #sorts list permanently
	sorted(<list>,[reverse=True]) #returns temporarily sorted list
	<list>.reverse() #reverses the orig list order
	len(<list>)
	list() - type conversion to list type
	min(<list>)
	max(<list>)
	sum(<list>)
	list comprehensions - lc = [val**2 for val in vals]
	<list>[<start>:<end>] #slices a list
	<list>[:] #copies a list
	<list1> = <list2> #does not copy list2, actually makes list1 point at list2 (ie reference instead of value)

tuples #tuples are lists whose elements are immutable

	* tuples use () instead of []
	* but you can redefine the whole tuple at once

dictionaries

	del <dict>['<key>'] 		# deletes a kv pair in a dict
	for k,v in <dict>.items() 	# returns all dict's kv pairs
	for k in <dict> 			# returns all dict's keys
	for k in <dict>.keys()		# returns all dict's keys
	for k in <dict>.values()	# returns all dict's values

user input

	input()

functions

	keyword 'def'
	positional arguments func(val1,val2)
	keyword arguments func(arg2=val1,arg1=val2)
	default values z3 put the default value in the function signature
	optional arguments should be set equal to a False value and placed last in the list of parameters
	lists are passed by reference, but you can pass a copy with <list>[:]
	pass an arbitrary numbers of arguments with *<param> # packs the arguments into a tuple
	you can pass keyword or positional arguments to an arbitrary argument

importing packages

	import functions from a pizza.py file by using 'import pizza' and then writing pizza.<func>()
	from pizza import func1 as alias1
	import pizza as alias1
	from pizza import *
	
BUILD A PROJECT
USE ANKI