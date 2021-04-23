class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()

    def searchNearest(self,root,target,closest):
        if root is None:
            return closest
        if abs(root.data - target ) < abs(closest - target ):
            closest = root.data
        if root.data > target :
            return self.searchNearest(root.left,target,closest)
        else:
            return self.searchNearest(root.right,target,closest)
    
    def is_balanced_helper(self,root):
        if root is None:
            return 0
        left_height = self.is_balanced_helper(root.left)
        right_height = self.is_balanced_helper(root.right)
        if left_height == -1 or right_height == -1 :
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def isBalanced(self,root):
        return self.is_balanced_helper(root) > -1


# Use the insert method to add nodes
root = Node(3)
root.insert(2)
root.insert(1)
root.insert(4)
root.insert(5)
print('\n-------- Printing Binary Tree --------------')
root.PrintTree()

ans = root.searchNearest(root,6,root.data)
print('\nNearest value found  = {}'.format(ans))

ans = root.isBalanced(root)
print('\nIs Tree balanced  = {}'.format(ans))

# print(root.data)
# print(root.left.data)
# l = root.left
# print(l.left.data)
