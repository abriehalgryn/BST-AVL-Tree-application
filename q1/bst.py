"""
File: bst.py

BST application system allows user to build BST and then perform operations on the BST.
"""

import os
class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None # Point to the left node, default None
        self.right = None # Point to the right node, default None

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
                print("ERROR: node <" + str(e) + "> already exists in the BST!")
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

    def delete_bst_item(self, key):
        self.delete_item(key, self.root)

    def delete_item(self, e, current):
        if current is None: #if the tree node is empty
            print("ERROR: Node <" + str(e) + "> not found!") #if the node is not found display error message
            input("Press Enter to continue")
            os.system('cls')
            return None

        else:

            if e < current.element: #if the key that has to be deleted is smaller than the root than it lies in the left subtree
                current.left = self.delete_item(e, current.left)
            elif e > current.element:#if the key that has to be deleted is greater than the root than it lies in the right subtree
                current.right = self.delete_item(e, current.right)
            else: # element matches current.element

                if current.right is None: #root with only one or no children
                    return current.left

                temp = self.minValueNode(current.right) #root with two children
                current.element = temp.element
                current.right = self.delete_item(temp.element, current.right) #deleted the in order successor

            return current

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

    # Inorder traversal from the root
    def inorder(self):
      self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
      if r != None:
        self.inorderHelper(r.left)
        print(r.element, end = " ")
        self.inorderHelper(r.right)

    def leaf_nodes(self):
        is_leaf, non_leaf = self.leaf_node_helper(self.root, non_leaf = [], is_leaf = [])

        return is_leaf, non_leaf

    def leaf_node_helper(self, r, non_leaf = [], is_leaf = []):
      if r != None: #If the root is not NONE
        self.leaf_node_helper(r.left, non_leaf, is_leaf)
        if not r.left and not r.right: #f there is no left and right subtrees to the current root
            is_leaf.append(r.element)
        if r.left or r.right: #        If there is a left or right sub tree
            non_leaf.append(r.element)
        self.leaf_node_helper(r.right, non_leaf, is_leaf)

      return is_leaf, non_leaf #tuple to return 2 lists

    # Postorder traversal from the root
    def postorder(self):
      self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
      if root != None:
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.element, end = " ")

    def max_subtree_depth(self, root):
        if root is None:
            return 0 # as there is no depth
        leftDepth = self.max_subtree_depth(root.left)
        rightDepth = self.max_subtree_depth(root.right)

        # Choose the larger one and add the root to it.
        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1

    def subtree_depth(self, e):
        current = self.root # Start from the root
        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                print("\nDepth of subtree", str(e) + " is:\n"+ str(self.max_subtree_depth(current)))
                print("\nElements: "), self.postorderHelper(current)
                return None
                #return current # Found at current
        print("ERROR: Node <" + str(e) + "> not found!")
        input("Press Enter to continue")
        os.system('cls')

    # for a given node N in a BST, it calculates the total number of nodes of the sub-tree rooted at N, and prints all nodes, including N, of the sub-tree.
    # Preorder traversal from the root
    def preorder(self):
      self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
      if root != None:
        print(root.element, end = " ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)

    def subtree_nodes(self, e):

        def countNodes(root):
            count = 1 #initialise count as root is 1
            if root is None:
                return -1

            if root.left is not None: #if there is a left child
                count += countNodes(root.left)
            if root.right is not None:#if there is a right child
                count +=  countNodes(root.right)
            return count

        current = self.root # Start from the root
        while current != None:
            if e < current.element: #If target value is less than Item to delete
                current = current.left
            elif e > current.element: #If target value is greater than Item to delete
                current = current.right
            else: # element matches current.element
                print("Preorder of subtree", str(e) + ":")
                self.preorderHelper(current)
                print ("\n\nNumber of Nodes for subtree", str(e) + ":\n" + str(countNodes(current)))
                input("\nPress Enter to continue")
                os.system('cls')
                return None
                #return current # Found at current
        print("ERROR: Node <" + str(e) + "> not found!") #Display error message saying node cannot be found
        input("Press Enter to continue")
        os.system('cls')

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

def main(size = 7):
    nums = [] # variable delcaration for the BST

    print("Welcome to the BST Traversal Program!") # main menu display

    print("\nBuild Menu:")
    print(" 1. Pre-load a sequence of integers to build a BST.")
    print(" 2. Manually enter integer values, one by one, build a BST.")

    while True: #error checking for int input to make sure the program doesnt crash
        try:
            build_choice = int(input("\nEnter choice (1 or 2) >> "))
            if build_choice in [1, 2]:
                break
            else:
                print("Invalid menu choice, please enter number 1 or number 2 ")
            #break out of loop when correct input is inserted
        except:
            print("Invalid menu choice, please enter number 1 or number 2 ")

    os.system('cls') # clear the screen to reduce junk

    if build_choice == 1:
        nums = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]
    else:
        while True:
            try:
                nums = list(map(int, input("Enter the numbers separated by a space (e.g. 1 2 3) >> ").strip().split())) #split input by space and put into list
                break
            except ValueError:
                print("\nInvalid input. Please use integers only, separated by a space. No strings.\n")

    # building tree
    print ("Inserting the following values:")
    for i in nums:
        print(i, end=" ") # print all the values in the list
    print("")
    intTree = BinaryTree()
    for e in nums:# add all the values in the list to the bst
      intTree.insert(e)

    print("")

    while True:
        # print menu  # main menu display
        print("\nMain Menu:")
        print(" 1. Print the pre-order, in-order, and post-order of the BST.")
        print(" 2. Print all leaf nodes of the BST, and all non-leaf nodes (separately).")
        print(" 3. Print the total number of nodes of a sub-tree.")
        print(" 4. Print the depth of a subtree rooted at a particular node.")
        print(" 5. Insert a new integer key into the BST.")
        print(" 6. Delete an integer key from the BST.")
        print(" 7. Exit.")

        while True:
            try:
                main_choice = int(input("\nEnter choice (1 - 7) >> ")) # take input
                if main_choice in [1, 2, 3, 4, 5, 6, 7]:#error checking for int input to make sure the program doesnt crash
                    break
                else:
                    print("Invalid menu choice, please choose a number between 1 and 7")
                #break out of loop when correct input is inserted
            except:
                print("Invalid menu choice, please choose a number between 1 and 7")

        os.system('cls')

        # menu functionalities
        if main_choice == 1: #calls in, pre and post order traversal methods on the tree to display
            print("Pre-order Traversal:")
            intTree.preorder()

            print("\nIn-order Traversal:")
            intTree.inorder()


            print("\nPost-order Traversal:")
            intTree.postorder()

            print("")

        elif main_choice == 2:
            is_leaf, non_leaf = intTree.leaf_nodes() #calls leaf_nodes methods on the tree to display
            print("\nLeaf Nodes:\n" + " ".join(map(str, is_leaf)))
            print("\nNon-leaf Nodes:\n" + " ".join(map(str, non_leaf)))

        elif main_choice == 3:
            print("Pre-order Traversal:")
            intTree.preorder()
            print("")
            while True:
                try:
                    calculate_node = int(input("\nEnter a node to view the subtree >> "))
                    break
                except:
                    print("Invalid menu choice, please enter a integer")

            print("")
            intTree.subtree_nodes(calculate_node)#calls subtree_nodes methods on the tree to display

        elif main_choice == 4:
            print("Pre-order Traversal:")
            intTree.postorder()
            print("")
            while True:#error checking for int input to make sure the program doesnt crash
                try:
                    calculate_node = int(input("\nEnter a node to view the subtree's depth >> "))
                    break
                except:
                    print("Invalid menu choice, please enter a integer")

            intTree.subtree_depth(calculate_node)#calls subtree_depth methods on the tree to display
            print("")

        elif main_choice == 5:
            while True:
                try:#error checking for int input to make sure the program doesnt crash
                    int_to_add = int(input("Enter a new integer into the BST >> "))
                    break
                except:
                    print("Invalid menu choice, please enter a integer")
            intTree.insert(int_to_add)#calls insert methods on the tree to display

        elif main_choice == 6:
            while True:#error checking for int input to make sure the program doesnt crash
                try:
                    int_to_delete = int(input("Delete a integer from the BST >> "))
                    break
                except:
                    print("Invalid menu choice, please enter a integer")

            intTree.delete_bst_item(int_to_delete)#calls delete_bst_item methods on the tree to display

        elif main_choice == 7:
            break

    print("\nGoodbye!\n")

if __name__ == "__main__":
    main()
