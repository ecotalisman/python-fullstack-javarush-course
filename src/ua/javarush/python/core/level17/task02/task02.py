# Searching for an Element in a Binary Search Tree (BST)

# Write a function to search for an element in a Binary Search Tree (BST).
# The function should take the root node of the tree and the value to search for,
# and return the node containing the value, or None if the element is not found.

### 🇺🇦 Ukrainian version:

# Пошук елемента в бінарному дереві

# Напишіть функцію для пошуку елемента в бінарному дереві пошуку (BST).
# Функція повинна приймати кореневий вузол дерева і значення шуканого елемента
# та повертати вузол, що містить шукане значення, або None, якщо елемент не знайдено.


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def search_bst(root: TreeNode, val: int) -> TreeNode:
    # Write your code here
    if root is None or root.value == val:
        return root
    elif val < root.value:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)
