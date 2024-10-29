def first_dup(string):
    """ 
    Time: O(n)
    Space: O(n)
    """
    seen = []
    for char in string:
        if char in seen:
            return char
        else: 
            seen.append(char)
    return None

if __name__=='__main__':

    string = 'acbbac'
    res = first_dup(string) # b
    print(res)