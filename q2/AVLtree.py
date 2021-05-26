"""
File: AVLtree.py

Tests the AVL tree building algorithm and deletion function.
"""

import os
import random

outputdebug = True

def debug(msg):
    if outputdebug:
        print (msg)

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class AVLTree():
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0;

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, key):
        tree = self.node

        newnode = Node(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        else:
            debug("Key [" + str(key) + "] already in tree.")

        self.rebalance()

    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate right pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete_node(self, key):
            if self.node != None:
                if self.node.key == key:
                    if self.node.left.node == None and self.node.right.node == None: # no children these can be deleted at will
                        self.node = None
                    elif self.node.left.node == None:# if there is only one subtree it will use this
                        self.node = self.node.right.node
                    elif self.node.right.node == None:
                        self.node = self.node.left.node
                    else:# if both children are present it will find the logical_successor
                        change = self.logical_successor(self.node)
                        if change != None:
                            debug("Replacing " + str(key) + " with: " + str(change.key))
                            self.node.key = change.key #replace key
                            self.node.right.delete(change.key) # delete key from right child
                    self.rebalance()
                    return
                elif key < self.node.key:
                    self.node.left.delete_node(key)
                elif key > self.node.key:
                    self.node.right.delete_node(key)

                self.rebalance()
            else:
                print("ERROR: Node <" + str(key) + "> not found!")

    def logical_predecessor(self, node):
        '''
        Find the biggest valued node in LEFT child
        '''
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        '''
        Find the smallese valued node in RIGHT child
        '''
        node = node.right.node
        if node != None: # just a sanity check

            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def display(self, level=0, pref=''):
        '''
        Display the whole tree (but turned 90 degrees counter-clockwisely). Uses recursive def.
        '''
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if(self.node != None):
            print ('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')

    def leaf_nodes(self):
        is_leaf, non_leaf = self.leaf_node_helper()

        return is_leaf, non_leaf

    def leaf_node_helper(self, non_leaf = [], is_leaf = []):
        if self.node == None: #if there is no node there will be no leaves and no non leaves
            return non_leaf, is_leaf

        if self.node.left: #if there is a left subtree it goes recursive on that node
            self.node.left.leaf_node_helper(non_leaf, is_leaf)

        if (not self.node.left.node) and (not self.node.right.node): #if there is no subtrees the node is a leaf
            is_leaf.append(self.node.key)
        else:
            non_leaf.append(self.node.key)

        if self.node.right:#if there is a right subtree it goes recursive on that node
            self.node.right.leaf_node_helper(non_leaf, is_leaf)

        return is_leaf, non_leaf

# Usage example
if __name__ == "__main__":
    nums = [] # variable delcaration for the BST
    print("Welcome to the AVL Traversal Program!")

    print("\nBuild Menu:")
    print(" 1. Pre-load a sequence of integers to build a AVL tree.")
    print(" 2. Manually enter integer values, one by one, build a AVL tree.")

    while True:
        try:
            build_choice = int(input("\nEnter choice (1 or 2) >> "))
            if build_choice in [1, 2]:
                break
            else:
                print("Invalid menu choice, please enter number 1 or number 2 ")
            #break out of loop when correct input is inserted
        except:
            print("Invalid menu choice, please enter number 1 or number 2 ")

    os.system('cls')

    if build_choice == 1:
        nums = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]
    else:
        nums = list(map(int, input("Enter the numbers separated by a space (e.g. 1 2 3) >> ").strip().split()))

    # building tree
    print ("Inserting the following values:")
    for i in nums:
        print(i, end=" ")
    print("")
    intTree = AVLTree()
    for e in nums:
        intTree.insert(e)

    print("")

    while True:
        # print menu
        print("\nMain Menu:")
        print(" 1. Insert a new integer key into the AVL tree.")
        print(" 2. Delete an integer key from the AVL tree.")
        print(" 3. Print the in-order traversal sequence of the AVL tree.")
        print(" 4. Print all leaf nodes of the AVL tree, and all non-leaf nodes (separately).")#do this
        print(" 5. Display the AVL tree, showing the height and balance factor for each node.")
        print(" 6. Exit.")

        while True:
            try: #error checking for int input to make sure the program doesnt crash
                main_choice = int(input("\nEnter choice (1 - 6) >> ")) # take input
                if main_choice in [1, 2, 3, 4, 5, 6]:
                    break
                else:
                    print("Invalid menu choice, please choose a number between 1 and 7")
                #break out of loop when correct input is inserted
            except:
                print("Invalid menu choice, please choose a number between 1 and 7")

        os.system('cls')

        if main_choice == 1:
            while True:#error checking for int input to make sure the program doesnt crash
                try:
                    int_to_add = int(input("Enter a new integer into the BST >> "))
                    break
                except:
                    print("Invalid menu choice, please enter a integer")
            intTree.insert(int_to_add)#calls insert methods on the tree to display

        elif main_choice == 2: #delete key
            while True:#error checking for int input to make sure the program doesnt crash
                try:
                    int_to_delete = int(input("Delete a integer from the BST >> "))
                    break
                except:
                    print("Invalid menu choice, please enter a integer")

            intTree.delete_node(int_to_delete)#calls delete methods on the tree to display

        elif main_choice == 3:
            print ("Inorder traversal:", intTree.inorder_traverse())#calls inorder traverse methods on the tree to display
            input("Press enter to continue")
            os.system('cls')

        elif main_choice == 4: #priNt leaf nodes
            is_leaf, non_leaf = intTree.leaf_nodes()#calls leaf nodes methods on the tree to display
            print("\nLeaf Nodes:\n" + " ".join(map(str, is_leaf)))
            print("\nNon-leaf Nodes:\n" + " ".join(map(str, non_leaf)))

        elif main_choice == 5:
            intTree.display()#calls display methods on the tree to display
            input("Press enter to continue")
            os.system('cls')

        elif main_choice == 6:
            break

    print("\nGoodbye!\n")