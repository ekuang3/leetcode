def product_except_self(nums):
    n = len(nums)
    
    # Initialize the result array where each element will be the product except self
    result = [1] * n
    
    # First pass: calculate the left product for each element
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Second pass: calculate the right product for each element and multiply with the left product
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

if __name__=='__main__':

    nums = [1,2,3,4,5]
    result = product_except_self(nums)
    print(result)