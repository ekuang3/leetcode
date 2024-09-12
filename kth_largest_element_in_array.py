def brute(nums, k):
    """
    Time: O(n log n), sorting has time complexity of O(n log n)
    Space: O(n)
    """
    nums.sort(reverse=True)
    return nums[k-1]

import heapq
def find_kth_largest(nums, k):
    """
    Time: O(nlogk), where n is total elements in nums
    Space: O(k), where heap stores only k elements

    Note: more efficient than quickselect method if k is much smaller than n
    """
    # Create a min-heap with the first k elements
    heap = nums[:k]
    heapq.heapify(heap) # smallest element at index 0; ascending order
    
    # Process the remaining elements
    for num in nums[k:]:
        if num > heap[0]:  # Only add the number if it's bigger than the smallest in the heap
            heapq.heappushpop(heap, num)
    
    # The root of the heap is the kth largest element
    return heap[0]

if __name__=='__main__':

    nums = [3,2,1,5,6,4]
    k = 3
    result = brute(nums, k)
    print(result)

    result = find_kth_largest(nums, k)
    print(result)