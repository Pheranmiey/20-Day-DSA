Input: fruits = [1,2,3,2,2]
Output: 4

def totalFruit(fruits):
    # Dictionary to count the number of each type of fruit in the current window
    count = {}
    # Left pointer of the window
    left = 0  
    # Variable to keep track of the maximum length of subarray
    max_length = 0  

    # Iterate through the array with the right pointer
    for right in range(len(fruits)):
        # Add current fruit to the window
        count[fruits[right]] = count.get(fruits[right], 0) + 1

        # Ensure the window has at most two types of fruits
        while len(count) > 2:
            # Decrement the count of the fruit at the left pointer
            count[fruits[left]] -= 1  
            # If the count becomes zero, remove the fruit from the dictionary
            if count[fruits[left]] == 0:  
                del count[fruits[left]]
            # Move the left pointer to the right
            left += 1  

        # Update the maximum length of the window
        max_length = max(max_length, right - left + 1)

    return max_length
