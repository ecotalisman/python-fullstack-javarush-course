# Finding Min and Max in a Binary Search Tree (BST)

# Write functions to find the minimum (find_min) and maximum (find_max) elements in a BST.
# The functions should take the root node of the tree and return the node
# with the minimum or maximum value.

### 🇺🇦 Ukrainian version:

# Пошук пар чисел в AVL-дереві

# Напишіть функції для знаходження мінімального (find_min) та максимального (find_max) елемента
# в бінарному дереві пошуку (BST).
# Функції повинні приймати кореневий вузол дерева та повертати вузол
# з мінімальним або максимальним значенням.

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_min(node):
    # Write your code here:
    if node is None:
        return None
    if node.left is None:
        return node
    return find_min(node.left)

def find_max(node):
    # Write your code here:
    if node is None:
        return None
    if node.right is None:
        return node
    return find_max(node.right)

# Example usage:
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.right = TreeNode(35)

print("Мінімальне значення:", find_min(root).val)
print("Максимальне значення:", find_max(root).val)
