'''Write a function to implement binary search'''
def bsearch(li, n, start = 0):
  l=0
  r=len(li)-1
  mid=(l+r)//2
  if n>li[mid]:
    return bsearch(li[mid+1:],n,start+mid+1)
  elif n<li[mid]:
    return bsearch(li[:mid],n,start=start)
  else:
    return start+mid
bsearch([1,2,3,4,5,6,7,8,9],8)