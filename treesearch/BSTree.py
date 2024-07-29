from TreeNode import *

class BSTree:
    def __init__(self):
        # YOUR CODE GOES HERE
        self.root = None
        pass

    def insert(self, value):
        # YOUR CODE GOES HERE
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)
        pass

    def _insert(self, node, value):
        # YOUR CODE GOES HERE
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)



    def search(self, value):
        # YOUR CODE GOES HERE
        return self._search_recursive(self.root, value)
        pass
    
    def _search_recursive(self, node, key):
        # YOUR CODE GOES HERE
        if node is None:
            return False
        if value == node.value:
            return True
        elif key < node.value:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

        pass
    
    def inorder_traversal(self):
        # YOUR CODE GOES HERE
        return self._inorder_recursive(self.root, [])
        pass
    
    def _inorder_recursive(self, node, result):
        # YOUR CODE GOES HERE
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
        return result
        pass