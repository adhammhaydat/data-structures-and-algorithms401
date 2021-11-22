
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
class HashNode:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = HashNode(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        """
        Initalization of Hash table
        
        """
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value 
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)
        return index

def tree_intersection(tree1, tree2):
    hash_map=HashTable()
    list_item1 = tree1.bfs()
    list_item2 = tree2.bfs()
    list_index2=[]
    list_index1 = []
    for item1 in list_item1:
        list_index1.append(hash_map.add(item1,item1)) 
    for item2 in list_item2:
        index=hash_map.add(item2,item2)  
        if index in list_index1:
            list_index2.append(item2)
    return list_index2        
            
            

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
          
print(tree_intersection(tree1,tree2))            
            
            
            
            
            
            
            



