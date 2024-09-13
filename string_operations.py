def evaluate_expression_stack(expression):
    """
    Time: O(n), n is number of characters in expression.
    Space: O(n), size of stack.
    """
    # Initialize an empty stack to hold numbers and intermediate results.
    stack = []

    # This will store the current number as it's being constructed from digits.
    current_number = 0

    # This keeps track of the last operator encountered. We start with '+' as the default.
    operator = '+'
    
    # Valid operators we allow in the expression.
    valid_operators = '+-*/'

    # Check if the expression starts or ends with an operator, which would be invalid.
    if expression[0] in valid_operators or expression[-1] in valid_operators:
        return 'invalid'
    
    # We will iterate over each character in the expression.
    i = 0
    while i < len(expression):
        char = expression[i]
        
        # If the current character is a digit, we build the full number.
        # For example, in the string "123", the characters '1', '2', and '3' need to be combined
        # into the integer 123. Each digit is processed and multiplied by 10 for place value.
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        
        # If the current character is an operator (+, -, *, or /)
        elif char in valid_operators:
            # Check if the previous character was also an operator. If so, the expression is invalid.
            if i > 0 and expression[i - 1] in valid_operators:
                return 'invalid'
            
            # Process the number and operator encountered so far.
            # Depending on the last operator, we push the appropriate value to the stack.
            # If the operator is '+', we just add the number.
            if operator == '+':
                stack.append(current_number)
            # If the operator is '-', we subtract by pushing the negative of the number.
            elif operator == '-':
                stack.append(-current_number)
            # If the operator is '*', we multiply the last number in the stack with the current one.
            elif operator == '*':
                stack.append(stack.pop() * current_number)
            # If the operator is '/', we divide the last number in the stack by the current one.
            elif operator == '/':
                stack.append(int(stack.pop() / current_number))  # Integer division

            # For debugging, print the current state of the stack and the number.
            print(stack, current_number)

            # Now, we update the operator to the current one for the next number.
            operator = char
            # Reset current_number to start building the next number.
            current_number = 0
        
        else:
            # If we encounter a character that's neither a digit nor a valid operator, return invalid.
            return 'invalid'
        
        # Move to the next character.
        i += 1
    
    # Print the stack and the last operator, for debugging purposes.
    print(stack, operator, current_number)
    
    # Once we've processed all characters, we handle the last number based on the last operator.
    if operator == '+':
        stack.append(current_number)
    elif operator == '-':
        stack.append(-current_number)
    elif operator == '*':
        stack.append(stack.pop() * current_number)
    elif operator == '/':
        stack.append(int(stack.pop() / current_number))  # Integer division
    
    # Finally, sum up everything in the stack and return the result.
    return sum(stack)


if __name__=='__main__':

    print(evaluate_expression_stack("1+2*3"))      # Output: 7
    print(evaluate_expression_stack("4-2+6*3"))    # Output: 20
    print(evaluate_expression_stack("1++2"))       # Output: invalid
    print(evaluate_expression_stack("1-2*3"))      # Output: -5
    print(evaluate_expression_stack("10*5-3"))     # Output: 47
