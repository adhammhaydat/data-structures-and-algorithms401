from data_structure.tree_intersection.tree_intersection import BinaryTree ,HashTable ,tree_intersection,Node

def test_tree_intersection():
    tree1=BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    e_node = Node('5')
    f_node = Node('6')
    g_node = Node('7')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    b_node.right = e_node
    c_node.left = f_node
    c_node.right = g_node
    tree1.root=a_node
    
    tree2=BinaryTree()
    a_node = Node('1')
    b_node = Node('8')
    c_node = Node('8')
    d_node = Node('4')
    e_node = Node('5')
    f_node = Node('6')
    g_node = Node('7')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    b_node.right = e_node
    c_node.left = f_node
    c_node.right = g_node
    tree2.root=a_node

    expected = ['1', '4', '5', '6', '7']

    actual = tree_intersection(tree1, tree2)
    assert actual == expected
