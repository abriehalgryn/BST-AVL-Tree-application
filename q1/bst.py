'''
Main program for Q1.
'''

# pre-order traversal function
def preorder():
    pass

# in-order traversal function
def inorder():
    pass

# post-order traversal function
def postorder():
    pass

# function to print and accept input for main menu
def menu():
    print("\nMain Menu:")
    print(" 1. Print the pre-order, in-order, and post-order of the BST.")
    print(" 2. Print all leaf nodes of the BST, and all non-leaf nodes (separately).")
    print(" 3. Print the total number of nodes of a sub-tree.")
    print(" 4. Print the depth of a subtree rooted at a particular node.")
    print(" 5. Insert a new integer key into the BST.")
    print(" 6. Delete an integer key from the BST.")
    print(" 7. Exit.")
    choice = int(input("\nEnter choice (1 - 7) >> "))
    return choice

# function to print leaf nodes
def print_leaves():
    pass

# function to print non-leaf nodes
def print_nodes():
    pass

# function to print total number of nodes
def print_total_nodes():
    pass

# function to print the depth of a subtree rooted at a particular node
def subtree_depth():
    pass

# function to insert a new integer key into the BST
def insert_int_key():
    pass

# function to delete an integer key from the BST
def delete_int_key():
    pass

# main program
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

print("\nBST Values are", nums)

while True:
    main_choice = menu()
    choices = [1, 2, 3, 4, 5, 6, 7]
    while main_choice not in choices:
        main_choice = int(input("Invalid menu choice, please choose a number between 1 and 7, inclusive >> "))

    if main_choice == 1:
        print("\nPre-order Traversal:\n")
        preorder()

        print("\nIn-order Traversal:\n")
        inorder()

        print("\nPost-order Traversal:\n")
        postorder()

    elif main_choice == 2:
        pass
        print("hi, this is a test to see if github works")
        print("This is test 2 with a new branch!!")

    elif main_choice == 3:
        pass

    elif main_choice == 4:
        pass

    elif main_choice == 5:
        pass

    elif main_choice == 6:
        pass

    elif main_choice == 7:
        break

print("\nGoodbye!\n")
