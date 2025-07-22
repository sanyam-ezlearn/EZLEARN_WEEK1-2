'''Majority Element'''
def majorityElement(nums):
    count = 0
    major_element = 0
    for i in nums:
        if count == 0:
            major_element = i
        if major_element == i:
            count = count + 1
        else:
            count = count - 1
    return major_element

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
        