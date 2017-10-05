places = ['desert', 'mountain', 'lake', 'river', 'san antonio']
print("Original order: " + str(places))

print("Temp sorted alpha: " + str(sorted(places)))
print("Still original order: " + str(places))

print("Temp reverse sorted alpha: " + str(sorted(places, reverse=True)))
print("Still original order: " + str(places))

places.reverse()
print("Reversed in order now: " + str(places))
places.reverse()
print("Back to original order: " + str(places))

places.sort()
print("Perm sorted alphabetically: " + str(places))
places.sort(reverse=True)
print("Perm reverse sorted alpha: " + str(places))