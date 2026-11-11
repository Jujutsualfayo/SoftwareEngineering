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
            
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)

root.left.left = TreeNode(5)
root.left.right = TreeNode(15)

root.right.right = TreeNode(40)

root.preorder()

