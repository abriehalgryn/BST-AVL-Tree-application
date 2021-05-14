class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, e):
        if self.root == None:
          self.root = self.createNewNode(e) # Create a new root
        else:
          # Locate the parent node
          parent = None
          current = self.root
          while current != None:
            if e < current.element:
              parent = current
              current = current.left
            elif e > current.element:
              parent = current
              current = current.right
            else:
              return False # Duplicate node not inserted

          # Create the new node and attach it to the parent node
          if e < parent.element:
            parent.left = self.createNewNode(e)
          else:
            parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    def createNewNode(self, e):
      return TreeNode(e)

    # Inorder traversal from the root
    def inorder(self):
      self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
      if r != None:
        self.inorderHelper(r.left)
        print(r.element, end = " ")
        self.inorderHelper(r.right)

    # Postorder traversal from the root
    def postorder(self):
      self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
      if root != None:
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.element, end = " ")

    # Preorder traversal from the root
    def preorder(self):
      self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
      if root != None:
        print(root.element, end = " ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)

    # Return true if the tree is empty
    def isEmpty(self):
      return self.size == 0

    # Remove all elements from the tree
    def clear(self):
      self.root == None
      self.size == 0

    # Return the root of the tree
    def getRoot(self):
      return self.root

class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None # Point to the left node, default None
        self.right = None # Point to the right node, default None

# function to print leaf nodes
def print_leaves():
    pass

# function to print non-leaf nodes
def print_nodes():
    pass

# function to print total number of nodes 
def print_total_nodes(N):
    pass

# function to print the depth of a subtree rooted at a particular node
def subtree_depth(N):
    pass

# function to insert a new integer key into the BST
def insert_int_key(N):
    pass

# function to delete an integer key from the BST
def delete_int_key(N):
    pass

def main(size = 7):
    print("\nWelcome to the BST Traversal Program!")

    print("\nBuild Menu:")
    print(" 1. Pre-load a sequence of integers to build a BST.")
    print(" 2. Manually enter integer values, one by one, build a BST.")
    build_choice = int(input("\nEnter choice (1 or 2) >> "))

    choices = [1, 2]
    while build_choice not in choices:
        build_choice = int(input("Invalid menu choice, please enter number 1 or number 2 >>"))

    if build_choice == 1:
        nums = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]

    else:
        nums = list(map(int, input("\nEnter the numbers separated by a space (e.g. 1 2 3) >> ").strip().split()))

    # building tree
    print ("\n\nInserting the following values:")
    for i in nums:
        print(i, end=" ")
    intTree = BinaryTree()
    for e in nums:
      intTree.insert(e)

    while True:
        # print menu
        print("\nMain Menu:")
        print(" 1. Print the pre-order, in-order, and post-order of the BST.")
        print(" 2. Print all leaf nodes of the BST, and all non-leaf nodes (separately).")
        print(" 3. Print the total number of nodes of a sub-tree.")
        print(" 4. Print the depth of a subtree rooted at a particular node.")
        print(" 5. Insert a new integer key into the BST.")
        print(" 6. Delete an integer key from the BST.")
        print(" 7. Exit.")
        main_choice = int(input("\nEnter choice (1 - 7) >> ")) # take input
        
        # input validation
        choices = [1, 2, 3, 4, 5, 6, 7]
        while main_choice not in choices:
            main_choice = int(input("Invalid menu choice, please choose a number between 1 and 7, inclusive >> "))

        # menu functionalities
        if main_choice == 1:
            print("\nPre-order Traversal:\n")
            intTree.preorder()

            print("\nIn-order Traversal:\n")
            intTree.inorder()

            print("\nPost-order Traversal:\n")
            intTree.postorder()

        elif main_choice == 2:
            print("\nLeaf Nodes:")
            print_leaves()

            print("\nNon-leaf Nodes:")
            print_nodes()

        elif main_choice == 3:
            N = int(input("Enter a node to view the subtree >> "))
            print_total_nodes(N)

        elif main_choice == 4:
            N = int(input("Enter a node to view the subtree's depth >> "))
            subtree_depth(N)

        elif main_choice == 5:
            N = int(input("Enter a node to insert into the tree >> "))
            insert_int_key(N)

        elif main_choice == 6:
            N = int(input("Enter a node to delete from the tree >> "))
            delete_int_key(N)

        elif main_choice == 7:
            break

    print("\nGoodbye!\n")

if __name__ == "__main__":
    main()