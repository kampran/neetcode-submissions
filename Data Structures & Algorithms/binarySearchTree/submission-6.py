class Node:
    def __init__(self, key, value):
        self.parent = None
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.min_node = None
        self.max_node = None

class TreeMap:
    
    def __init__(self):
        self.head = None
        self.dic = {}


    def inorderTraversal(self, node: Node) -> List[int]:
        if not node:
            return []
        
        return self.inorderTraversal(node.left) + [node.key] + self.inorderTraversal(node.right)


    def insert(self, key: int, val: int) -> None:
        if not self.head:
            new_node = Node(key, val)
            self.head = new_node
            self.min_node = new_node
            self.max_node = new_node
            self.dic[key] = self.head
            return
        
        node = self.head
        prev_node = None
        prev_pointer = None # 'l' or 'r'

        while node:
            if key == node.key:
                node.value = val
                self.dic[key].value = val
                return
            
            prev_node = node

            if key < node.key:
                prev_pointer = 'l'
                node = node.left
            else:
                prev_pointer = 'r'
                node = node.right
        
        new_node = Node(key, val)

        if prev_pointer == 'l':
            prev_node.left = new_node
        elif prev_pointer == 'r':
            prev_node.right = new_node
        
        new_node.parent = prev_node

        self.dic[key] = new_node

        if key < self.min_node.value:
            self.min_node = new_node
        elif key > self.max_node.value:
            self.max_node = new_node

        print (self.inorderTraversal(self.head))
        


    def get(self, key: int) -> int:
        if key in self.dic:
            return self.dic[key].value
        else:
            return -1


    def getMin(self) -> int:
        if self.head:
            return self.dic[self.min_node.key].value
        else:
            return -1


    def getMax(self) -> int:
        if self.head:
            return self.dic[self.max_node.key].value
        else:
            return -1


    def getMinOfTree(self, head):
        node = head
        prev_node = None

        while node:
            prev_node = node
            node = node.left
        
        val = prev_node.key

        if head == prev_node:
            prev_node.parent.right = None
        else:
            prev_node.parent.left = None

        prev_node = None

        return val


    def remove(self, key: int) -> None:
        if key not in self.dic:
            return

        node = self.dic[key]

        del self.dic[key]

        if not node.left and not node.right:

            if node == self.head:
                self.head = None
                self.min_node = None
                self.max_node = None

            elif node == self.min_node:
                self.min_node = node.parent
            
            elif node == self.max_node:
                self.max_node = node.parent

            node = None

            return
        
        if not node.left:
            prev_node = node
            node = node.right

            if prev_node == self.head:
                self.head = node
                self.head.parent = None
            
            if not self.head.right and not self.head.left:
                self.min_node = self.head
                self.max_node = self.head

            prev_node = None

            return
        
        if not node.right:
            prev_node = node
            node = node.left

            if prev_node == self.head:
                self.head = node
                self.head.parent = None
            
            if not self.head.right and not self.head.left:
                self.min_node = self.head
                self.max_node = self.head

            return
        
        print ("node.right :", node.right.key)
        successor_value = self.getMinOfTree(node.right)
        print ("successor value : ", successor_value)

        node.key = successor_value

    def getInorderKeys(self) -> List[int]:
        if not self.head:
            return []
        
        return self.inorderTraversal(self.head)

        


