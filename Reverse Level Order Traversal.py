Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def reverse_level_order_traversal(root):
    # If the tree is empty, return an empty list
    if not root:
        return []

    # Initialize a queue for BFS and a deque to store results in reverse order
    queue = deque([root])
    result = deque()

    # Perform level order traversal using BFS
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        # List to store the values of nodes at the current level
        level_nodes = []
        
        # Process each node at the current level
        for _ in range(level_size):
            # Dequeue a node from the front of the queue
            node = queue.popleft()
            # Add the node's value to the level's list
            level_nodes.append(node.val)
            # Enqueue the left child if it exists
            if node.left:
                queue.append(node.left)
            # Enqueue the right child if it exists
            if node.right:
                queue.append(node.right)
        
        # Add the current level's list at the beginning of the result deque
        result.appendleft(level_nodes)

    # Convert the deque to a list before returning
    return list(result)
