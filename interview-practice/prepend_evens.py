# https://repl.it/repls/WaryTameMicrocode

# In: li
# Out: li, with evens in front, in-place
# W
# P
# -
# S
# T
# E
# O

#O(n) time
#O(n) space

# li = [774657202] => [462027757]
# evens = [46202]
# odds = [7757]

def _is_odd(num):
  return bool(num & 1)

def prepend_evens(li):
  print(li)
  evens = []
  odds = []
  for num in li:
    if _is_odd(num):
      odds.append(num)
    else:
      evens.append(num)
  li[:] = evens + odds
  print(li)
  
ints = [7,7,4,6,5,7,2,0,2]
prepend_evens(ints)

ints = [1,3,5,7,9,2,4,6,8,0]
prepend_evens(ints)

ints = [0]
prepend_evens(ints)

ints = list(range(-5,5))
prepend_evens(ints)
