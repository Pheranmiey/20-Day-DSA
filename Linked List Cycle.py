def hasCycle(head):
        # If the list is empty, there is no cycle
        if not head:
            return False

        # Initialize two pointers, fast and slow
        # Fast moves 2 steps at a time and slow moves 1 step at a time
        fast = head.next
        slow = head.next

        # Loop until the fast pointer reaches the end of the list
        while fast and fast.next:
            # Move slow pointer by 1 step
            slow = slow.next
            # Move fast pointer by 2 steps
            fast = fast.next.next

            # If slow and fast meet, there's a cycle in the list
            if slow == fast:
                return True

        # If we exit the loop, fast reached the end of the list, hence no cycle
        return False
