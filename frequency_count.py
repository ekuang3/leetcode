def frequency_count(nums):
    """
    Time: O(n), where n is the length of the list nums. Each element is processed once.
    Space: O(u), where u is the number of unique elements in nums. 
    """
    # Initialize an empty dictionary to store frequency counts
    freq_dict = {}

    # Iterate through each element in the list
    for num in nums:
        # If the element is already in the dictionary, increment its count
        if num in freq_dict:
            freq_dict[num] += 1
        # If the element is not in the dictionary, add it with count 1
        else:
            freq_dict[num] = 1

    return freq_dict

if __name__=='__main__':
    
    nums = [1, 2, 2, 3, 1, 1, 4]
    print(frequency_count(nums))
