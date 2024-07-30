from TreeNode import *
class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root is None:
            self.root = TreeNode(key, data)
        else:
            self._insert_recursive(self.root, key, data)

    def _insert_recursive(self, node, key, data):
        if key == node.key:
            node.data.append(data)
        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key, data)
            else:
                self._insert_recursive(node.left, key, data)
        else:
            if node.right is None:
                node.right = TreeNode(key, data)
            else:
                self._insert_recursive(node.right, key, data)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append((node.key, node.data))
            self._inorder_recursive(node.right, result)
