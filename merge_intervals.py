"""
Task: Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

def merge_intervals(intervals):
    """
    Time: O(n log n), b/c O(n log n) for sorting and O(n) for merging.
    Space: O(n), for storing the output list of merged intervals.
    """
    if not intervals:
        return []
    
    # Sort intervals by the start of each interval
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]  # Initialize the merged list with the first interval
    
    for i in range(1, len(intervals)):
        # Get the last interval in the merged list
        last_interval = merged[-1]
        
        # If the current interval overlaps with the last interval, merge them
        if intervals[i][0] <= last_interval[1]:
            last_interval[1] = max(last_interval[1], intervals[i][1])
        else:
            # Otherwise, there is no overlap, so add the current interval
            merged.append(intervals[i])
    
    return merged

if __name__=='__main__':

    intervals = [[1,3],[2,6],[8,10],[15,18]] # [[1,6],[8,10],[15,18]]
    result = merge_intervals(intervals)
    print(result)
