Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]


from collections import deque

#class TreeNode:
    #def __init__(self, value=0, left=None, right=None):
       # self.value = value
       # self.left = left
        # self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []
    
    results = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level_nodes = deque()
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if left_to_right:
                level_nodes.append(node.value)
            else:
                level_nodes.appendleft(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        results.append(list(level_nodes))
        left_to_right = not left_to_right
    
    return results
