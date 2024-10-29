def longest_palindrome_substring(s):
    """
    Time: O(n²), where n is the length of the input string s; each center * n total centers.
    Space: O(1), no new data structures created. 
    """
    # Helper function to expand around the center
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the longest palindrome substring for the given center
        return s[left + 1:right]
    
    # If the input string is empty or has only one character
    if len(s) <= 1:
        return s
    
    longest = ""
    
    for i in range(len(s)):
        # Odd length palindromes (single character center)
        palindrome1 = expand_around_center(i, i)
        #print(i, i, palindrome1)
        
        # Even length palindromes (two character center)
        palindrome2 = expand_around_center(i, i + 1)
        #print(i, i+1, palindrome2)

        # Update longest palindrome if we find a longer one
        longest = max(longest, palindrome1, palindrome2, key=len)
    
    return longest


if __name__=='__main__':

    s = "babad" 
    result = longest_palindrome_substring(s) # bab
    print(result)

    s = "cbbd"
    result = longest_palindrome_substring(s) # bb
    print(result)