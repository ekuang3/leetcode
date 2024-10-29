def binary_search(arr, target):
    """ 
    Time: O(log n), where n is the length of the input array
    Space: O(1), b/c no additional data structure is used
    """
    left, right = 0, len(arr) - 1 
            
    while left <= right:
        mid = (left + right) // 2
                
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 
                    
    return -1

if __name__=='__main__':

    arr = [1, 3, 5, 7, 9]

    x = 5 
    index = binary_search(arr, x) # 2
    print(index)

    x = 6 
    index = binary_search(arr, x) # -1
    print(index)