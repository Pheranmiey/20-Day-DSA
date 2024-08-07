Input: nums = [3,0,1]
Output: 2

def find_missing_number(nums):
    n = len(nums)  # Length of the array
    
    # Cyclic sort to place each number at its correct index if possible
    i = 0
    while i < n:
        # Check if the current number is within the valid range and not at the correct position
        if nums[i] < n and nums[i] != nums[nums[i]]:
            # Swap the current number with the number at its correct position
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        else:
            # Move to the next index if the current number is already in the correct position
            i += 1
    
    # After sorting, find the first index where the number does not match the index
    for i in range(n):
        if nums[i] != i:
            return i  # The missing number is found
    
    # If all numbers are in their correct positions, the missing number is n
    return n
