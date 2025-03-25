import unittest
from binary_Search_tree import Node, BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree(Node(10, 'root', 1))
        self.bst.put(5, 'left')
        self.bst.put(15, 'right')

    def test_search_existing_key(self):
        self.assertEqual(self.bst._search(self.bst.root, 10), 'root')
        self.assertEqual(self.bst._search(self.bst.root, 5), 'left')
        self.assertEqual(self.bst._search(self.bst.root, 15), 'right')

    def test_search_non_existing_key(self):
        self.assertIsNone(self.bst._search(self.bst.root, 20))
        self.assertIsNone(self.bst._search(self.bst.root, 0))

    def test_put_new_key(self):
        self.bst.put(20, 'new_right')
        self.assertEqual(self.bst._search(self.bst.root, 20), 'new_right')
        self.bst.put(2, 'new_left')
        self.assertEqual(self.bst._search(self.bst.root, 2), 'new_left')

    def test_put_existing_key(self):
        self.bst.put(10, 'new_root')
        self.assertEqual(self.bst._search(self.bst.root, 10), 'new_root')
        self.bst.put(5, 'new_left')
        self.assertEqual(self.bst._search(self.bst.root, 5), 'new_left')

    def test_max(self):
        self.assertEqual(self.bst.max().key, 15)
        self.bst.put(20, 'new_right')
        self.assertEqual(self.bst.max().key, 20)

    def test_min(self):
        self.assertEqual(self.bst.min().key, 5)
        self.bst.put(2, 'new_left')
        self.assertEqual(self.bst.min().key, 2)

    def test_select_valid_rank(self):
        self.bst.put(2, 'new_left')
        self.bst.put(20, 'new_right')
        self.assertEqual(self.bst.get_node_with_rank(0).key, 2)
        self.assertEqual(self.bst.get_node_with_rank(1).key, 5)
        self.assertEqual(self.bst.get_node_with_rank(2).key, 10)
        self.assertEqual(self.bst.get_node_with_rank(3).key, 15)
        self.assertEqual(self.bst.get_node_with_rank(4).key, 20)

    def test_select_invalid_rank(self):
        self.bst.put(2, 'new_left')
        self.bst.put(20, 'new_right')
        self.assertIsNone(self.bst.get_node_with_rank(-1))
        self.assertIsNone(self.bst.get_node_with_rank(5))

    def test_rank_existing_key(self):
        self.bst.put(2, 'new_left')
        self.bst.put(20, 'new_right')
        self.assertEqual(self.bst.rank(2), 0)
        self.assertEqual(self.bst.rank(5), 1)
        self.assertEqual(self.bst.rank(10), 2)
        self.assertEqual(self.bst.rank(15), 3)
        self.assertEqual(self.bst.rank(20), 4)
        self.assertEqual(self.bst.rank(25), 5)

    def test_size_of_tree(self):
        self.assertEqual(Node.get_size(self.bst.root), 3)
        self.bst.put(20, 'new_right')
        self.assertEqual(Node.get_size(self.bst.root), 4)
        self.bst.put(2, 'new_left')
        self.assertEqual(Node.get_size(self.bst.root), 5)

    def test_delete_min(self):
        self.bst.put(2, 'new_left')
        self.bst.put(1, 'new_left_left')
        self.bst.delete_min()
        self.assertEqual(self.bst.min().key, 2)
        self.bst.delete_min()
        self.assertEqual(self.bst.min().key, 5)

    def test_delete_max(self):
        self.bst.put(20, 'new_right')
        self.bst.put(25, 'new_right_right')
        self.bst.delete_max()
        self.assertEqual(self.bst.max().key, 20)
        self.bst.delete_max()
        self.assertEqual(self.bst.max().key, 15)

    def test_delete_existing_key(self):
        self.bst.put(2, 'new_left')
        self.bst.put(20, 'new_right')
        self.bst.put(1, 'new_left_left')
        self.bst.put(25, 'new_right_right')
        
        self.bst.root = self.bst.delete(20)
        self.assertIsNone(self.bst._search(self.bst.root, 20))
        self.assertEqual(self.bst.max().key, 25)
        
        self.bst.root = self.bst.delete(5)
        self.assertIsNone(self.bst._search(self.bst.root, 5))
        self.assertEqual(self.bst.min().key, 1)

    def test_delete_non_existing_key(self):
        self.bst.put(2, 'new_left')
        self.bst.put(20, 'new_right')
        
        original_size = Node.get_size(self.bst.root)
        self.bst.root = self.bst.delete(100)
        self.assertEqual(Node.get_size(self.bst.root), original_size)
        
    def test_delete_root(self):
        self.bst.put(2, 'new_left')
        self.bst.put(20, 'new_right')
        
        self.bst.root = self.bst.delete(10)
        self.assertIsNone(self.bst._search(self.bst.root, 10))
        self.assertEqual(self.bst.root.key, 15)

if __name__ == '__main__':
    unittest.main()