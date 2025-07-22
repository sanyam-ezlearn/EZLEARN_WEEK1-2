''' Write a function which extracts the index range of 
consecutive similar elements from a list.'''
def consecutive_sim(l):
  idx=0
  res=[]

  while idx<len(l):
    start = idx
    val = l[idx]
    while idx<len(l) and l[idx]==val:
      idx+=1
    end=idx-1
    res.append((val,start,end))
  return res

consecutive_sim([2, 3, 3, 3, 8, 8, 6, 7, 7])