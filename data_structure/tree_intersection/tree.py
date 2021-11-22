class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Queue:
    def __init__(self, collection=[]):
        self.data = collection

    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)


class BinaryTree:
    def __init_(self):
        self.root = None

    def bfs(self):
        """
        A binary tree method which returns a list of items that it contains
        input: None
        output: tree items
        """
        # Queue breadth <-- new Queue()
        breadth = Queue()
        # breadth.enqueue(root)
        breadth.enqueue(self.root)
        if not self.root:
            return None
        list_of_items = []

        while breadth.peek():
            front = breadth.dequeue()
            list_of_items += [front.data]

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return list_of_items

    def pre_order(self):
        """
        A binary tree method which returns a list of items that it contains
        input: None
        output: tree items
        sub method : walk () to make the recursion staff
        """
        list_of_items = []

        def walk(node):
            if node:
                list_of_items.append(node.data)
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items

    def in_order(self):
        """
        function to in order the list using Trees
        """
        if not self.root:
            return None
        list_of_items = []

        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                list_of_items.append(node.data)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items

    def post_order(self):
        """
        A binary tree method which returns a list of items in post order
        input: None
        output: tree items
        """
        list_of_items = []

        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)
                list_of_items.append(node.data)

        walk(self.root)
        return list_of_items

    def find_maximum_value(self):
        """
        find maximum value
        Arguments: none
        Returns: number
        """
        if not self.root:
            return "the tree are empty"

        list_of_items = []

        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)
                list_of_items.append(node.data)
        walk(self.root)
        max_number=0
        for i in range(len(list_of_items)):
            if list_of_items[i]>max_number:
                max_number=list_of_items[i]
        return max_number


def breadth_first(tree):
        """
        A binary tree method which returns a list of items that it contains
        input: tree
        output: tree items
        """
        if not tree.root:
            return None
        # Queue breadth <-- new Queue()
        breadth = Queue()
        # breadth.enqueue(root)
        breadth.enqueue(tree.root)

        list_of_items = []

        while breadth.peek():
            front = breadth.dequeue()
            list_of_items += [front.data]

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return list_of_items