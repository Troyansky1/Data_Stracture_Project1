
import random

import avl_template


def print_avl_tree(root, prefix="", is_left=True):
    if root is not None:
        key_str = "KEY:" + str(root.key)
        bf_str = " BF:" + str(root.get_BF())
        height_str = " Height:" + str(root.get_height())

        print(prefix + ("|-- " if is_left else "\\-- ") + key_str + bf_str + height_str)
        print_avl_tree(root.left, prefix + ("|   " if is_left else "    "), True)
        print_avl_tree(root.right, prefix + ("|   " if is_left else "    "), False)


def test_avl_template():
    def test1():
        for i in range(6):
            avl.insert(i, i)
        print_avl_tree(avl.get_root())

    def test2():
        nums_in_tree = []
        for i in range(50):
            num = random.randint(0, 100)
            nums_in_tree.append(num)
            if num not in nums_in_tree:
                avl.insert(num, num)
        print_avl_tree(avl.get_root())

        for i in range(10):
            num = random.choice(nums_in_tree)
            avl.delete(num)
        print_avl_tree(avl.get_root())


    avl = avl_template.AVLTree()
    test1()

if __name__ == '__main__':
    test_avl_template()



