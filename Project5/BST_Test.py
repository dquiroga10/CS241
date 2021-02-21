import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BSTTester(unittest.TestCase):

  def setUp(self):
    self.tree = Binary_Search_Tree()

  def test_empty_tree_in_order(self):
    self.assertEqual('[ ]', self.tree.in_order())

  def test_empty_tree_pre_order(self):
    self.assertEqual('[ ]', self.tree.pre_order())

  def test_empty_tree_post_order(self):
    self.assertEqual('[ ]', self.tree.post_order())

  def test_empty_tree_str(self):
    self.assertEqual('[ ]', self.tree.__str__())

  def test_empty_tree_height(self):
    self.assertEqual(0, self.tree.get_height())

  def test_one_insert_in_order(self):
    self.tree.insert_element(5)
    self.assertEqual('[ 5 ]', self.tree.in_order())

  def test_one_insert_pre_order(self):
    self.tree.insert_element(5)
    self.assertEqual('[ 5 ]', self.tree.pre_order())

  def test_one_insert_post_order(self):
    self.tree.insert_element(5)
    self.assertEqual('[ 5 ]', self.tree.post_order())

  def test_one_insert_str(self):
    self.tree.insert_element(5)
    self.assertEqual('[ 5 ]', self.tree.__str__())

  def test_one_insert_height(self):
    self.tree.insert_element(5)
    self.assertEqual(1, self.tree.get_height())

  def test_one_small_child_in_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.assertEqual('[ 3, 5 ]', self.tree.in_order())

  def test_one_small_child_pre_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.assertEqual('[ 5, 3 ]', self.tree.pre_order())

  def test_one_small_child_post_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.assertEqual('[ 3, 5 ]', self.tree.post_order())

  def test_one_small_child_str(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.assertEqual('[ 3, 5 ]', self.tree.__str__())

  def test_one_small_child_height(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.assertEqual(2, self.tree.get_height())

  def test_one_big_child_in_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.assertEqual('[ 5, 8 ]', self.tree.in_order())

  def test_one_big_child_pre_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.assertEqual('[ 5, 8 ]', self.tree.pre_order())

  def test_one_big_child_post_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.assertEqual('[ 8, 5 ]', self.tree.post_order())

  def test_one_big_child_str(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.assertEqual('[ 5, 8 ]', self.tree.__str__())

  def test_one_big_child_height(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.assertEqual(2, self.tree.get_height())

  def test_one_parent_two_children_in_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.tree.insert_element(8)
    self.assertEqual('[ 3, 5, 8 ]', self.tree.in_order())

  def test_one_parent_two_children_pre_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.tree.insert_element(8)
    self.assertEqual('[ 5, 3, 8 ]', self.tree.pre_order())

  def test_one_parent_two_children_post_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.tree.insert_element(8)
    self.assertEqual('[ 3, 8, 5 ]', self.tree.post_order())

  def test_one_parent_two_children_str(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.tree.insert_element(8)
    self.assertEqual('[ 3, 5, 8 ]', self.tree.__str__())

  def test_one_parent_two_children_height(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.tree.insert_element(8)
    self.assertEqual(2, self.tree.get_height())

  def test_one_parent_one_big_child_two_leaf_in_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.insert_element(7)
    self.tree.insert_element(10)
    self.assertEqual('[ 5, 7, 8, 10 ]', self.tree.in_order())

  def test_one_parent_one_big_child_two_leaf_pre_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.insert_element(7)
    self.tree.insert_element(10)
    self.assertEqual('[ 7, 5, 8, 10 ]', self.tree.pre_order())

  def test_one_parent_one_big_child_two_leaf_post_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.insert_element(7)
    self.tree.insert_element(10)
    self.assertEqual('[ 5, 10, 8, 7 ]', self.tree.post_order())

  def test_one_parent_one_big_child_two_leaf_str(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.insert_element(7)
    self.tree.insert_element(10)
    self.assertEqual('[ 5, 7, 8, 10 ]', self.tree.__str__())

  def test_one_parent_one_big_child_two_leaf_height(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.insert_element(7)
    self.tree.insert_element(10)
    self.assertEqual(3, self.tree.get_height())

  def test_one_parent_one_small_child_two_leaf_in_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(7)
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.assertEqual('[ 5, 7, 8, 10 ]', self.tree.in_order())

  def test_one_parent_one_small_child_two_leaf_pre_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(7)
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.assertEqual('[ 7, 5, 10, 8 ]', self.tree.pre_order())

  def test_one_parent_one_small_child_two_leaf_post_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(7)
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.assertEqual('[ 5, 8, 10, 7 ]', self.tree.post_order())

  def test_one_parent_one_small_child_two_leaf_str(self):
    self.tree.insert_element(10)
    self.tree.insert_element(7)
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.assertEqual('[ 5, 7, 8, 10 ]', self.tree.__str__())

  def test_one_parent_one_small_child_two_leaf_height(self):
    self.tree.insert_element(10)
    self.tree.insert_element(7)
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.assertEqual(3, self.tree.get_height())

  def test_one_parent_two_children_four_leaf_in_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.assertEqual('[ 5, 8, 9, 10, 11, 13, 14 ]', self.tree.in_order())

  def test_one_parent_two_children_four_leaf_pre_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.assertEqual('[ 10, 8, 5, 9, 13, 11, 14 ]', self.tree.pre_order())

  def test_one_parent_two_children_four_leaf_post_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.assertEqual('[ 5, 9, 8, 11, 14, 13, 10 ]', self.tree.post_order())

  def test_one_parent_two_children_four_leaf_str(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.assertEqual('[ 5, 8, 9, 10, 11, 13, 14 ]', self.tree.__str__())

  def test_one_parent_two_children_four_leaf_height(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.assertEqual(3, self.tree.get_height())

  def test_insert_one_remove_one_in_order(self):
    self.tree.insert_element(5)
    self.tree.remove_element(5)
    self.assertEqual('[ ]', self.tree.in_order())

  def test_insert_one_remove_one_pre_order(self):
    self.tree.insert_element(5)
    self.tree.remove_element(5)
    self.assertEqual('[ ]', self.tree.pre_order())

  def test_insert_one_remove_one_post_order(self):
    self.tree.insert_element(5)
    self.tree.remove_element(5)
    self.assertEqual('[ ]', self.tree.post_order())

  def test_insert_one_remove_one_str(self):
    self.tree.insert_element(5)
    self.tree.remove_element(5)
    self.assertEqual('[ ]', self.tree.__str__())

  def test_insert_one_remove_one_height(self):
    self.tree.insert_element(5)
    self.tree.remove_element(5)
    self.assertEqual(0, self.tree.get_height())

  def test_insert_two_remove_root_in_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.remove_element(5)
    self.assertEqual('[ 8 ]', self.tree.in_order())

  def test_insert_two_remove_root_pre_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.remove_element(5)
    self.assertEqual('[ 8 ]', self.tree.pre_order())

  def test_insert_two_remove_root_post_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.remove_element(5)
    self.assertEqual('[ 8 ]', self.tree.post_order())

  def test_insert_two_remove_root_str(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.remove_element(5)
    self.assertEqual('[ 8 ]', self.tree.__str__())

  def test_insert_two_remove_root_height(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.remove_element(5)
    self.assertEqual(1, self.tree.get_height())

  def test_insert_two_remove_right_leaf_in_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.remove_element(8)
    self.assertEqual('[ 5 ]', self.tree.in_order())

  def test_insert_two_remove_right_leaf_pre_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.remove_element(8)
    self.assertEqual('[ 5 ]', self.tree.pre_order())

  def test_insert_two_remove_right_leaf_post_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.remove_element(8)
    self.assertEqual('[ 5 ]', self.tree.post_order())

  def test_insert_two_remove_right_leaf_str(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.remove_element(8)
    self.assertEqual('[ 5 ]', self.tree.__str__())

  def test_insert_two_remove_right_leaf_height(self):
    self.tree.insert_element(5)
    self.tree.insert_element(8)
    self.tree.remove_element(8)
    self.assertEqual(1, self.tree.get_height())

  def test_insert_two_remove_left_leaf_in_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.tree.remove_element(3)
    self.assertEqual('[ 5 ]', self.tree.in_order())

  def test_insert_two_remove_left_leaf_pre_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.tree.remove_element(3)
    self.assertEqual('[ 5 ]', self.tree.pre_order())

  def test_insert_two_remove_left_leaf_post_order(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.tree.remove_element(3)
    self.assertEqual('[ 5 ]', self.tree.post_order())

  def test_insert_two_remove_left_leaf_str(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.tree.remove_element(3)
    self.assertEqual('[ 5 ]', self.tree.__str__())

  def test_insert_two_remove_left_leaf_height(self):
    self.tree.insert_element(5)
    self.tree.insert_element(3)
    self.tree.remove_element(3)
    self.assertEqual(1, self.tree.get_height())

  def test_one_parent_two_children_four_leaf_remove_leaf1_in_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(5)
    self.assertEqual('[ 8, 9, 10, 11, 13, 14 ]', self.tree.in_order())

  def test_one_parent_two_children_four_leaf_remove_leaf1_pre_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(5)
    self.assertEqual('[ 10, 8, 9, 13, 11, 14 ]', self.tree.pre_order())

  def test_one_parent_two_children_four_leaf_remove_leaf1_post_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(5)
    self.assertEqual('[ 9, 8, 11, 14, 13, 10 ]', self.tree.post_order())

  def test_one_parent_two_children_four_leaf_remove_leaf1_str(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(5)
    self.assertEqual('[ 8, 9, 10, 11, 13, 14 ]', self.tree.__str__())

  def test_one_parent_two_children_four_leaf_remove_leaf1_height(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(5)
    self.assertEqual(3, self.tree.get_height())

  def test_one_parent_two_children_four_leaf_remove_leaf2_in_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(9)
    self.assertEqual('[ 5, 8, 10, 11, 13, 14 ]', self.tree.in_order())

  def test_one_parent_two_children_four_leaf_remove_leaf2_pre_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(9)
    self.assertEqual('[ 10, 8, 5, 13, 11, 14 ]', self.tree.pre_order())

  def test_one_parent_two_children_four_leaf_remove_leaf2_post_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(9)
    self.assertEqual('[ 5, 8, 11, 14, 13, 10 ]', self.tree.post_order())

  def test_one_parent_two_children_four_leaf_remove_leaf2_str(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(9)
    self.assertEqual('[ 5, 8, 10, 11, 13, 14 ]', self.tree.__str__())

  def test_one_parent_two_children_four_leaf_remove_leaf2_height(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(9)
    self.assertEqual(3, self.tree.get_height())

  def test_one_parent_two_children_four_leaf_remove_leaf3_in_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(11)
    self.assertEqual('[ 5, 8, 9, 10, 13, 14 ]', self.tree.in_order())

  def test_one_parent_two_children_four_leaf_remove_leaf3_pre_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(11)
    self.assertEqual('[ 10, 8, 5, 9, 13, 14 ]', self.tree.pre_order())

  def test_one_parent_two_children_four_leaf_remove_leaf3_post_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(11)
    self.assertEqual('[ 5, 9, 8, 14, 13, 10 ]', self.tree.post_order())

  def test_one_parent_two_children_four_leaf_remove_leaf3_str(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(11)
    self.assertEqual('[ 5, 8, 9, 10, 13, 14 ]', self.tree.__str__())

  def test_one_parent_two_children_four_leaf_remove_leaf3_height(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(11)
    self.assertEqual(3, self.tree.get_height())

  def test_one_parent_two_children_four_leaf_remove_leaf4_in_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(14)
    self.assertEqual('[ 5, 8, 9, 10, 11, 13 ]', self.tree.in_order())

  def test_one_parent_two_children_four_leaf_remove_leaf4_pre_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(14)
    self.assertEqual('[ 10, 8, 5, 9, 13, 11 ]', self.tree.pre_order())

  def test_one_parent_two_children_four_leaf_remove_leaf4_post_order(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(14)
    self.assertEqual('[ 5, 9, 8, 11, 13, 10 ]', self.tree.post_order())

  def test_one_parent_two_children_four_leaf_remove_leaf4_str(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(14)
    self.assertEqual('[ 5, 8, 9, 10, 11, 13 ]', self.tree.__str__())

  def test_one_parent_two_children_four_leaf_remove_leaf4_height(self):
    self.tree.insert_element(10)
    self.tree.insert_element(8)
    self.tree.insert_element(5)
    self.tree.insert_element(9)
    self.tree.insert_element(13)
    self.tree.insert_element(11)
    self.tree.insert_element(14)
    self.tree.remove_element(14)
    self.assertEqual(3, self.tree.get_height())

if __name__ == '__main__':
  unittest.main()


  



  


    

    


    






    



    