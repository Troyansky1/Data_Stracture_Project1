
import random
import inspect
import avl_template


def print_avl_tree(root, title= "Tree"):
    print(title)
    print_avl_tree_req(root)
    print("\n")

def print_avl_tree_req(root, prefix="", is_left=True):
    if root.is_real_node():
        key_str = "KEY:" + str(root.key)
        bf_str = " BF:" + str(root.get_bf())
        height_str = " Height:" + str(root.get_height())

        print(prefix + ("|-- " if is_left else "\\-- ") + key_str + bf_str + height_str)
        print_avl_tree_req(root.left, prefix + ("|   " if is_left else "    "), True)
        print_avl_tree_req(root.right, prefix + ("|   " if is_left else "    "), False)


def print_test(test):
    print("*"*40)
    print("_"*16, test, "_"*16)
    print("*" * 40)

#Insert in order and a few deletes. uses rotations.
def test1():
    print_test(inspect.currentframe().f_code.co_name)
    avl = avl_template.AVLTree()
    for i in range(1, 30):
       avl.insert(i, i)
    node = avl.search(7)
    avl.delete(node)
    node = avl.search(9)
    avl.delete(node)
    print(avl.avl_to_array())
    print_avl_tree(avl.get_root())

# Insert in reverse order and a few deletes. uses rotations.
def test2():
    print_test(inspect.currentframe().f_code.co_name)
    avl = avl_template.AVLTree()
    for i in range(30, 1, -1):
        avl.insert(i, i)
    node = avl.search(7)
    avl.delete(node)
    node = avl.search(9)
    avl.delete(node)
    print(avl.avl_to_array())
    print_avl_tree(avl.get_root())

#insert random numbers.
def test3():
    print_test(inspect.currentframe().f_code.co_name)
    avl = avl_template.AVLTree()
    nums_in_tree = []
    for i in range(20):
        num = random.randint(1, 100)
        if num not in nums_in_tree:
            avl.insert(num, num)
            print_avl_tree(avl.get_root())
        nums_in_tree.append(num)
    print(avl.avl_to_array())
    print_avl_tree(avl.get_root())

#inser random numbers, than delete random numbers.
def test4():
    print_test(inspect.currentframe().f_code.co_name)
    avl = avl_template.AVLTree()
    nums_in_tree = []
    for i in range(50):
        num = random.randint(1, 100)
        if num not in nums_in_tree:
            avl.insert(num, num)
        nums_in_tree.append(num)
    print_avl_tree(avl.get_root())

    for i in range(10):
        num = random.randint(1, 100)
        node = avl.search(num)
        if node is not None:
            print(avl.delete(node), node.get_key())
    print(avl.avl_to_array())
    print_avl_tree(avl.get_root())


# Super random, checks for bugs and edge cases
def test5():
    print_test(inspect.currentframe().f_code.co_name)
    avl = avl_template.AVLTree()
    nums_in_tree = []
    for i in range(1000):
        num = random.randint(1, 100)
        if num not in nums_in_tree:
            avl.insert(num, num)
            nums_in_tree.append(num)
        else:
            node = avl.search(num)
            if node is not None:
                avl.delete(node), node.get_key()
    print_avl_tree(avl.get_root())


def test6(): #testing join
    print_test(inspect.currentframe().f_code.co_name)
    avl = avl_template.AVLTree()
    for i in range(1, 5):
       avl.insert(i, i)
    print_avl_tree(avl.get_root())
    print("####################################")
    print("####################################")
    avl2 = avl_template.AVLTree()
    for i in range(10, 20):
       avl2.insert(i, i)
    print_avl_tree(avl2.get_root())
    print("####################################")
    print("####################################")
    avl.join(avl2, 7,7)
    print_avl_tree(avl.get_root())

def test7(): #testing split
    print_test(inspect.currentframe().f_code.co_name)
    avl = avl_template.AVLTree()
    for i in range(1, 20):
       avl.insert(i, i)
    print_avl_tree(avl.get_root())
    print("####################################")
    print("####################################")
    x = avl_template.AVLNode(7,7)
    [minT, maxT] = avl.split(x)
    print(minT.get_root().get_key())
    print_avl_tree(minT.get_root())
    print("####################################")
    print("####################################")
    print(maxT.get_root().get_key())
    print_avl_tree(maxT.get_root())


def test8():
    tree = avl_template.AVLTree()
    tree.insert(33, 0)
    tree.insert(25, 0)
    tree.insert(59, 0)

    tree.insert(23, 0)
    tree.insert(29, 0)
    tree.insert(120, 0)
    tree.insert(31, 0)
    print("tree before is ")
    print_avl_tree(tree.get_root())
    print("########")
    node = tree.search(120)
    print(tree.delete(node))
    print("tree after is ")
    print_avl_tree(tree.get_root())
    print("########")


if __name__ == '__main__':
    #test1()
    #test2()
    #test3()
    #test4()
    #test5()
    #test6()
    #test7()
    test8()

