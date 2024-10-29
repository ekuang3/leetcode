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
    
    # Example 1
    nums = [1, 2, 2, 3, 1, 1, 4] 
    res = frequency_count(nums) # {1: 3, 2: 2, 3: 1, 4: 1}
    print(res)

    # Example 2
    sentence = "I have a nice car with a nice tires"
    words = sentence.split(' ')
    res = frequency_count(words)
    print(res)

    # ...change frequency to percentage
    size = len(words)
    freq_dict = {}
    for key,value in res.items():
        freq_dict[key] = round(value / size, 2)
    print(freq_dict)