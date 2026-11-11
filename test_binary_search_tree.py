from binary_search_tree import TreeNode


def test_root_creation():
    root = TreeNode(50)

    assert root.value == 50
    assert root.left is None
    assert root.right is None


def test_insert_left_child():
    root = TreeNode(50)
    root.insert(30)

    assert root.left.value == 30


def test_insert_right_child():
    root = TreeNode(50)
    root.insert(70)

    assert root.right.value == 70


def test_insert_multiple_values():
    root = TreeNode(50)

    for value in [30, 70, 20, 40, 60, 80]:
        root.insert(value)

    assert root.left.value == 30
    assert root.right.value == 70
    assert root.left.left.value == 20
    assert root.left.right.value == 40
    assert root.right.left.value == 60
    assert root.right.right.value == 80