def brute(s):
    """
    Time: O(n), where n is the length of the input string.
    Space: O(n), due to the storage of the filtered list and its reversed copy.
    """
    s = s.lower()
    s = list(s)
    s = list(filter(lambda x:x.isalnum(), s))
    if s == s[::-1]: return True
    else: return False

def is_palindrome(s):
    """
    A phrase is a palindrome if, after converting all uppercase letters into 
    lowercase letters and removing all non-alphanumeric characters, it reads 
    the same forward and backward. Alphanumeric characters include letters 
    and numbers.

    Time: O(n), where n is the length of the input string, since we process each character once.
    Space: O(1), since the function uses a fixed amount of extra space regardless of the input size.
    """
    start = 0
    end = len(s)- 1
    while start < end:  # We stop when start and end pointers meet
        # Move the start pointer until we find an alphanumeric character
        while start < end and not s[start].isalnum():
            start += 1
        
        # Move the end pointer until we find an alphanumeric character
        while start < end and not s[end].isalnum():
            end -= 1
        
        # Compare the characters at start and end, after converting to lowercase
        if s[start].lower() != s[end].lower():
            return False
        
        # Move both pointers towards the center
        start += 1
        end -= 1
    
    return True

if __name__=='__main__':

    s = "A man, a plan, a canal: Panama"

    result = brute(s)

    result = is_palindrome(s) # Output: true
    print(result)

