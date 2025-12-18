# Searching in an AVL Tree

# Write a search function to find an element in a Binary Search Tree (BST).
# The function should take the root node of the tree and the value to search for,
# and return the node containing the value, or None if the element is not found.

### 🇺🇦 Ukrainian version:

# Пошук в AVL-дереві

# Напишіть функцію search для пошуку елемента в бінарному дереві пошуку (BST).
# Функція повинна приймати кореневий вузол дерева і значення шуканого елемента та повертати вузол,
# що містить шукане значення, або None, якщо елемент не знайдено.

class TreeNode:
    def __init__(self, key, left=None, right=None, height=1):
        self.key = key
        self.left = left
        self.right = right
        self.height = height

def search(root, key):
    # Write your code here:
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

# Example usage:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
result = search(root, 15)
print(result.key if result else "Not found")