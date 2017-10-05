strings
	
	<str>.upper()
	<str>.lower()
	<str>.title()
	<str>.strip()
	<str>.count(<char>) - returns number of occurrences of character
	string slicing <str>[start:end]
	str() - type conversion to string type

builtins

	abs()
	// - integer division
	pow()
	len()
	print()
	range(x,y,[skip_amount]) #includes x but not y

math package

	math.floor()

OOP

	class Thing(object)
		def __init__(self, name="default_name"):
			self.name = name
			self.quantity = 5
			pass

conditionals

	'and' takes place of &&
	'or' takes place of ||
	<x> in <list>
	<x> not in <list>
	if-elif-else

loops

	for item in items:

lists

	* enclosed in []
	access last element with index -1
	<list>.append(<item>)
	<list>.insert(<idx>,<item>)
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
BUILD A PROJECT
USE ANKI