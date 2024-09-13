def is_even_or_odd(n):
    
    if n % 2 == 1:
        return 'odd'
    elif n % 2 == 0:
        return 'even'
    else:
        return 'neither'
    
if __name__=='__main__':

    n = 0
    print(is_even_or_odd(n))

    n = 1
    print(is_even_or_odd(n))

    n = 2
    print(is_even_or_odd(n))

    n = 1/2
    print(is_even_or_odd(n))