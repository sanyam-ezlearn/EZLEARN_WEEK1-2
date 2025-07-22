'''Write a function which takes a list of numbers and returns a list of tuples with two values in it with the first value as a number from the list and the second value as the number of
 times the first value is repeated consecutively in the input list.'''
def consecutive_sim_frequency(tl):
  res=[]
  idx=0
  while idx<len(tl):
    st=idx
    val=tl[idx]
    while idx<len(tl) and tl[idx]==val:
      idx+=1
    count=idx-st
    res.append((val,count))
  return res
consecutive_sim_frequency([2, 2, 3, 3, 3, 3, 4,2])