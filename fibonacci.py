# Fibonacci is 0,1,1,2,3,5,8,13,21,34,55...

def fibonacci(n):
    """
    Brute force...

    Time: O(n) b/c it uses a loop to calculate each 
    Fibonacci number up to n
    
    Space: O(1) b/c it stores 3 variables (a,b,c)
    """
    a = 0
    b = 1
    if n < 0: # base case: anything less than 0 is invalid
        print('Incorrect input!')
    elif n == 0: # at 0, return 0
        return 0
    elif n == 1: # at 1, return 1 (0 + 1 = 1)
        return 1
    else: # all else...
        for i in range(1,n):
            c = a+b # prev + next = next.next
            a = b # next becomes prev
            b = c # next.next becomes next
        return b

def fibonacci(n):
    """ 
    Using recursion...

    Time: O(2^n) b/c each call to the function 
    generates 2 more calls until the base case is reached
    
    Space: O(n) b/c the max depth of the recursive
    call stack is n
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__=='__main__':

    print(fibonacci(0)) # 0 
    print(fibonacci(1)) # 1
    print(fibonacci(5)) # 5
    print(fibonacci(10)) # 55
    print(fibonacci(15)) # 610