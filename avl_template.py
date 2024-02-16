# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info


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
        height_right = -2 if self.get_right() is None else self.get_right().get_height()
        height_left = -2 if self.get_left() is None else self.get_left().get_height()
        return height_left - height_right

    """sets left child

	@type node: AVLNode
	@param node: a node
	"""

    def set_left(self, node):
        self.left = node
        return None

    """sets right child

	@type node: AVLNode
	@param node: a node
	"""

    def set_right(self, node):
        self.right = node
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

    def recalc_height(self):
        right_height = -2
        left_height = -2
        if self.get_right() is not None:
            right_height = self.get_right().get_height()
        if self.get_left() is not None:
            left_height = self.get_left().get_height()
        self.set_height(max(right_height, left_height) + 1)
        return

    def recalc_height_req(self):
        right_height = 0
        left_height = 0
        if self.get_right() is not None:
            self.get_right().recalc_height_req()
            right_height = self.get_right().get_height()
        if self.get_left() is not None:
            self.get_left().recalc_height_req()
            left_height = self.get_left().get_height()
        self.set_height(max(right_height, left_height) + 1)
        return


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
        return self.key == None


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

    def get_size(self):
        return self.size

    def search(self, key):
        return self.req_search(key, self.root)

    def connect_to_parent(self, node, new_parent):
        node.parent = new_parent
        if new_parent is not None:
            if node.get_key() > new_parent.get_key():
                new_parent.set_right(node)
            else:
                new_parent.set_left(node)
        else:
            self.root = node
        return

    def disconnect_from_parent(self, node):
        parent = node.get_parent()
        if node.get_key() > parent.get_key():
            parent.set_right(None)
        else:
            parent.set_left(None)

    def l_rotate(self, node):
        if node is not None:
            parent = node.get_parent()
            new_root = node.get_right()
            child_to_move = new_root.get_left()
            node.set_right(child_to_move)
            if child_to_move is not None:
                child_to_move.set_parent(node)
            node.recalc_height()
            new_root.set_left(node)
            node.set_parent(new_root)
            new_root.recalc_height()
            self.connect_to_parent(new_root, parent)
            return 1

    def r_rotate(self, node):
        if node is not None:
            parent = node.get_parent()
            new_root = node.get_left()
            child_to_move = new_root.get_right()
            node.set_left(child_to_move)
            if child_to_move is not None:
                child_to_move.set_parent(node)
            node.recalc_height()
            new_root.set_right(node)
            node.set_parent(new_root)
            new_root.recalc_height()
            self.connect_to_parent(new_root, parent)
            return 1

    def l_r_rotate(self, node):
        self.l_rotate(node.get_left)
        self.r_rotate(node)
        return 2

    def r_l_rotate(self, node):
        self.r_rotate(node.get_right)
        self.l_rotate(node)
        return 2

    # TODO double check this, it's very confusing :)
    def get_rotate_func(self, node):
        right = node.get_right()
        right_bf = 0
        left = node.get_left()
        left_bf = 0
        if right is not None:
            right_bf = right.get_BF()
        if left is not None:
            left_bf = left.get_BF()

        if node is not None:
            if node.get_BF() == -2:
                if right_bf == -1 or left_bf == 0:
                    return self.l_rotate
                if right_bf == 1:
                    return self.r_l_rotate

            elif node.get_BF() == 2:
                if left_bf == 1 or right_bf == 0:
                    return self.r_rotate
                if left_bf == -1:
                    return self.r_l_rotate
        return None

    def fix_tree(self, parent, after_insert):
        num_actions = 0
        while parent is not None:
            parent.recalc_height()
            if abs(parent.get_BF()) == 2:
                rotate_func = self.get_rotate_func(parent)
                #print(rotate_func.__name__, "after insert node", node.get_key(), "parent is", parent.get_key())
                num_actions += rotate_func(parent)
                if after_insert:
                    return num_actions
            elif parent.get_BF() == 0:
                return num_actions
            parent = parent.get_parent()
        return num_actions

    def req_insert(self, node, root):
        if node.get_key() > root.get_key():
            if root.get_right() is None:
                root.set_right(node)
                node.set_parent(root)
                root.set_height(root.get_height()+1)
                return
            else:
                self.req_insert(node, root.get_right())
                root.recalc_height()

        elif node.get_key() < root.get_key():
            if root.get_left() is None:
                root.set_left(node)
                root.set_height(root.get_height() + 1)
                node.set_parent(root)
                return
            else:
                self.req_insert(node, root.get_left())
                root.recalc_height()
        return


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
        node = AVLNode(key, val)
        if self.root is None:
            self.root = node
        else:
            self.req_insert(node, self.root)
        self.size += 1
        return self.fix_tree(node.get_parent(), after_insert=True)


    def replace_nodes(self, old_node, new_node):
        old_node.set_value(new_node.get_value())
        old_node.set_key(new_node.get_key())

    def get_min_node(self, root):
        min_node = root
        while min_node.get_left() is not None:  # Find minimum in right subtree
            min_node = min_node.get_left()
        return min_node

    """deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def delete(self, node):
        self.size -= 1
        parent = node.get_parent()
        right = node.get_right()
        left = node.get_left()
        if right is None and left is None:
            self.disconnect_from_parent(node)
            self.fix_tree(parent, False)
        elif left is None and right is not None:
            self.connect_to_parent(right, parent)
            self.fix_tree(parent, False)
        elif left is not None and right is None:
            self.connect_to_parent(left, parent)
            self.fix_tree(parent, False)
        else:
            min_successor = self.get_min_node(right)
            self.replace_nodes(node, min_successor)
            self.connect_to_parent(min_successor.get_right(), min_successor.get_parent())
            self.fix_tree(min_successor.get_right(), False)


        return -1

    def req_avl_to_array(self, node, keys_list):
        if node is not None:
            self.req_avl_to_array(self, node.get_left, keys_list)
            keys_list.append({node.get_key(), node.get_key})
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
        tmp = None
        x = self.root
        stackSmall = []
        stackBig = []
        while x is not None:
            if node.get_key() > x.get_key():
                stackSmall.append(x)
                x = x.get_right()
            if node.get_key() < x.get_key():
                stackBig.append(x)
                x = x.get_left()
            if node.get_key() == x.get_key():
                stackSmall.append(x.get_left())
                stackBig.append(x.get_right())
                x = None  # Exit the while

        minT = stackBig.pop()
        while len(stackBig) != 0:
            tmp = stackBig.pop()
            minT.join(tmp.get_right(), tmp.get_key(), tmp.get_value())
        if tmp is not None:
            minT.fix_tree(tmp, after_insert=False)
        maxT = stackSmall.pop()
        while len(stackSmall) != 0:
            tmp = stackSmall.pop()
            maxT.join(tmp.get_left(), tmp.get_key(), tmp.get_value())
        if tmp is not None:
            maxT.fix_tree(tmp, after_insert=False)
        return [minT, maxT]

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
        self.size += tree2.get_size() + 1
        r = abs(tree2.root.get_height() - self.root.get_height()) + 1
        x = AVLNode(key, val)
        if tree2.root.get_height() > self.root.get_height():
            T1 = self
            T2 = tree2
        else:
            T1 = tree2
            T2 = self
        if T2.root.get_key() > key:  ## then its like the lecturer
            b = T2.get_root()
            h = T1.get_root().get_height()
            c = b
            while b.get_height() > h:
                c = b
                b = b.get_left()
            x.set_left(T1)
            x.set_right(b)
            c.set_right(x)
            self.root = T2.root
        else:  ## T2<x<T1
            x.set_left(T2.get_root())
            x.set_right(T1)
            self.root = x

        self.fix_tree(x, after_insert = False)

        return r

    """returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""

    def get_root(self):
        return self.root
