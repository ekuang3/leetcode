from valid_palindrome import isPalindrome

def brute(s):
    """
    Time: O(n**2), where n is the length of the input string. 
    Space: O(n) b/c of temporary string creation.
    """ 
    
    #First check if original string is a palindrome 
    if isPalindrome(s): return True 
 
    # Delete one character at a time and validate new string 
    for idx,char in enumerate(s): 
        tmp = s[0:idx] + s[idx+1:] 
        if isPalindrome(tmp): return True 
        
    return False 

def isPalindromeRange(s, start, end):
    """
    Helper function to check if the substring s[start:end] is a palindrome.
    """
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def validPalindrome(s):
    """
    Time: O(n), where n is the length of the input string.
    Space: O(1), since no additional space is used except for a few pointers.
    """
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            # Check if skipping either s[start] or s[end] results in a palindrome
            return isPalindromeRange(s, start + 1, end) or isPalindromeRange(s, start, end - 1)
        start += 1
        end -= 1
    
    return True  # If no mismatches, the string is already a palindrome

if __name__=='__main__':

    s = "abca" # true
    result = validPalindrome(s)
    print(result)

    s = "abc" # false
    result = validPalindrome(s)
    print(result)