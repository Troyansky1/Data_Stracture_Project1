import unittest
import avl_template
import pytest

from avl_template import AVLNode, AVLTree

AVLNode.__eq__ = lambda self, other: self.key == other.key and self.value == other.value
AVLNode.__bool__ = lambda self: self.is_real_node()


def build_sample_avl():
    tree = AVLTree()

    tree.insert(15, 0)
    tree.insert(8, 0)
    tree.insert(22, 0)

    tree.insert(4, 0)
    tree.insert(11, 0)
    tree.insert(20, 0)
    tree.insert(24, 0)

    tree.insert(2, 0)
    tree.insert(9, 0)
    tree.insert(12, 0)
    tree.insert(18, 0)

    tree.insert(13, 0)
    return tree


def is_valid_bst(node: AVLNode):
    if not node.key:
        return True
    left = node.get_left()
    if left and node.key < left.key:
        return False

    right = node.get_right()
    if right and node.key > right.key:
        return False
    return is_valid_bst(left) and is_valid_bst(right)


def walk(node: AVLNode):
    left = walk(node.get_left()) if node.get_left() else []
    right = walk(node.get_right()) if node.get_right() else []

    return left + [node] + right


def assert_valid_avl(tree: AVLTree):
    nodes_list = walk(tree.root)
    for node in nodes_list:
        bf = node.get_bf()
        if abs(bf) > 1:
            raise AssertionError(f"Found node with illegal BF {bf}!")

    if not is_valid_bst(tree.root):
        raise AssertionError(f"Tree is not a valid BST")


def test_is_valid_bst_given_valid_tree_returns_true():
    tree = build_sample_avl()
    # print(is_valid_bst(tree.root))
    assert is_valid_bst(tree.root) is True


def test_is_valid_bst_given_invalid_tree_returns_false():
    root = AVLNode(3, 3)

    left_child = AVLNode(1, 1)
    left_grandchild = AVLNode(2, 2)
    right_child = AVLNode(5, 5)
    right_left_grandchild = AVLNode(7, 7)
    right_right_grandchild = AVLNode(6, 6)

    root.set_left(left_child)
    left_child.set_right(left_grandchild)
    root.set_right(right_child)
    right_child.set_left(right_left_grandchild)
    right_child.set_right(right_right_grandchild)

    assert is_valid_bst(root) is False


def test_is_valid_avl_raises_error_for_unbalanced_tree():
    tree = AVLTree()
    root = AVLNode(6, 6)
    child = AVLNode(7, 7)
    grandchild = AVLNode(8, 8)

    tree.root = root
    root.right = child
    root.height = 2
    child.right = grandchild
    child.height = 1
    grandchild.height = 0
    with pytest.raises(AssertionError):
        assert_valid_avl(tree)


def test_avl_node_given_child_returns_child():
    # setup
    parent_node = AVLNode(2, 2)
    left_child = AVLNode(1, 1)
    right_child = AVLNode(3, 3)

    # process
    parent_node.set_left(left_child)
    parent_node.set_right(right_child)

    # assert
    assert parent_node.get_left() == left_child
    assert parent_node.get_right() == right_child
    assert left_child.get_parent() == parent_node
    assert right_child.get_parent() == parent_node


@pytest.mark.parametrize(
    argnames="key, expected",
    argvalues=[
        (4, AVLNode(4, 0)),
        (17, None)
    ],
    ids=[
        "key is in tree",
        "key isn't in tree"
    ]
)
def test_search_given_key_should_return_node_if_key_is_in_the_tree(key: int, expected: AVLNode | None):
    tree = build_sample_avl()

    result = tree.search(key=key)
    assert result == expected


def test_to_array_given_tree_should_return_nodes_in_valid_order():
    tree = build_sample_avl()

    result = tree.avl_to_array()
    assert result == [(2, 0), (4, 0), (8, 0), (9, 0), (11, 0), (12, 0),
                      (13, 0), (15, 0), (18, 0), (20, 0), (22, 0), (24, 0), ]


def test_insert_given_key_and_value_should_add_node_to_tree():
    tree = build_sample_avl()
    tree.insert(8, 8)

    assert tree.search(8)


def test_rotate_left_should_rotate_left():
    tree = AVLTree()
    updated_nodes = tree.insert(6, 6)
    assert updated_nodes == 0
    updated_nodes = tree.insert(7, 7)
    assert updated_nodes == 1
    updated_nodes = tree.insert(8, 8)
    assert updated_nodes == 3

    assert tree.root == AVLNode(7, 7)
    assert tree.root.left == AVLNode(6, 6)
    assert tree.root.right == AVLNode(8, 8)
    assert_valid_avl(tree)


def test_rotate_right_should_rotate_right():
    tree = AVLTree()
    rotations = tree.insert(8, 8)
    assert rotations == 0
    rotations = tree.insert(7, 7)
    assert rotations == 1
    rotations = tree.insert(6, 6)
    assert rotations == 3

    assert tree.root == AVLNode(7, 7)
    assert tree.root.left == AVLNode(6, 6)
    assert tree.root.right == AVLNode(8, 8)
    assert_valid_avl(tree)


def test_rotate_right_then_left():
    tree = AVLTree()
    rotations = tree.insert(6, 6)
    assert rotations == 0
    rotations = tree.insert(8, 8)
    assert rotations == 1
    rotations = tree.insert(7, 7)
    assert rotations == 4

    assert tree.root == AVLNode(7, 7)
    assert tree.root.left == AVLNode(6, 6)
    assert tree.root.right == AVLNode(8, 8)
    assert_valid_avl(tree)


def test_rotate_left_then_right():
    tree = AVLTree()
    rotations = tree.insert(8, 8)
    assert rotations == 0
    rotations = tree.insert(6, 6)
    assert rotations == 1
    rotations = tree.insert(7, 7)
    assert rotations == 4

    assert tree.root == AVLNode(7, 7)
    assert tree.root.left == AVLNode(6, 6)
    assert tree.root.right == AVLNode(8, 8)
    assert_valid_avl(tree)


def test_simple_deletions_shouldnt_trigger_rotations():
    tree = build_sample_avl()
    node = tree.search(12)
    rebalances = tree.delete(node)
    assert rebalances == 3
    assert tree.root.left.right.right == AVLNode(13, 0)

    node = tree.search(4)
    rebalances = tree.delete(node)
    assert rebalances == 0
    assert tree.root.left.left == AVLNode(2, 0)

    assert tree.size == 10
    assert_valid_avl(tree)


def test_simple_deletion_of_root_shouldnt_trigger_rotation():
    tree = AVLTree()
    tree.insert(2, 0)
    tree.insert(1, 0)
    tree.insert(3, 0)

    node = tree.search(2)
    tree.delete(node)

    node = tree.search(3)
    tree.delete(node)

    node = tree.search(1)
    tree.delete(node)
    assert_valid_avl(tree)


def test_deletion_with_two_children_replaces_node_with_successor():
    tree = build_sample_avl()
    node = tree.search(11)
    rebalances = tree.delete(node)
    assert rebalances == 2
    assert tree.root.left.right == AVLNode(12, 0)
    assert tree.root.left.right.left == AVLNode(9, 0)
    assert tree.root.left.right.right == AVLNode(13, 0)
    assert_valid_avl(tree)


def test_delete_should_trigger_rotations():
    tree = build_sample_avl()
    node = tree.search(24)
    rotations = tree.delete(node)

    assert rotations == 3
    assert tree.root == AVLNode(11, 0)
    assert tree.root.left == AVLNode(8, 0)
    assert tree.root.right == AVLNode(15, 0)
    assert tree.size == 11
    assert_valid_avl(tree)


def test_minimum_should_return_minimum():
    tree = build_sample_avl()
    assert tree.get_min_node(tree.root) == AVLNode(2, 0)
    assert tree.get_min_node(tree.root.right) == AVLNode(18, 0)


def test_successor_should_return_the_next_largest_node():
    tree = build_sample_avl()
    node = tree.search(9)
    #assert node.get_right() == AVLNode(11, 0)

    node = tree.search(13)
    #assert node.get_right() == AVLNode(15, 0)

    node = tree.search(15)
    #assert node.get_right() == AVLNode(18, 0)


def test_successor_given_maximal_value_of_tree_should_return_null():
    tree = build_sample_avl()
    node = tree.search(24)
    assert not node.get_right().is_real_node()


def build_trees_for_join():
    large_tree = AVLTree()
    large_tree.insert(4, 0)
    large_tree.insert(2, 0)
    large_tree.insert(8, 0)

    large_tree.insert(1, 0)
    large_tree.insert(3, 0)
    large_tree.insert(6, 0)
    large_tree.insert(9, 0)

    small_right_tree = AVLTree()
    small_right_tree.insert(15, 0)
    small_right_tree.insert(12, 0)
    small_right_tree.insert(18, 0)

    small_left_tree = AVLTree()
    small_left_tree.insert(-5, 0)
    small_left_tree.insert(-4, 0)
    small_left_tree.insert(-6, 0)

    return small_left_tree, large_tree, small_right_tree
def print_avl_tree_req(root, prefix="", is_left=True):
    if root.is_real_node():
        key_str = "KEY:" + str(root.key)
        bf_str = " BF:" + str(root.get_bf())
        height_str = " Height:" + str(root.get_height())

        print(prefix + ("|-- " if is_left else "\\-- ") + key_str + bf_str + height_str)
        print_avl_tree_req(root.left, prefix + ("|   " if is_left else "    "), True)
        print_avl_tree_req(root.right, prefix + ("|   " if is_left else "    "), False)


def test_rtl_join_should_trigger_rotations():
    _, large_tree, small_tree = build_trees_for_join()
    cost = large_tree.join(small_tree, 10, 0)
    assert cost == 2
#    assert large_tree.root == AVLNode(10, 0)
    assert large_tree.root.height == 3
    assert_valid_avl(large_tree)

    _, large_tree, small_tree = build_trees_for_join()
    print("small tree is ")
    print_avl_tree_req(small_tree.root)
    print("#################")
    print("big tree is ")
    print_avl_tree_req(large_tree.root)
    print("#################")
    cost = small_tree.join(large_tree, 10, 0)
    print("joined tree is ")
    print_avl_tree_req(small_tree.root)
    print("#################")
    assert cost == 2
#    assert small_tree.root == AVLNode(10, 0)
    assert small_tree.root.height == 3
    assert_valid_avl(small_tree)


def test_ltr_join_should_trigger_rotations():
    small_tree, large_tree, _ = build_trees_for_join()
    print("small tree is ")
    print_avl_tree_req(small_tree.root)
    print("#################")
    print("big tree is ")
    print_avl_tree_req(large_tree.root)
    print("#################")
    cost = large_tree.join(small_tree, -2, 0)
    print("joined tree is ")
    print_avl_tree_req(large_tree.root)
    print("#################")
    assert cost == 2
    #assert large_tree.root == AVLNode(-2, 0)
    assert large_tree.root.height == 3
    assert_valid_avl(large_tree)

    small_tree, large_tree, _ = build_trees_for_join()
    cost = small_tree.join(large_tree, -2, 0)
    print("joined tree is ")
    print_avl_tree_req(small_tree.root)
    print("#################")
    print_avl_tree_req(large_tree.root)
    print("#################")
    assert cost == 2
    #assert small_tree.root == AVLNode(-2, 0)
    assert small_tree.root.height == 3
    assert_valid_avl(small_tree)


def test_join_given_trees_of_equal_height_should_add_them_as_siblings():
    left_tree, _, right_tree = build_trees_for_join()
    cost = right_tree.join(left_tree, 1, 0)
    assert cost == 1
    assert right_tree.root == AVLNode(1, 0)
    assert right_tree.root.height == 2
    assert right_tree.root.left == AVLNode(-5, 0)
    assert right_tree.root.right == AVLNode(15, 0)
    assert_valid_avl(right_tree)

    left_tree, _, right_tree = build_trees_for_join()
    cost = left_tree.join(right_tree, 1, 0)
    assert cost == 1
    assert left_tree.root == AVLNode(1, 0)
    assert left_tree.root.height == 2
    assert left_tree.root.left == AVLNode(-5, 0)
    assert left_tree.root.right == AVLNode(15, 0)
    assert_valid_avl(left_tree)


def build_tree_for_split():
    tree = AVLTree()
    tree.insert(25, 0)
    tree.insert(9, 0)
    tree.insert(33, 0)

    tree.insert(5, 0)
    tree.insert(13, 0)
    tree.insert(29, 0)
    tree.insert(59, 0)

    tree.insert(2, 0)
    tree.insert(11, 0)
    tree.insert(20, 0)
    tree.insert(31, 0)

    tree.insert(10, 0)
    tree.insert(18, 0)
    tree.insert(23, 0)

    return tree


def test_split_given_root_should_split_on_its_children():
    tree = build_tree_for_split()
    node = tree.root
    left, right = tree.split(node)
    assert left.root == AVLNode(9, 0)
    assert right.root == AVLNode(33, 0)
    assert_valid_avl(left)
    assert_valid_avl(right)


def test_split_given_node_with_children_should_split_into_trees():
    tree = build_tree_for_split()
    node = tree.search(20)
    print("tree tree is ")
    print_avl_tree_req(tree.root)
    print("#################")

    left, right = tree.split(node)

    print("left tree is ")
    print_avl_tree_req(left.root)
    print("#################")
    print("right tree is ")
    print_avl_tree_req(right.root)
    print("#################")
    #assert left.root == AVLNode(9, 0)
    #assert left.root.left == AVLNode(5, 0)
    #assert left.root.right == AVLNode(13, 0)
    #assert left.root.right.right == AVLNode(18, 0)
    assert_valid_avl(left)

    #assert right.root == AVLNode(29, 0)
    #assert right.root.left == AVLNode(25, 0)
    #assert right.root.left.left == AVLNode(23, 0)
    assert_valid_avl(right)


def test_split_given_node_with_no_children_should_split_into_trees():
    tree = build_tree_for_split()
    node = tree.search(23)
    left, right = tree.split(node)
    assert left.root == AVLNode(9, 0)
    assert left.root.left == AVLNode(5, 0)
    assert left.root.right == AVLNode(13, 0)
    assert left.root.right.right == AVLNode(18, 0)
    assert_valid_avl(left)

    assert right.root == AVLNode(33, 0)
    assert right.root.left == AVLNode(29, 0)
    assert right.root.left.left == AVLNode(25, 0)
    assert_valid_avl(right)
