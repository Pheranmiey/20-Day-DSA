Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]

def reverseBetween(head, left, right):
        if not head or left == right:
            return head
        
        # Create a dummy node to simplify the head operations
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node before the start of the sublist to be reversed
        for _ in range(left - 1):
            prev = prev.next
        
        # Reverse the sublist from left to right
        reverse_start = prev.next
        curr = reverse_start.next
        
        for _ in range(right - left):
            reverse_start.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = reverse_start.next
        
        return dummy.next
