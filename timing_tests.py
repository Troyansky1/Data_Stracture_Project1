import random
import avl_template


def get_tree_size(i):
    return 1000 * (2 ^ i)


def build_random_tree(i):
    tree1 = avl_template.AVLTree()
    tree2 = avl_template.AVLTree()
    tree_size = get_tree_size(i)
    for j in range(tree_size):
        key = get_rand_key_not_in_tree(tree1, tree_size)
        tree1.insert(key, 0)
        tree2.insert(key, 0)
    return tree1, tree2


def get_rand_node_in_tree(tree, max):
    key = random.randint(max)
    while tree.search(key) is None:
        key = random.randint(max)
    return tree.search(key)


def get_rand_key_not_in_tree(tree, max):
    key = random.randint(max)
    while tree.search(key) is not None:
        key = random.randint(max)
    return key


def calc_rand_cost(tree, tree_size):
    rand_key = get_rand_node_in_tree(tree, tree_size)
    rand_cost = tree.split(rand_key)[2] #TODO change in avl tree, return cost from split
    return rand_cost


def calc_max_cost(tree):
    max_key = tree.get_max_node(tree.get_root())
    max_cost = tree.split(max_key)[2] #TODO change in avl tree return cost from split
    return max_cost


def run_and_calc_cost(num_of_runs, i):
    max_cost_rand = 0
    sum_costs_rand = 0
    max_cost_max = 0
    sum_costs_max = 0
    for j in num_of_runs:
        tree1, tree2 = build_random_tree(i)
        cost_rand = calc_rand_cost(tree1, get_tree_size(i))
        if cost_rand>max_cost_rand:
            max_cost_rand = cost_rand
        sum_costs_rand += cost_rand

        cost_max = calc_max_cost(tree2, )
        if cost_max > max_cost_max:
            max_cost_max = cost_max
        sum_costs_max += cost_max
    avg_cost_rand = sum_costs_rand/num_of_runs
    avg_cost_max = sum_costs_max/num_of_runs
    return max_cost_rand, avg_cost_rand, max_cost_max, avg_cost_max


def run_increment_i(max_i):
    for i in range(max_i):
        print("*" * 40)
        print("_" * 16, i, "_" * 16)
        print("*" * 40)
        max_cost_rand, avg_cost_rand, max_cost_max, avg_cost_max = run_and_calc_cost(100, i)
        print("Max cost for random split is ", max_cost_rand)
        print("Max cost for spliting from the max node is", max_cost_max)
        print("Avg cost for random split is ", avg_cost_rand)
        print("Avg cost for spliting from the max node is", avg_cost_max)






