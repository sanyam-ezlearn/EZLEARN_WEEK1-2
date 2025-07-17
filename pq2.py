''' Problem Statement 02 
You are given an array A (i-based indexing) of size of N. You can remove 
up to N-1 elements from this array. 
You have to remove the elements in jzj a way such that Al - I for all 
1 <=i<=size_of_newArray.  
What are the minimum number of elements you need to remove order to 
satisfy the given property? If it is not possible return -1.'''
def min_removals_to_match_index(N, A):
    expected = 1
    for num in A:
        if num == expected:
            expected += 1
    matched = expected - 1
    return -1 if matched == 0 else N - matched

# Input
N = int(input())
A = [int(input()) for _ in range(N)]

# Output
print(min_removals_to_match_index(N, A))


