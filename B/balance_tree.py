class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def is_balanced(root: TreeNode) -> bool:
    def height_and_balance(node: TreeNode):
        if not node:
            return 0, True
        
        left_height, left_balanced = height_and_balance(node.left)
        right_height, right_balanced = height_and_balance(node.right)
        
        is_balanced = abs(left_height - right_height) <=1
        
        return max(left_height, right_height) + 1, left_balanced and right_balanced and is_balanced
    _,balanced = height_and_balance(root)
    return balanced