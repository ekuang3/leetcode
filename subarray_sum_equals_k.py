def total_subarrays(nums, k):
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

def get_subarrays(nums, k):
    """
    Returns all subarrays whose sum equals k.

    Time: O(n), where n is the length of the array.
    Space: O(n), where n is the size of the hashmap that stores the prefix sums.
    """

    # Hashmap to store the prefix sum and its frequency
    prefix_sum_count = {0: [-1]}  # Start with prefix sum 0 at index -1 for subarrays starting from index 0
    current_sum = 0
    subarrays = []  # List to store the actual subarrays
    
    for i, num in enumerate(nums):
        # Update the running sum (prefix sum)
        current_sum += num
        
        # Check if there is a subarray sum equals to k
        # by checking if current_sum - k exists in prefix_sum_count
        if current_sum - k in prefix_sum_count:
            # Retrieve the indices where this prefix sum occurred
            for start_index in prefix_sum_count[current_sum - k]:
                # Create the subarray from the start index + 1 to the current index
                subarrays.append(nums[start_index + 1:i + 1])
        
        # Update the prefix_sum_count hashmap
        if current_sum in prefix_sum_count:
            prefix_sum_count[current_sum].append(i)  # Store the current index
        else:
            prefix_sum_count[current_sum] = [i]  # Create a new list with the current index

    return subarrays

if __name__=='__main__':

    nums = [1,1,1]
    k = 2
    result = total_subarrays(nums, k) # Output: 2
    print(result)
    result = get_subarrays(nums, k)
    print(result)

    nums = [1,2,3]
    k = 3 
    result = total_subarrays(nums, k) # Output: 2
    print(result)
    result = get_subarrays(nums, k)
    print(result)

    nums = [2,2,1,3,4]
    k = 4
    result = total_subarrays(nums, k) # Output: 3
    print(result)
    result = get_subarrays(nums, k)
    print(result)