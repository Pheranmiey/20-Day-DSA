# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleNode(head: ListNode) -> ListNode:
    # Initialize two pointers, both starting at the head of the list
    slow = head
    fast = head

    # Move slow pointer one step at a time and fast pointer two steps at a time
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # When fast pointer reaches the end, slow pointer will be at the middle node
    return slow
