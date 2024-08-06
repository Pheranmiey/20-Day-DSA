Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, current_path, current_sum):
            if not node:
                return
            
            # Include the current node in the path
            current_path.append(node.val)
            current_sum += node.val
            
            # Check if the current node is a leaf and its path sum equals the target sum
            if not node.left and not node.right and current_sum == targetSum:
                paths.append(list(current_path))
            
            # Continue the search in the left and right subtrees
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
            
            # Backtrack to explore other paths
            current_path.pop()
        
        paths = []
        dfs(root, [], 0)
        return paths
