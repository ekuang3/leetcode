class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_root_to_leaf_paths(root):
    def dfs(node, current_sum):
        if not node:
            return 0
        
        # Update the current path sum
        current_sum = current_sum * 10 + node.val
        
        # If it's a leaf, return the current sum
        if not node.left and not node.right:
            return current_sum
        
        # Recursively sum the left and right paths
        return dfs(node.left, current_sum) + dfs(node.right, current_sum)

    return dfs(root, 0)


# Example tree
#      7
#     / \
#    3   2
#   / \  / \
#  5   6 8  9
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
root.right.left = TreeNode(8)
root.right.right = TreeNode(9)

# Calculate the sum of all root-to-leaf paths
result = sum_root_to_leaf_paths(root)
print(result)  # Output should be 2928 b/c (735 + 736 + 728 + 729)
