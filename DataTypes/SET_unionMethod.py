# 2. Set Union = a_set.union()
# Syntax: a_set.union(an_iter)
# Example:
print ("union",set([1, 2, 3, 4, 5]).union(set([5, 6, 7])))
#Output : set([1, 2, 3, 4, 5, 6, 7])
'''Returns the union of set a_set and the set of 
elements in iterable an_iter.'''

# ------------------------------------- #
# 2. Set Intersection = a_set.intersection()
# Syntax: a_set.intersection(an_iter)
# Example:
print("intersection",set([1, 2, 3, 4, 5]).intersection(set([5, 6, 7])))
#Output : set([5])

'''Returns the intersection of set a_set and the set of elements
in iterable an_iter.'''
# ------------------------------------- #
# 3. Set Difference = a_set.difference()
# Syntax: a_set.difference(an_iter)
# Example:

print ("difference",set([1, 2, 3, 4, 5]).difference(set([5, 6, 7])))
#Output : set([1, 2, 3, 4])

'''Returns a set with all elements from set a_set 
that are not in iterable an_iter.'''
# ------------------------------------- #
# 4. Set Symmetric Difference 	= a_set.symmetric_difference()
# Syntax: a_set.symmetric_difference(anInter)
# Example: 

print("symmetric_difference",set([1,2,3,4,5]).symmetric_difference(set([5,6,7])))
#Output : set([1, 2, 3, 4, 6, 7])

'''Returns a set with all elements that are in exactly
one of set a_set and iterable an_iter.'''
# ------------------------------------- #
# 5. Set Union with Mutation  =	a_set.update()
# Syntax: a_set.update(an_iter)
# Example:
s = set([1, 2, 3, 4, 5])
s.update(set([5, 6, 7]))
print("update",s)
#Output : set([1, 2, 3, 4, 5, 6, 7])
'''Mutates a_set to be the union of set a_set and
the set of elements in iterable an_iter. Returns None.'''
# ------------------------------------- #
# 6.Set Intersection with Mutation 	= a_set.intersection_update()
# Syntax: a_set.intersection_update(an_iter)
# Example:
s = set([1, 2, 3, 4,5])
s.intersection_update(set([5, 6, 7]))
print("intersection_update",s)
#Output : set([5])

'''Mutates a_set to be the intersection of set a_set
and the set of elements in iterable an_iter. Returns None.'''
# ------------------------------------- #
# 7. Set Difference with Mutation = a_set.difference_update()
# Syntax: a_set.difference_update(an_iter)
# Example:
s = set([1, 2, 3, 4, 5])
s.difference_update(set([5, 6, 7]))
print (s)

#Output : set([1, 2, 3, 4])

'''Mutates a_set to be the set difference of set a_set and the 
set of elements in iterable an_iter. Returns None.'''
# ------------------------------------- #
# 8. Set Symmetric Difference with Mutation
# =a_set.symmetric_difference_update()
# Syntax: a_set.symmetric_difference_update(an_iter)
# Example:
s = set([1, 2, 3, 4, 5])
s.symmetric_difference_update(set([5, 6, 7]))
print (s)

#Output : set([1, 2, 3, 4, 6, 7])

'''Mutates a_set to be a set with all elements that are in exactly 
one of set a_set and iterable an_iter. Returns None.'''
# ------------------------------------- #
# 9. Add Element into Set  = a_set.add()
# Syntax: a_set.add(x)

# Example:
s = set([1, 2, 3, 4, 5])
s.add(5)
print (s)
# Output : set([1, 2, 3, 4, 5])

s.add(6)
print (s)
#Output :  set([1, 2, 3, 4, 5, 6])

'''Adds element x to the set a_set. Returns None.'''
# ------------------------------------- #
# 10. Remove Specified Element from Set = a_set.remove(), a_set.discard()
# Syntax: a_set.remove(x) a_set.discard(x)
# Example:
s = set([1, 2, 3, 4, 5])
s.remove(5)
print (s)

s.discard(7)
print (s)

s.discard(3)
print (s)

# Output: 
set([1, 2, 3, 4])
set([1, 2, 3, 4])
set([1, 2, 4])
'''
Removes element x from set a_set. 
If element x is not in a_set, a_set.remove raises an error, 
while a_set.discard does not. 
Returns None.
'''
# ------------------------------------- #

# ------------------------------------- #
