class TreeNode:
    def __init__(self, key, data):
        self.key = key  # The token
        self.data = [data]  # List to store URLs
        self.left = None
        self.right = None
