class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs(root):
    result = []
    
    def _dfs(node):
        if node:
            result.append(node.value)
            _dfs(node.left)
            _dfs(node.right)
            
    _dfs(root)
    return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("DFS Traversal:", dfs(root))
