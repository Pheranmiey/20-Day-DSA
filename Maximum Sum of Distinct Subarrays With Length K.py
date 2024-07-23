
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15

def maximumSubarraySum(nums, k):

        n = len(nums)
    
        # If the number of elements in nums is less than k, return 0
        if n < k:
            return 0

        max_sum = 0  # Variable to keep track of the maximum sum of subarrays
        window_sum = 0  # Variable to keep track of the sum of the current window
        count = {}  # Dictionary to count the occurrences of elements in the current window
        left = 0  # Left pointer of the window

        # Iterate through the array with the right pointer
        for right in range(n):
            # Add current element to the window
            window_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1

            # Ensure window size does not exceed k
            while right - left + 1 > k:
                window_sum -= nums[left]  # Subtract the element at the left pointer from the window sum
                count[nums[left]] -= 1  # Decrement the count of the element at the left pointer
                if count[nums[left]] == 0:  # If the count becomes zero, remove the element from the dictionary
                    del count[nums[left]]
                left += 1  # Move the left pointer to the right

            # Check if the current window has exactly k distinct elements
            if right - left + 1 == k and len(count) == k:
                max_sum = max(max_sum, window_sum)  # Update the maximum sum if the current window sum is larger

        return max_sum
        
