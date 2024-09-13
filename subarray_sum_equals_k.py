def subarray_sum(nums, k):
    """
    Time: O(n), where n is the length of the array.
    Space: O(n), where n is the size of the hashmap that stores the prefix sums.
    """

    # Hashmap to store the prefix sum and its frequency
    prefix_sum_count = {0: 1} # cumulative sum at each index
    current_sum = 0
    count = 0
    
    for num in nums:
        # Update the running sum (prefix sum)
        current_sum += num
        
        # Check if there is a subarray sum equals to k
        # by checking if current_sum - k exists in prefix_sum_count
        if current_sum - k in prefix_sum_count:
            count += prefix_sum_count[current_sum - k]
        
        # Update the prefix_sum_count hashmap
        if current_sum in prefix_sum_count:
            prefix_sum_count[current_sum] += 1
        else:
            prefix_sum_count[current_sum] = 1
        #print(prefix_sum_count)
    
    return count

if __name__=='__main__':

    nums = [1,1,1]
    k = 2
    result = subarray_sum(nums, k) # Output: 2
    print(result)

    nums = [1,2,3]
    k = 3 
    result = subarray_sum(nums, k) # Output: 2
    print(result)

    nums = [2,2,1,3,4]
    k = 4
    result = subarray_sum(nums, k) # Output: 3
    print(result)