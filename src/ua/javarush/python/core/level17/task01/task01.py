# Binary Search Tree (BST) Insert

# Write a function to insert a new element into a Binary Search Tree (BST).
# The function should take the root node of the tree and the value of the new element,
# and return the updated tree.

### 🇺🇦 Ukrainian version:

# Бінарне дерево

# Напиши функцію для вставки нового елемента у бінарне дерево пошуку (BST).
# Функція повинна приймати кореневий вузол дерева і значення нового елемента,
# і повертати оновлене дерево.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert_into_bst(root, value):
    # Write your code here
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    elif value > root.value:
        root.right = insert_into_bst(root.right, value)

    return root
