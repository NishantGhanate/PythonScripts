class Node:
    def __init__(self, val): 
        self.val = val  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.val) 
    
class BinarySearchTree:
    # Init root as none 
    def __init__(self): 
        self.root = None
        
    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
        return self.root
    
    def preOrder(self,root):
        if root:
            print(root.val, end = ' ')
            self.preOrder(root.left)
            self.preOrder(root.right)
            
    def postOrder(self,root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.val, end=' ')
    
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.val, end=" ")
            self.inOrder(root.right)
    
    def levelOrder(self,root):
        if root is None: return
        q = [root]
        while(len(q) > 0):
            n = q.pop(0)
            print (n.val,end='')
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
            
    def height(self,root):
        if root is None:
            return -1
        return 1 + max( self.height(root.left),  self.height(root.right))

if __name__ == "__main__":
    tree = BinarySearchTree()
    # arr = list(map(int, input().split()))
    arr = [1,2,5,3,4,6]
    for i in arr:
        tree.create(i)
     
     # Sample Input
    #  1
    #   \
    #    2
    #     \
    #      5
    #     /  \
    #    3    6
    #     \
    #      4
    # Sample Output - Pre-Order
    # 1 2 5 3 4 6 
        
    print("\n------------ Pre Order ----------------")
    tree.preOrder(root=tree.root) 
    
    

    # Sample Input
    #  1
    #   \
    #    2
    #     \
    #      5
    #     /  \
    #    3    6
    #     \
    #      4
    # Sample Output - Post Order
    # 4 3 6 5 2 1 
    
    print("\n------------ Post Order ----------------")
    tree.postOrder(root=tree.root) 
    
    # Sample Input
    #  1
    #   \
    #    2
    #     \
    #      5
    #     /  \
    #    3    6
    #     \
    #      4
    # Sample Output - In-Order
    # 1 2 5 3 4 6 
    print("\n------------ In Order ----------------")
    tree.inOrder(root=tree.root)
    
    print("\n------------ Tree height ----------------")
    height = tree.height(root=tree.root)
    print(height)
    
        
    print("\n------------ Level order ----------------")
    tree.levelOrder(root=tree.root)
    