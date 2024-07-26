# Example usage
intervals = [[1,3], [6,9]]
newInterval = [2,5]

def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
    
    # Step 1: Add all intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Step 2: Merge all overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)
    
    # Step 3: Add all intervals starting after newInterval ends.
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

