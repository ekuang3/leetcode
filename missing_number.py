def find_missing_number(arr): 
    """
    Time: O(n), where n is the length of the array.
    Space: O(1), constant space
    """
    n = len(arr) + 1
    expected_sum = n * (n+1) // 2
    actual_sum = sum(arr) 
    
    return expected_sum - actual_sum 

if __name__=='__main__':

    arr = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 30
        ]
        
    result = find_missing_number(arr) # 29 
    print(result)