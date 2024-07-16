Input: nums = [2,7,11,15], target = 9
Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
def find_pair(nums, target):
    store = sorted(nums)  # Sort the input list
    l, r = 0, len(nums) - 1  # Initialize two pointers: left (l) and right (r)

    while l < r:
        sum_ = store[l] + store[r]  # Calculate the sum of elements at pointers l and r

        if sum_ == target:
            # If the sum equals the target, find the original indices in the unsorted list
            if store[l] != store[r]:
                pos1 = nums.index(store[l])
                pos2 = nums.index(store[r])
            else:
                # When both elements are the same, find the first occurrence and then the next occurrence
                pos1 = nums.index(store[l])
                pos2 = nums.index(store[r], pos1 + 1)
            return pos1, pos2  # Return the indices of the elements

        elif sum_ < target:
            l = l + 1  # If the sum is less than the target, move the left pointer to the right
        else:
            r = r - 1  # If the sum is greater than the target, move the right pointer to the left

    return None  # If no pair is found, return None

      
      
  
