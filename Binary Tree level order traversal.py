Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrder(root):
        if not root:
            return []  # If the tree is empty, return an empty list
        
        result = []  # This will store the final level order traversal
        queue = deque([root])  # Initialize the queue with the root node

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            current_level = []  # List to store the nodes at the current level
            
            for _ in range(level_size):
                node = queue.popleft()  # Dequeue the next node
                current_level.append(node.val)  # Add the node's value to the current level list
                
                # Enqueue the left child if it exists
                if node.left:
                    queue.append(node.left)
                
                # Enqueue the right child if it exists
                if node.right:
                    queue.append(node.right)
            
            # Add the current level list to the result
            result.append(current_level)
        
        return result
