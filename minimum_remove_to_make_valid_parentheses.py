def minRemoveToMakeValid(s: str) -> str:
    """Time and space complexity is O(n) where n is length of string"""
    # Convert the string into a list so that we can mutate it
    s = list(s)
    
    # Stack to hold the indices of unmatched '('
    stack = []
    
    # First pass: Remove unmatched ')'
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack:
                stack.pop()  # matched, so we pop the corresponding '('
            else:
                s[i] = ''  # unmatched ')', so we mark it for removal

    # Second pass: Remove unmatched '('
    while stack:
        s[stack.pop()] = ''  # unmatched '(', so we mark it for removal
    
    # Rebuild the string and return the result
    return ''.join(s)

# Example usage
s = "lee(t(c)o)de)" # Output: "lee(t(c)o)de"
s = "))((" # Output: ""
result = minRemoveToMakeValid(s)
print(result)