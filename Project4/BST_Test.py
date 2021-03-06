import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BSTTester(unittest.TestCase):

	def setUp(self):
		self.tree = Binary_Search_Tree()

	def test_empty_tree(self):
		self.assertEqual('[ ]', self.tree.pre_order())
		self.assertEqual('[ ]', self.tree.post_order())
		self.assertEqual('[ ]', self.tree.in_order())
		self.assertEqual('[ ]', self.tree.__str__())
		self.assertEqual(0, self.tree.get_height())

	def test_insert_one(self):
		self.tree.insert_element(12)
		self.assertEqual('[ 12 ]', self.tree.pre_order())
		self.assertEqual('[ 12 ]', self.tree.post_order())
		self.assertEqual('[ 12 ]', self.tree.in_order())
		self.assertEqual('[ 12 ]', self.tree.__str__())
		self.assertEqual(1, self.tree.get_height())

	def test_insert_parent_one_child_small(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.assertEqual('[ 12, 10 ]', self.tree.pre_order())
		self.assertEqual('[ 10, 12 ]', self.tree.post_order())
		self.assertEqual('[ 10, 12 ]', self.tree.in_order())
		self.assertEqual('[ 10, 12 ]', self.tree.__str__())
		self.assertEqual(2, self.tree.get_height())

	def test_insert_parent_one_child_big(self):
		self.tree.insert_element(12)
		self.tree.insert_element(14)
		self.assertEqual('[ 12, 14 ]', self.tree.pre_order())
		self.assertEqual('[ 14, 12 ]', self.tree.post_order())
		self.assertEqual('[ 12, 14 ]', self.tree.in_order())
		self.assertEqual('[ 12, 14 ]', self.tree.__str__())
		self.assertEqual(2, self.tree.get_height())

	def test_insert_parent_two_children(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(14)
		self.assertEqual('[ 12, 10, 14 ]', self.tree.pre_order())
		self.assertEqual('[ 10, 14, 12 ]', self.tree.post_order())
		self.assertEqual('[ 10, 12, 14 ]', self.tree.in_order())
		self.assertEqual('[ 10, 12, 14 ]', self.tree.__str__())
		self.assertEqual(2, self.tree.get_height())

	def test_insert_parent_one_child_two_leaf_small(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(5)
		self.tree.insert_element(11)
		self.assertEqual('[ 12, 10, 5, 11 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_insert_parent_one_child_two_leaf_big(self):
		self.tree.insert_element(12)
		self.tree.insert_element(15)
		self.tree.insert_element(13)
		self.tree.insert_element(16)
		self.assertEqual('[ 12, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_insert_parent_two_children_four_leaf(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(5)
		self.tree.insert_element(11)
		self.tree.insert_element(15)
		self.tree.insert_element(13)
		self.tree.insert_element(16)
		self.assertEqual('[ 12, 10, 5, 11, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_check_hieght_one(self):
		self.tree.insert_element(13)
		self.assertEqual('[ 13 ]', self.tree.pre_order())
		self.assertEqual('[ 13 ]', self.tree.post_order())
		self.assertEqual('[ 13 ]', self.tree.in_order())
		self.assertEqual('[ 13 ]', self.tree.__str__())
		self.assertEqual(1, self.tree.get_height())

	def test_check_height_two(self):
		self.tree.insert_element(14)
		self.tree.insert_element(12)
		self.assertEqual('[ 14, 12 ]', self.tree.pre_order())
		self.assertEqual('[ 12, 14 ]', self.tree.post_order())
		self.assertEqual('[ 12, 14 ]', self.tree.in_order())
		self.assertEqual('[ 12, 14 ]', self.tree.__str__())
		self.assertEqual(2, self.tree.get_height())

	def test_check_height_three(self):
		self.tree.insert_element(14)
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.assertEqual('[ 14, 12, 10 ]', self.tree.pre_order())
		self.assertEqual('[ 10, 12, 14 ]', self.tree.post_order())
		self.assertEqual('[ 10, 12, 14 ]', self.tree.in_order())
		self.assertEqual('[ 10, 12, 14 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_check_height_four(self):
		self.tree.insert_element(14)
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(8)
		self.assertEqual('[ 14, 12, 10, 8 ]', self.tree.pre_order())
		self.assertEqual('[ 8, 10, 12, 14 ]', self.tree.post_order())
		self.assertEqual('[ 8, 10, 12, 14 ]', self.tree.in_order())
		self.assertEqual('[ 8, 10, 12, 14 ]', self.tree.__str__())
		self.assertEqual(4, self.tree.get_height())

	def test_check_height_five(self):
		self.tree.insert_element(14)
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(8)
		self.tree.insert_element(6)
		self.assertEqual('[ 14, 12, 10, 8, 6 ]', self.tree.pre_order())
		self.assertEqual('[ 6, 8, 10, 12, 14 ]', self.tree.post_order())
		self.assertEqual('[ 6, 8, 10, 12, 14 ]', self.tree.in_order())
		self.assertEqual('[ 6, 8, 10, 12, 14 ]', self.tree.__str__())
		self.assertEqual(5, self.tree.get_height())

	def test_check_height_five_then_change_to_six(self):
		self.tree.insert_element(14)
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(8)
		self.tree.insert_element(6)
		self.tree.insert_element(16)
		self.tree.insert_element(18)
		self.tree.insert_element(22)
		self.tree.insert_element(20)
		self.assertEqual('[ 14, 12, 10, 8, 6, 16, 18, 22, 20 ]', self.tree.pre_order())
		self.assertEqual('[ 6, 8, 10, 12, 20, 22, 18, 16, 14 ]', self.tree.post_order())
		self.assertEqual('[ 6, 8, 10, 12, 14, 16, 18, 20, 22 ]', self.tree.in_order())
		self.assertEqual('[ 6, 8, 10, 12, 14, 16, 18, 20, 22 ]', self.tree.__str__())
		self.assertEqual(5, self.tree.get_height())
		self.tree.insert_element(19)
		self.assertEqual('[ 14, 12, 10, 8, 6, 16, 18, 22, 20, 19 ]', self.tree.pre_order())
		self.assertEqual('[ 6, 8, 10, 12, 19, 20, 22, 18, 16, 14 ]', self.tree.post_order())
		self.assertEqual('[ 6, 8, 10, 12, 14, 16, 18, 19, 20, 22 ]', self.tree.in_order())
		self.assertEqual('[ 6, 8, 10, 12, 14, 16, 18, 19, 20, 22 ]', self.tree.__str__())
		self.assertEqual(6, self.tree.get_height())

	def test_height_one_remove(self):
		self.tree.insert_element(10)
		self.assertEqual('[ 10 ]', self.tree.pre_order())
		self.assertEqual('[ 10 ]', self.tree.post_order())
		self.assertEqual('[ 10 ]', self.tree.in_order())
		self.assertEqual('[ 10 ]', self.tree.__str__())
		self.assertEqual(1, self.tree.get_height())
		self.tree.remove_element(10)
		self.assertEqual('[ ]', self.tree.pre_order())
		self.assertEqual('[ ]', self.tree.post_order())
		self.assertEqual('[ ]', self.tree.in_order())
		self.assertEqual('[ ]', self.tree.__str__())
		self.assertEqual(0, self.tree.get_height())

	def test_height_one_remove_head(self):
		self.tree.insert_element(14)
		self.tree.insert_element(12)
		self.assertEqual('[ 14, 12 ]', self.tree.pre_order())
		self.assertEqual('[ 12, 14 ]', self.tree.post_order())
		self.assertEqual('[ 12, 14 ]', self.tree.in_order())
		self.assertEqual('[ 12, 14 ]', self.tree.__str__())
		self.assertEqual(2, self.tree.get_height())
		self.tree.remove_element(14)
		self.assertEqual('[ 12 ]', self.tree.pre_order())
		self.assertEqual('[ 12 ]', self.tree.post_order())
		self.assertEqual('[ 12 ]', self.tree.in_order())
		self.assertEqual('[ 12 ]', self.tree.__str__())
		self.assertEqual(1, self.tree.get_height())

	def test_height_one_remove_leaf_left(self):
		self.tree.insert_element(14)
		self.tree.insert_element(12)
		self.assertEqual('[ 14, 12 ]', self.tree.pre_order())
		self.assertEqual('[ 12, 14 ]', self.tree.post_order())
		self.assertEqual('[ 12, 14 ]', self.tree.in_order())
		self.assertEqual('[ 12, 14 ]', self.tree.__str__())
		self.assertEqual(2, self.tree.get_height())
		self.tree.remove_element(12)
		self.assertEqual('[ 14 ]', self.tree.pre_order())
		self.assertEqual('[ 14 ]', self.tree.post_order())
		self.assertEqual('[ 14 ]', self.tree.in_order())
		self.assertEqual('[ 14 ]', self.tree.__str__())
		self.assertEqual(1, self.tree.get_height())

	def test_height_one_remove_leaf_right(self):
		self.tree.insert_element(14)
		self.tree.insert_element(21)
		self.assertEqual('[ 14, 21 ]', self.tree.pre_order())
		self.assertEqual('[ 21, 14 ]', self.tree.post_order())
		self.assertEqual('[ 14, 21 ]', self.tree.in_order())
		self.assertEqual('[ 14, 21 ]', self.tree.__str__())
		self.assertEqual(2, self.tree.get_height())
		self.tree.remove_element(21)
		self.assertEqual('[ 14 ]', self.tree.pre_order())
		self.assertEqual('[ 14 ]', self.tree.post_order())
		self.assertEqual('[ 14 ]', self.tree.in_order())
		self.assertEqual('[ 14 ]', self.tree.__str__())
		self.assertEqual(1, self.tree.get_height())

	def test_complete_height3_tree_remove_inner_node_left(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(5)
		self.tree.insert_element(11)
		self.tree.insert_element(15)
		self.tree.insert_element(13)
		self.tree.insert_element(16)
		self.assertEqual('[ 12, 10, 5, 11, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())
		self.tree.remove_element(10)
		self.assertEqual('[ 12, 11, 5, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 11, 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 11, 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_complete_height3_tree_remove_inner_node_right(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(5)
		self.tree.insert_element(11)
		self.tree.insert_element(15)
		self.tree.insert_element(13)
		self.tree.insert_element(16)
		self.assertEqual('[ 12, 10, 5, 11, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())
		self.tree.remove_element(15)
		self.assertEqual('[ 12, 10, 5, 11, 16, 13 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 13, 16, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_complete_height3_tree_remove_leaf_node_left1(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(5)
		self.tree.insert_element(11)
		self.tree.insert_element(15)
		self.tree.insert_element(13)
		self.tree.insert_element(16)
		self.assertEqual('[ 12, 10, 5, 11, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())
		self.tree.remove_element(5)
		self.assertEqual('[ 12, 10, 11, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 11, 10, 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 10, 11, 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 10, 11, 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_complete_height3_tree_remove_leaf_node_left2(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(5)
		self.tree.insert_element(11)
		self.tree.insert_element(15)
		self.tree.insert_element(13)
		self.tree.insert_element(16)
		self.assertEqual('[ 12, 10, 5, 11, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())
		self.tree.remove_element(11)
		self.assertEqual('[ 12, 10, 5, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 10, 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_complete_height3_tree_remove_leaf_node_right1(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(5)
		self.tree.insert_element(11)
		self.tree.insert_element(15)
		self.tree.insert_element(13)
		self.tree.insert_element(16)
		self.assertEqual('[ 12, 10, 5, 11, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())
		self.tree.remove_element(16)
		self.assertEqual('[ 12, 10, 5, 11, 15, 13 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 13, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_complete_height3_tree_remove_leaf_node_right2(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(5)
		self.tree.insert_element(11)
		self.tree.insert_element(15)
		self.tree.insert_element(13)
		self.tree.insert_element(16)
		self.assertEqual('[ 12, 10, 5, 11, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())
		self.tree.remove_element(13)
		self.assertEqual('[ 12, 10, 5, 11, 15, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_complete_height3_tree_remove_root(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(5)
		self.tree.insert_element(11)
		self.tree.insert_element(15)
		self.tree.insert_element(13)
		self.tree.insert_element(16)
		self.assertEqual('[ 12, 10, 5, 11, 15, 13, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 13, 16, 15, 12 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 12, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())
		self.tree.remove_element(12)
		self.assertEqual('[ 13, 10, 5, 11, 15, 16 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 11, 10, 16, 15, 13 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 11, 13, 15, 16 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 11, 13, 15, 16 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_remove_from_head_height4_left(self):
		self.tree.insert_element(25)
		self.tree.insert_element(10)
		self.tree.insert_element(5)
		self.tree.insert_element(15)
		self.tree.insert_element(18)
		self.assertEqual('[ 25, 10, 5, 15, 18 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 18, 15, 10, 25 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 15, 18, 25 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 15, 18, 25 ]', self.tree.__str__())
		self.assertEqual(4, self.tree.get_height())
		self.tree.remove_element(25)
		self.assertEqual('[ 10, 5, 15, 18 ]', self.tree.pre_order())
		self.assertEqual('[ 5, 18, 15, 10 ]', self.tree.post_order())
		self.assertEqual('[ 5, 10, 15, 18 ]', self.tree.in_order())
		self.assertEqual('[ 5, 10, 15, 18 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())

	def test_remove_from_head_two_rotations_right(self):
		self.tree.insert_element(12)
		self.tree.insert_element(10)
		self.tree.insert_element(17)
		self.tree.insert_element(14)
		self.tree.insert_element(11)
		self.tree.insert_element(15)
		self.assertEqual('[ 12, 10, 11, 17, 14, 15 ]', self.tree.pre_order())
		self.assertEqual('[ 11, 10, 15, 14, 17, 12 ]', self.tree.post_order())
		self.assertEqual('[ 10, 11, 12, 14, 15, 17 ]', self.tree.in_order())
		self.assertEqual('[ 10, 11, 12, 14, 15, 17 ]', self.tree.__str__())
		self.assertEqual(4, self.tree.get_height())
		self.tree.remove_element(12)
		self.assertEqual('[ 14, 10, 11, 17, 15 ]', self.tree.pre_order())
		self.assertEqual('[ 11, 10, 15, 17, 14 ]', self.tree.post_order())
		self.assertEqual('[ 10, 11, 14, 15, 17 ]', self.tree.in_order())
		self.assertEqual('[ 10, 11, 14, 15, 17 ]', self.tree.__str__())
		self.assertEqual(3, self.tree.get_height())
		

if __name__ == '__main__':
  unittest.main()	