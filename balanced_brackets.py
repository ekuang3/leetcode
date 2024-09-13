def is_balanced(s): 
    """
    Time: O(n), n is the length of the input string.
    Space: O(n), the stack can grow up to the size of the input string in the worst case.
    """ 
    
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    # Initialize an empty stack to keep track of opening brackets 
    stack = [] 
    
    # Iterate over the input string 
    for bracket in s: 
        # If the bracket is an opening bracket, push it onto the stack 
        if bracket in matching_brackets.values(): 
            stack.append(bracket) 
            # If the bracket is a closing bracket and the stack is empty, 
            # or if the bracket does not match the last opening bracket on the stack, 
            # then the string is not balanced 
        elif bracket in matching_brackets.keys():
            if not stack or stack.pop() != matching_brackets[bracket]:
                return False 
            
    # If the stack is empty after all the brackets have been processed,
    # then the string is balanced 
    return not stack 

if __name__=='__main__':

    print(is_balanced('()')) # True 
    print(is_balanced('()[]{}')) # True 
    print(is_balanced('(]')) # False 
    print(is_balanced('([)]')) # False 