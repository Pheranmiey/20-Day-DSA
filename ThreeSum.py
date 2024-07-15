def threeSum(nums):
  store = []   # Initialize an empty list to store the result triplets
  nums = sorted(nums)  # Sort the input list

  for i in range(len(nums)):
    # Skip duplicate elements to avoid duplicate triplets in the result
    if  i > 0 and nums[i] == nums[i-1]:
      continue
    
    # Initialize two pointers: one starting just after the current element and one at the end of the list
    l, r = i + 1, len(nums) - 1
    
    # Use a while loop to find triplets that sum to zero
    while l < r:
      # Calculate the sum of the current triplet
      target = nums[i] + nums[l] + nums[r]
      
      # If the sum is greater than zero, move the right pointer to the left
      if target > 0:
        r -= 1
      # If the sum is less than zero, move the left pointer to the right
      elif target < 0:
        l += 1
      # If the sum is zero, add the triplet to the result list
      else:
        store.append([nums[i], nums[l], nums[r]])
        l += 1
        # Skip duplicate elements to avoid duplicate triplets in the result
        while nums[l] == nums[l-1] and l < r:
          l += 1
  return store
