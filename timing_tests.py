import random
import AVLTree


def get_tree_size(i):
    return 1000 * (2 ** i)


def build_random_tree(i):
    tree1 = AVLTree.AVLTree()
    tree2 = AVLTree.AVLTree()
    tree_size = get_tree_size(i)
    for j in range(tree_size):
        key = get_rand_key_not_in_tree(tree1, tree_size)
        tree1.insert(key, 0)
        tree2.insert(key, 0)
    return tree1, tree2


def get_rand_node_in_tree(tree, max):
    arr = tree.avl_to_array()
    key = random.randint(0, max)
    return tree.search(arr[key][0])


def get_rand_key_not_in_tree(tree, max):
    key = random.randint(0, 5*max)
    while tree.search(key) is not None:
        key = random.randint(0, 5*max)

    return key


def calc_rand_node_cost(tree, tree_size):
    rand_key = get_rand_node_in_tree(tree, tree_size)
    t1, t2, avg_cost, max_cost = tree.split(rand_key)
    return avg_cost, max_cost


def calc_max_node_cost(tree):
    max_key = get_max_node(tree.get_root().get_left())
    t1, t2, avg_cost, max_cost = tree.split(max_key)
    return avg_cost, max_cost

def get_max_node(node):
    while node.get_right() is not None and node.get_right().is_real_node():
        node = node.get_right()
    return node
def run_and_calc_cost(num_of_runs, i):
    sum_costs_rand_node_max = 0
    sum_costs_rand_node_avg = 0
    sum_costs_max_node_max = 0
    sum_costs_max_node_avg = 0

    for j in range(num_of_runs):
        tree1, tree2 = build_random_tree(i)

        # Tree 1
        avg_cost_rand_node, max_cost_rand_node = calc_rand_node_cost(tree1, get_tree_size(i))
        sum_costs_rand_node_max += max_cost_rand_node
        sum_costs_rand_node_avg += avg_cost_rand_node

        # Tree 2
        avg_cost_max_node, max_cost_max_node = calc_max_node_cost(tree2)
        sum_costs_max_node_max += max_cost_max_node
        sum_costs_max_node_avg += avg_cost_max_node

    avg_cost_rand_node_max = sum_costs_rand_node_max / num_of_runs
    avg_cost_rand_node_avg = sum_costs_rand_node_avg / num_of_runs
    avg_cost_max_node_max = sum_costs_max_node_max / num_of_runs
    avg_cost_max_node_avg = sum_costs_max_node_avg / num_of_runs
    return avg_cost_rand_node_max, avg_cost_rand_node_avg, avg_cost_max_node_max, avg_cost_max_node_avg


def run_increment_i(max_i):
    for i in range(1, max_i+1):
        print("*" * 40)
        print("_" * 16, i, "_" * 16)
        print("*" * 40)
        max_cost_rand, avg_cost_rand, max_cost_max, avg_cost_max = run_and_calc_cost(10, i)
        print("Max cost for random split is ", max_cost_rand)
        print("Max cost for spliting from the max node is", max_cost_max)
        print("Avg cost for random split is ", avg_cost_rand)
        print("Avg cost for spliting from the max node is", avg_cost_max)


run_increment_i(10)
