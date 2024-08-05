Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22
Output: true

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def hasPathSum(root, targetSum):
    if not root:
        return False
    
    # If we reach a leaf node, check if the remaining sum equals the node's value
    if not root.left and not root.right:
        return targetSum == root.val
    
    # Recursively check the left and right subtrees with the updated target sum
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum
