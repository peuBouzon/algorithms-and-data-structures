
class Node:
    @staticmethod
    def get_size(node):
        return node.size if node else 0

    def __init__(self, key, value, size):
        self.key = key
        self.value = value
        self.left : Node = None
        self.right : Node = None
        self.size = size # number of keys in the subtree rooted at this node

class BinarySearchTree:
    def __init__(self, root):
        if not root:
            raise ValueError("A root node must be specified.")
        self.root = root

    def get(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node.value
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
    
    def put(self,key, value):
        return self._put(self.root, key, value)

    def _put(self, node : Node, key, value):
        if not node:
            return Node(key, value, 1)
        if node.key == key:
            node.value = value
        elif key < node.key:
            node.left = self._put(node.left, key, value)
        else:
            node.right = self._put(node.right, key, value)
        node.size = Node.get_size(node.right) + Node.get_size(node.left) + 1
        return node

    def max(self):
        if not self.root:
            return
        node : Node = self.root
        while node.right:
            node = node.right

        return node
    
    def min(self):
        return self._min(self.root)
    
    def _min(self, node):
        if not node:
            return
        while node.left:
            node = node.left
        return node
    
    # get the key with the specified rank
    def get_node_with_rank(self, rank):
        return self._get_node_with_rank(self.root, rank)

    def _get_node_with_rank(self, node : Node, rank):
        if not node:
            return
        left_size = Node.get_size(node.left)
        
        if rank == left_size:
            return node
        if rank < left_size:
            return self._get_node_with_rank(node.left, rank)
        return self._get_node_with_rank(node.right, rank - left_size - 1)
    
    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, node : Node, key):
        if not node:
            return 0
        if node.key == key:
            return Node.get_size(node.left)
        if key < node.key:
            return self._rank(node.left, key)
        return self._rank(node.right, key) + Node.get_size(node.left) + 1
    
    def delete_min(self):
        return self._delete_min(self.root)

    def _delete_min(self, node : Node):
        if not node.left:
            return node.right
        node.left = self._delete_min(node.left)
        node.size = Node.get_size(node.right) + Node.get_size(node.left) + 1
        return node

    def delete_max(self):
        return self._delete_max(self.root)

    def _delete_max(self, node : Node):
        if not node.right:
            return node.left
        node.right = self._delete_max(node.right)
        node.size = Node.get_size(node.right) + Node.get_size(node.left) + 1
        return node

    def delete(self, key):
        return self._delete(self.root, key)

    def _delete(self, node : Node, key):
        if not node:
            return None
        if node.key == key:
            if not node.right:
                return node.left
            if not node.left:
                return node.right

            tmp = node
            node = self._min(tmp.right)
            node.right = self._delete_min(tmp.right)
            node.left = tmp.left
        elif key < node.key:
            node.left = self._delete(node.left,  key)
        else:
            node.right = self._delete(node.right, key)
        node.size = Node.get_size(node.right) + Node.get_size(node.left) + 1
        return node

        