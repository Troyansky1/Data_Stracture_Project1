#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left



	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right


	"""sets the parent 

	@rtype: AVLNode
	@param node: a node
	@returns: sets the parent of self
	"""
	def set_parent(self, node):
		self.parent = node

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height

	"""returns the Balance Factor

		@rtype: int
		@returns: height of left - height of right (height is -1 if the node does not exist)
	"""
	def get_BF(self):
		height_right = -1 if self.get_right() is None else self.get_right().get_height()
		height_left = -1 if self.get_left() is None else self.get_left().get_height()
		return height_left - height_right

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		if self.left is None:
			self.left = node
		else:
			print("problem with set left")
		return None


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		if self.right is None:
			self.right = node
		else:
			print("problem with set right")
		return None


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node
		return None


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key
		return None


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value
		return None


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h
		return None


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return False



"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.size = 0

	def req_search(self, node, key):  # not sure if self needed
		if node is not None:
			if node.key == key:
				return node
			elif node.key < key:
				return self.req_search(node.get_right(), key)
			else:
				return self.req_search(node.get_left(), key)
		return None

	"""searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""
	def search(self, key):
		return self.req_search(key, self.root)

	def l_rotate(self, node):
		if node is not None:
			parent = node.get_parent()
			new_root = node.get_right()
			new_root.parent = parent
			child_to_move = new_root.get_left()
			node.set_right(child_to_move)
			new_root.set_left(node)
			# update heights
			return 1

	def r_rotate(self, node):
		if node is not None:
			parent = node.get_parent()
			new_root = node.get_left()
			new_root.parent = parent
			child_to_move = new_root.get_right()
			node.set_left(child_to_move)
			new_root.set_right(node)
			# update heights
			return 1

	def l_r_rotate(self, node):
		self.l_rotate(node.get_left)
		self.r_rotate(node)
		return 2

	def r_l_rotate(self, node):
		self.r_rotate(node.get_right)
		self.l_rotate(node)
		return 2


	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		self.size += 1
		return -1


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		self.size -= 1
		return -1

	def req_avl_to_array(self, node, keys_list):
		if node is not None:
			self.req_avl_to_array(self, node.get_left, keys_list)
			keys_list.append({node.get_key(), node.get_value})
			self.req_avl_to_array(self, node.get_right, keys_list)
		return

	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		keys_list = []
		self.req_avl_to_array(self, self.root, keys_list)
		return keys_list

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.size

	"""splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		#update size
		return None

	
	"""joins self with key and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree2, key, val):
		self.size += tree2.size + 1
		return None


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root