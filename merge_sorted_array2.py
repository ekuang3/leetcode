def brute(arr1, arr2):
    """
    Time: O((len(arr1) + len(arr2)) * log(len(arr1) + len(arr2)))
    Space: O(m+n) which is the size of the merged array 
    """
    return sorted([*arr1, *arr2]) 

def merge_sorted_arrays(arr1, arr2):
    """ 
    Time: O(m+n) where m and n are the lengths of the input arrays

    Space: O(m+n), which is the size of the merged array
    """

    merged_array = []
    i = 0
    j = 0
  
    # Traverse both lists
    # If the current element of first list
    # is smaller than the current element
    # of the second list, then store the
    # first list's value and increment the index 

    while i < len(arr1) and j < len(arr2): 
      
        if arr1[i] < arr2[j]: 
            merged_array.append(arr1[i])
            i = i + 1
        else: 
            merged_array.append(arr2[j])
            j = j + 1
      
  
    # Store remaining elements of the first list
    while i < len(arr1): 
        merged_array.append(arr1[i])
        i = i + 1
  
    # Store remaining elements of the second list
    while j < len(arr2): 
        merged_array.append(arr2[j])
        j = j + 1

    return merged_array

if __name__=='__main__':
        
    arr1, arr2 = [1, 3, 5], [2, 4, 6]
    res = merge_sorted_arrays(arr1, arr2) # [1, 2, 3, 4, 5, 6]
    print(res)