Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1  # Initialize left and right pointers

    # Binary search loop
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        
        if nums[mid] == target:
            return mid  # Target found, return the index
        elif nums[mid] < target:
            left = mid + 1  # Move the left pointer to the right of mid
        else:
            right = mid - 1  # Move the right pointer to the left of mid

    # Return the insert position
    return left

