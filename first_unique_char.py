def first_unique_char(s):
    """ 
    Time: O(n)
    Space: O(n) 
    """
    # Create a dictionary to store the frequency of each character
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1 
    
    # Loop through the string and find the first character with a count of 1
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return s[i]
    
    # If no unique character is found, return -1
    return -1

if __name__=='__main__':

    s = "leetcode"
    res = first_unique_char(s) 
    print(res) # Output: 0 b/c 'l' at index 0

    s = "loveleetcode"
    res = first_unique_char(s)
    print(res) # Output: 2 b/c 'v' at index 2

    s = "aabb"
    res = first_unique_char(s)
    print(res) # Output: -1 b/c None