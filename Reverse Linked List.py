Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    
    while curr is not None:
        next_node = curr.next  # Store the next node
        curr.next = prev  # Reverse the current node's pointer
        prev = curr  # Move prev and curr one step forward
        curr = next_node
    
    return prev
