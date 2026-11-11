from binary_search_tree import TreeNode


def make_tree():
    root = TreeNode(10)
    root.insert(5)
    root.insert(15)
    root.insert(3)
    root.insert(7)
    root.insert(20)
    return root


def test_find_root():
    root = make_tree()

    assert root.search(10) is True


def test_find_left_child():
    root = make_tree()

    assert root.search(5) is True


def test_find_right_child():
    root = make_tree()

    assert root.search(15) is True


def test_find_deep_leaf():
    root = make_tree()

    assert root.search(7) is True
    assert root.search(20) is True


def test_value_not_found():
    root = make_tree()

    assert root.search(100) is False


def test_value_smaller_than_minimum():
    root = make_tree()

    assert root.search(1) is False


def test_value_missing_between_nodes():
    root = make_tree()

    assert root.search(12) is False


def test_single_node_tree():
    root = TreeNode(10)

    assert root.search(10) is True
    assert root.search(5) is False


def test_zero_value_is_found():
    root = TreeNode(5)
    root.insert(0)

    assert root.search(0) is True


def test_chain_tree():
    root = TreeNode(1)
    for n in [2, 3, 4, 5]:
        root.insert(n)

    assert root.search(5) is True
    assert root.search(99) is False