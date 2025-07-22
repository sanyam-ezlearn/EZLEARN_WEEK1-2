''' Write a function to get the
 index of the first element greater than K in a list.'''
def first_element(l,k):
  for i,n in enumerate(l):
    if n>k:
      return i
  return None
first_element([0.4, 0.5, 11.2, 8.4, 10.4],0.6)