def brute(arr):
    """
    Time: O(n), where n is the number of elements in the list
    
    Space: O(n), as the set needs to store each element in the 
    list in order to determine if it is a duplicate or not
    """
    return set(arr)

def remove_dups(arr):
    """
    Time: O(n^2), where n is the number of elements in the list
    Space: O(n), to store unique elements in the set
    """

    unique = []  
    for element in arr:  
        if element not in unique: 
            unique.append(element)

    return unique

def remove_duplicates(arr):
    """ 
    Time: O(n), where n is the length of the array

    Space: O(n), because we store each unique 
    element as a key in the dictionary
    """
    d = {}
    for element in arr:
        d[element] = None
    return list(d.keys())

if __name__=='__main__':
    
    arr = [1, 1, 2, 2, 3, 3]
    res = remove_duplicates(arr) # [1,2,3]
    print(res)

    arr = [[1, 1], [1, 1]] # [[1, 1]]
    res = remove_dups(arr)
    print(res)