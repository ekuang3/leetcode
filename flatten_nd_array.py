def flatten(array):
    """
    Time: O(n), where n is the total number of elements in the nested list, including elements in any nested sublists
    Space: O(n), for the output list, plus up to O(d) auxiliary space for recursion
    """
    result = []
    for item in array:
        if isinstance(item, list):
            result.extend(flatten(item))  # Recursively flatten nested lists
        else:
            result.append(item)  # Add non-list items directly
    return result

if __name__=='__main__':

    array = [1, [2, 3], [4, [5, 6]], 7]
    flattened_array = flatten(array) # Output: [1, 2, 3, 4, 5, 6, 7]
    print(flattened_array)