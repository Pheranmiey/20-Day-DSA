intervals = [[1, 3], [2, 6], [8, 10], [15, 18]] 
Output: [[1, 6], [8, 10], [15, 18]]


def merge_intervals(intervals):
    # Step 1: Sort the intervals by the start time
    intervals = sorted(intervals, key=lambda x: x[0])

    # Step 2: Initialize the result list
    ans = []

    # Step 3: Iterate through the sorted intervals
    for interval in intervals:
        # If ans is empty or there is no overlap, add the interval to ans
        if not ans or ans[-1][1] < interval[0]:
            ans.append(interval)
        else:
            # If there is an overlap, merge the intervals
            ans[-1][1] = max(ans[-1][1], interval[1])

    # Step 4: Return the result list
    return ans
