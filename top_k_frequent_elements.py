import heapq
from collections import Counter

def top_k_frequent(nums, k):
    """
    Time: O(n log k), where n is the number of elements in nums, and k is the number of most frequent elements to return.
    Space: O(n), where n is the number of elements in nums. Extra space used to store the frequency map and the heap.
    """

    # Step 1: Count the frequency of each element
    frequency_map = Counter(nums)  # This returns a dictionary-like object with frequency counts
    print(frequency_map)

    # Step 2: Use a min-heap to keep track of the k most frequent elements
    # We use (-frequency, element) because Python's heapq is a min-heap, and we want max frequency.
    heap = []
    
    for num, freq in frequency_map.items():
        heapq.heappush(heap, (-freq, num))  # Push negative of frequency for max-heap behavior
    
    # Step 3: Extract the top k elements from the heap
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])  # Pop and get the element
    
    return result

if __name__=='__main__':

    nums = [1,1,1,2,2,3]
    k = 2

    result = top_k_frequent(nums, k) # [1,2]
    print(result)