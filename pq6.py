'''Write a function which extracts 
pairs of the same integers from a list'''
def same_int(l):
  v=set()
  res=[]
  for t in test_list:
    if t in v:
      res.append((t,t))
      v.remove(t)
    else:
      v.add(t)
  return res
same_int([4, 4, 4, 4, 4, 4, 6, 7, 4, 2, 6, 2, 8, 8, 8])