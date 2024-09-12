"""
Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and 
you may not use the same element twice.

You can return the answer in any order.
"""

def two_sum_hash(nums, target):
    """
    Time: O(n), linear time b/c loops through the list once.
    Space: O(n), due to the space needed for the dictionary.
    """
    result = {}
    for idx,val in enumerate(nums):
        diff = target - val
        if diff in result:
            return [result[diff], idx] # returns idx
            #return diff, val # returns val
        result[val] = idx
    return [-1, -1]

def two_sum_best(nums, target):
    """
    Time: O(n), list is traversed once by the two pointers.
    Space: O(1), constant space, no additional memory used.
    """
    start = 0
    end = len(nums) - 1
    while start<=end:
        if nums[start] + nums[end] == target:
            return [start, end]
            #return [nums[start], nums[end]]
        elif nums[start] + nums[end] < target:
            start += 1
        else:
            end -= 1
    return [-1,-1]

if __name__=='__main__':

    nums = [2,7,11,15]
    target = 9
    result = two_sum_hash(nums, target) # [0, 1]
    print(result)

    result = two_sum_best(nums, target) # [0, 1]
    print(result)
