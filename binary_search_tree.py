class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def preorder(self):
        print(self.value)
        
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    def search(self, value):
        if self.value == value:
            return True
        elif value < self.value:
            if self.left:
                return self.left.search(value)
        else:
            if self.right:
                return self.right.search(value)
        return False                
root = TreeNode(50)

root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(80)