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

        if key is not None:
            self.height = 0
            self.left = AVLNode(None, None)
            self.right = AVLNode(None, None)

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        if self.is_real_node():
            return self.left
        return None

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        if self.is_real_node():
            return self.right
        return None

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
        if self.is_real_node():
            return self.key
        return 0

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        if self.is_real_node():
            return self.value
        return None

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

    def get_bf(self):
        if self.is_real_node():
            height_right = self.get_right().get_height()
            height_left = self.get_left().get_height()
            return height_left - height_right
        return -1

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node
        node.set_parent(self)
        return None

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node
        node.set_parent(self)
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

    """Recalculates the height of the node, and sets it.

    @rtype: int
    @returns: 1 if the height has been changed, 0 otherwise.
    """
    def recalc_height(self):
        height = self.get_height()
        right_height = self.get_right().get_height()
        left_height = self.get_left().get_height()
        new_height = max(right_height, left_height) + 1
        if new_height != height:
            self.set_height(new_height)
            return 1
        return 0



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
        if self.key is None:
            return False
        return True

    def debug_print_node(self):
        left_val = self.get_left().get_value()
        left_bf = self.get_left().get_bf()
        left_height = self.get_left().get_height()
        right_val = self.get_right().get_value()
        right_bf = self.get_right().get_bf()
        right_height = self.get_right().get_height()
        print("node:", "value:", self.get_value(), "bf:", self.get_bf(), "Height:", self.get_height())
        print("  right:", "value:", right_val, "bf:", right_bf, "height:", right_height, "")
        print("  left:", "value:", left_val, "bf:", left_bf, "height:", left_height, "")




    ## To use in join function in AVLTREE class


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = AVLNode(None, None)
        self.size = 0

    def set_root(self, r):
        self.root = r
        return None

    def get_size(self):
        return self.size

    # A recursive binary search function that search can call. Runs in O(log(n))
    def req_search(self, node, key):
        if node.is_real_node():
            if node.get_key() == key:
                return node
            elif node.get_key() < key:
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
        return self.req_search(self.root, key)

    def connect_to_parent(self, node, new_parent):
        if new_parent is not None:
            if node.get_key() > new_parent.get_key():
                new_parent.set_right(node)
            else:
                new_parent.set_left(node)
        else:
            node.set_parent(new_parent)
            self.root = node
        return

    """Disconnects a node from it's parent, both ways.

    @type node: AVLNode
    @param node: The node to be disconnected
    """
    def disconnect_from_parent(self, node):
        parent = node.get_parent()
        if parent is not None:
            if node.get_key() > parent.get_key():
                parent.set_right(AVLNode(None, None))
            else:
                parent.set_left(AVLNode(None, None))
        else:
            self.root = AVLNode(None, None)

    """Standard AVL left rotation operation.

    @type node: AVLNode
    @param node: The "criminal" node to be rotated
    @rtype: int
    @returns: The number of rebalancing actions needed to be done
    """
    def l_rotate(self, node):
        if node is not None:
            parent = node.get_parent()
            new_root = node.get_right()
            child_to_move = new_root.get_left()
            node.set_right(child_to_move)
            node.recalc_height()
            new_root.set_left(node)
            new_root.recalc_height()
            self.connect_to_parent(new_root, parent)
            return 1

    """Standard AVL right rotation operation.

    @type node: AVLNode
    @param node: The "criminal" node to be rotated
    @rtype: int
    @returns: The number of rebalancing actions needed to be done
    """
    def r_rotate(self, node):
        if node is not None:
            parent = node.get_parent()
            new_root = node.get_left()
            child_to_move = new_root.get_right()
            node.set_left(child_to_move)
            node.recalc_height()
            new_root.set_right(node)
            new_root.recalc_height()
            self.connect_to_parent(new_root, parent)
            return 1

    """Standard AVL left and then right rotation operations.

    @type node: AVLNode
    @param node: The "criminal" node to be rotated
    @rtype: int
    @returns: The number of rebalancing actions needed to be done
    """
    def l_r_rotate(self, node):
        self.l_rotate(node.get_left())
        self.r_rotate(node)
        return 2

    """Standard AVL right and then left rotation operation.

    @type node: AVLNode
    @param node: The "criminal" node to be rotated
    @rtype: int
    @returns: The number of rebalancing actions needed to be done
    """
    def r_l_rotate(self, node):
        self.r_rotate(node.get_right())
        self.l_rotate(node)
        return 2

    """Returns a corresponding rotate function.

    @type node: AVLNode
    @param node: The node with a balance factor of |2|
    @rtype: function
    @returns: The corresponding rotate function to be applied on the node.
    """
    def get_rotate_func(self, node):
        right = node.get_right()
        left = node.get_left()
        right_bf = right.get_bf()
        left_bf = left.get_bf()
        if node is not None:
            if node.get_bf() == -2:
                if right_bf == 1:
                    return self.r_l_rotate
                if right_bf == -1 or right_bf == 0:
                    return self.l_rotate

            elif node.get_bf() == 2:
                if left_bf == -1:
                    return self.l_r_rotate
                if left_bf == 1 or left_bf == 0:
                    return self.r_rotate

        node.debug_print_node()
        return None

    """Climbs up the tree and searches for criminals. Applies rotations as needed.
    Runs in O(log(n))- as the max height of the tree.

    @type node: AVLNode
    @param node: The node which the search should begin with
    @type after_insert: Boolean
    @param after_insert: True if we are fixing after insert- for optimizations.
    @rtype: int
    @returns: The number of rotations which were performed overall
    """
    def fix_tree(self, node, after_insert):
        num_actions = 0
        while node is not None and node.is_real_node():
            num_actions += node.recalc_height()
            parent = node.get_parent()
            if abs(node.get_bf()) == 2:
                rotate_func = self.get_rotate_func(node)
                # print(rotate_func.__name__, "parent is", parent.get_key())
                num_actions += rotate_func(node)
            node = parent

        return num_actions

    # A recursive insert function that insert can call. Runs in O(log(n))
    def req_insert(self, node, root):
        num_actions = 0
        # Searching the right subtree
        if node.get_key() > root.get_key():
            # Can insert here
            if not root.get_right().is_real_node():
                root.set_right(node)
                root.set_height(root.get_height()+1)
                num_actions += 1
                return num_actions
            # Continue the search recursively
            else:
                num_actions += self.req_insert(node, root.get_right())
                num_actions += root.recalc_height()
        # Searching the left subtree
        elif node.get_key() < root.get_key():
            # Can insert here
            if not root.get_left().is_real_node():
                root.set_left(node)
                root.set_height(root.get_height() + 1)
                num_actions += 1
                return num_actions
            # Continue the search recursively
            else:
                num_actions += self.req_insert(node, root.get_left())
                num_actions += root.recalc_height()
        return num_actions


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
        num_actions = 0
        node = AVLNode(key, val)
        # If the tree is empty insert to the root.
        if not self.root.is_real_node():
            self.root = node
        # Call recursive insert on the root.
        else:
            num_actions += self.req_insert(node, self.root)
        self.size += 1
        # Fix the tree from the location of the inserted node and get the number of actions needed.
        num_actions += self.fix_tree(node.get_parent(), after_insert=True)
        return num_actions

    """ Takes the values (key and val) from the new node and sets in the place of the old node. Replace in-place.

       @type old_node: AVLNode
       @param old_node: The old node
       @type new_node: AVLNode
       @param new_node: the new node
       """
    def replace_nodes(self, old_node, new_node):
        old_node.set_value(new_node.get_value())
        old_node.set_key(new_node.get_key())

    """ gets the minimus successor

    @type root: AVLNode
    @param root: The node from which to search the minimus
    @rtype: AVLNode
    @returns: The minimum successor
    """
    def get_min_node(self, root):
        min_node = root
        # Find minimum in right subtree
        while min_node.get_left().is_real_node():
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
        # Node to delete has no children
        if not right.is_real_node() and not left.is_real_node():
            self.disconnect_from_parent(node)
            num_actions = self.fix_tree(parent, False)
        # Node to delete has no left child
        elif not left.is_real_node() and right.is_real_node():
            self.connect_to_parent(right, parent)
            num_actions = self.fix_tree(parent, False)
        # Node to delete has no right child
        elif left.is_real_node() and not right.is_real_node():
            self.connect_to_parent(left, parent)
            num_actions = self.fix_tree(parent, False)
        # Node to delete has both children
        else:
            # Replaces with the minimun successor
            min_successor = self.get_min_node(right)
            self.replace_nodes(node, min_successor)
            # Connect the min successor's successors to the new place.
            self.connect_to_parent(min_successor.get_right(), min_successor.get_parent())
            # Fix the tree from the location of the parent of the node wich replaced the deleted node.
            num_actions = self.fix_tree(min_successor.get_parent(), False)
        return num_actions

    # A recursive avl_to_array function that avl_to_array can call.
    def req_avl_to_array(self, node, keys_list):
        if node.is_real_node():
            self.req_avl_to_array(node.get_left(), keys_list)
            keys_list.append((node.get_key(), node.get_value()))
            self.req_avl_to_array(node.get_right(), keys_list)
        return

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        keys_list = []
        self.req_avl_to_array(self.root, keys_list)
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
        tmp_tree = AVLTree()
        x = self.root
        stack_smaller_than_x = []
        stack_bigger_than_x= []
        while x is not None:
            if node.get_key() > x.get_key():
                stack_smaller_than_x.append(x)
                x = x.get_right()
            elif node.get_key() < x.get_key():
                stack_bigger_than_x.append(x)
                x = x.get_left()
            elif node.get_key() == x.get_key():
                if x.get_left().is_real_node():
                    stack_smaller_than_x.append(x.get_left())
                if x.get_right().is_real_node():
                    stack_bigger_than_x.append(x.get_right())
                x = None  # Exit the while

        minT = AVLTree()
        while len(stack_bigger_than_x) != 0:
            tmp = stack_bigger_than_x.pop()
            tmp_tree.set_root(tmp.get_right())
            minT.join(tmp_tree, tmp.get_key(), tmp.get_value())

        minT.fix_tree(tmp, after_insert=False)
        maxT = AVLTree()
        while len(stack_smaller_than_x) != 0:
            tmp = stack_smaller_than_x.pop()
            tmp_tree.set_root(tmp.get_left())
            maxT.join(tmp_tree, tmp.get_key(), tmp.get_value())


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
        r = abs(tree2.get_root().get_height() - self.root.get_height()) + 1
        x = AVLNode(key, val)
        if tree2.get_root().get_height() > self.root.get_height():
            T1 = self
            T2 = tree2
        else:
            T1 = tree2
            T2 = self
        # If true going down the left (smaller) tree
        if T2.get_root().get_key() > key:
            # If T1 is a leaf
            if not T1.get_root().is_real_node(): # TODO check if we can just insert...
                T2.insert(key, val)
            else:
                b = T2.get_root()
                h = T1.get_root().get_height()
                # Going down the tree until the height of b is no more than h
                while b.get_height() > h:
                    b = b.get_left()
                c = b.get_parent()
                x.set_left(T1.get_root())
                T1.get_root().set_parent(x)
                x.set_right(b)
                b.set_parent(x)
                # If B is not the root of T2
                if c is not None:
                    c.set_left(x)
                    x.set_parent(c)
                    self.root = T2.get_root()
                else:
                    self.root = x
        # Going down the right (bigger) tree
        else:  ## T2<x<T1   h(T2)> h(T1)
            if not T1.get_root().is_real_node():
                T2.insert(key, val)
            else:
                b = T2.get_root()
                h = T1.get_root().get_height()
                # Going down the tree until the height of b is no more than h
                while b.get_height() > h:
                    b = b.get_right()
                c = b.get_parent()
                x.set_right(T1.get_root())
                T1.get_root().set_parent(x)
                x.set_left(b)
                b.set_parent(x)
                if c is not b:
                    c.set_right(x)
                    x.set_parent(c)
                    self.root = T2.get_root()
                else:
                    self.root = x

        self.fix_tree(x, after_insert = False)

        return r

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root
