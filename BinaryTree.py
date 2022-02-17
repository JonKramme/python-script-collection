class Node:
    def __init__(self,val):
        self.data = val
        self._left = None
        self._right = None

    def left(self):
        return self._left

    def right(self):
        return self._right

    def insert_left(self, val):
        if self._left is None:
            self._left = Node(val)
        return -1

    def insert_right(self, val):
        if self._right is None:
            self._right = Node(val)
        return -1

    def preorder_query(self):
        print(self.data)
        if self._left is not None:
            self._left.preorder_query()
        if self._right is not None:
            self._right.preorder_query()

    def inorder_query(self):
        if self._left is not None:
            self._left.inorder_query()
        print(self.data)
        if self._right is not None:
            self._right.inorder_query()

    def postorder_query(self):
        if self._left is not None:
            self._left.postorder_query()
        if self._right is not None:
            self._right.postorder_query()
        print(self.data)

    def breadth_first_query(self):
        height = self.height(self)
        for i in range(1, height+1):
            self.print_curr_level(self,i)

    def print_curr_level(self,node,level):
        if node is None:
            return
        if level == 1:
            print(node.data)
        elif level > 1:
            self.print_curr_level(node.left(),level-1)
            self.print_curr_level(node.right(),level-1)

    def height(self,node):
        if node is None:
            return 0
        else:
            lheight = node.height(node._left)
            rheight = node.height(node._right)
            return lheight+1 if lheight > rheight else rheight+1


#Test Driver-code
N = Node(1)
N.insert_left(2)
N.left().insert_left(4)
N.left().insert_right(5)
N.insert_right(3)

N.breadth_first_query()
