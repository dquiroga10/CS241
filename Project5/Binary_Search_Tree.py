class Binary_Search_Tree:


	class __BST_Node:

		def __init__(self, value):
			self.value = value
			self.right = None
			self.left = None
			self.n_height = 1


		def get_node_height_ins(self):
			if self.right == None and self.left != None:
				self.n_height = self.left.n_height + 1

			elif self.right != None and self.left == None:
				self.n_height = self.right.n_height + 1

			elif self.right != None and self.left != None:

				if self.right.n_height > self.left.n_height:
					self.n_height = self.right.n_height + 1

				else:
					self.n_height = self.left.n_height + 1

		def get_node_height_rem(self):
			if self.right == None and self.left != None:
				self.n_height = self.left.n_height + 1

			elif self.right != None and self.left == None:
				self.n_height = self.right.n_height + 1

			elif self.right != None and self.left != None:

				if self.right.n_height > self.left.n_height:
					self.n_height = self.right.n_height + 1

				else:
					self.n_height = self.left.n_height + 1
			else:
				self.n_height -= 1

	def __init__(self):
		self.__root = None

	def insert_element(self, value):

		x = value
		t = self.__root
		self.__root = self.__rins(x, t)

	def __rins(self, value, position):
	#recursive calls to reach base case
		t = position
		x = value
		if t == None:
			t = Binary_Search_Tree.__BST_Node(x)
			t.get_node_height_ins()
			return t
		if x < t.value:
			t.left = self.__rins(x, t.left)
		if x > t.value:
			t.right = self.__rins(x, t.right)
		if x == t.value:
			raise ValueError
		t.get_node_height_ins()
		return self.__balanced(t)

	def remove_element(self, value):

		x = value
		t = self.__root
		self.__root = self.__rrem(x, t)

	def __rrem(self, value, position):
	#recursive call to remove specific value
		t = position
		x = value
		if t == None:
			raise ValueError

		if t.value == x:
			if t.right == None and t.left == None:
				t.get_node_height_rem()
				return None

			if t.right != None and t.left == None:
				t.get_node_height_rem()
				return t.right

			if t.right == None and t.left != None:
				t.get_node_height_rem()
				return t.left

			if t.right != None and t.left != None:
				pos = t.right
				m = self.__smallest_value(pos)
				t.value = m
				t.right = self.__rrem(m, pos)
				t.get_node_height_rem()
				return t

		if x < t.value:
			t.left = self.__rrem(x, t.left)

		if x > t.value:
			t.right = self.__rrem(x, t.right)

		t.get_node_height_rem()
		return self.__balanced(t)

	def __smallest_value(self, position):
		t = position
		while t.left != None:
			t = t.left
		m = t.value
		return m

	def __balanced(self, position):
		root = position
		t = position
		balance = self.__calc_balance(root)

		if t == None:
			return t

		if balance == -2:
			temp1 = t.left
			balance = self.__calc_balance(temp1)
			if balance == -1 or balance == 0:
				temp = t.left.right
				root = t.left
				root.right = t
				t.left = temp
				if temp != None:
					temp.get_node_height_ins()
				t.get_node_height_rem()
				root.left.get_node_height_ins()
				if t.right == None and t.left == None:
					t.n_height = 1
				root.get_node_height_ins()
				return root

			if balance == 1:  
				root = t.left.right
				temp = root.left
				root.left = t.left
				t.left = root
				root.left.right = temp
				temp = root.right
				root.right = t
				t.left = temp
				if temp != None:
					temp.get_node_height_ins()
				t.get_node_height_ins()
				if t.right == None and t.left == None:
					t.n_height = 1
				root.left.get_node_height_ins()
				if root.left.right == None and root.left.left == None:
					root.left.n_height = 1
				root.get_node_height_ins()
				return root

		if balance == 2: 
			temp1 = t.right
			balance = self.__calc_balance(temp1)
			if balance == 1 or balance == 0: 
				root = t.right
				temp = root.left
				root.left = t
				t.right = temp
				if temp != None:
					temp.get_node_height_ins()
				t.get_node_height_rem()
				root.left.get_node_height_ins()
				if t.right == None and t.left == None:
					t.n_height = 1
				root.get_node_height_ins()
				return root

			if balance == -1:
				root = t.right.left
				temp = root.right
				root.right = t.right
				t.right = root
				root.right.left = temp
				temp = root.left
				root.left = t
				t.right = temp
				if temp != None:
					temp.get_node_height_ins()
				t.get_node_height_ins()
				if t.right == None and t.left == None:
					t.n_height = 1
				root.right.get_node_height_ins()
				if root.right.right == None and root.right.left == None:
					root.right.n_height = 1
				root.get_node_height_ins()
				return root

		return root

	def __calc_balance(self,position):
		t = position
		bal = 0

		if t.left == None and t.right != None:
			bal = int(t.right.n_height)

		if t.right == None and t.left != None:
			bal -= int(t.left.n_height)

		if t.left != None and t.right != None:
			bal = int(t.right.n_height - t.left.n_height)

		if t.left == None and t.right == None:
			bal = 0

		return bal

	def in_order(self):

		if self.__root == None:
			return '[ ]'
		else:
			string = '[ '
			string += self.__rin_order(self.__root)
			string += ' ]'
			return string

	def __rin_order(self, position):
		t = position
		string = ''
		if t.left != None:
			string += self.__rin_order(t.left) + ', '
		string += str(t.value)
		if t.right != None:
			string += ', ' + self.__rin_order(t.right)
		return string

	def pre_order(self):

		if self.__root == None:
			return '[ ]'
		else:
			string = '[ '
			string += self.__rpre_order(self.__root)
			string += ' ]'
			return string

	def __rpre_order(self, position):
		t = position
		string = ''
		string += str(t.value)
		if t.left != None:
			string += ', ' + self.__rpre_order(t.left)
		if t.right != None:
			string += ', ' + self.__rpre_order(t.right)
		return string

	def post_order(self):

		if self.__root == None:
			return '[ ]'
		else:
			string = '[ '
			string += self.__rpost_order(self.__root)
			string += ' ]'
			return string

	def __rpost_order(self, position):
		t = position
		string = ''
		if t.left != None:
			string += self.__rpost_order(t.left) + ', '
		if t.right != None:
			string += self.__rpost_order(t.right) + ', '
		string += str(t.value)
		return string

	def get_height(self):

		if self.__root == None:
			return 0
		else:
			return self.__root.n_height # TODO replace pass with your implementation

	def __str__(self):
		return self.in_order()

	def to_list(self):
		vals = list()
		if self.__root == None:
			return vals
		else:
			vals = self.__rlist(self.__root)
			return vals

	def __rlist(self, t):
		vals = list()
		if t.left != None:
			vals += self.__rlist(t.left)
		vals.append(t.value)
		if t.right != None:
			vals += self.__rlist(t.right)
		return vals

if __name__ == '__main__':
	pass #unit tests make the main section unnecessary.

