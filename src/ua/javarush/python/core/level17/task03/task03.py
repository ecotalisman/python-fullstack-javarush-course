# AVL Tree

# Write a function to insert a new element into an AVL tree.
# Also write the functions get_height, update_height, left_rotate, and right_rotate.

### 🇺🇦 Ukrainian version:

# AVL-дерево

# Напишіть функцію для вставки нового елемента в AVL-дерево.
# Напишіть функції get_height, update_height, left_rotate і right_rotate

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    # Write your code here
    if not node:
        return 0
    return node.height

def update_height(node):
    # Write your code here
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def left_rotate(z):
    # Write your code here
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    update_height(z)
    update_height(y)

    return y

def right_rotate(z):
    # Write your code here
    y = z.left
    T2 = y.right

    y.right = z
    z.left = T2

    update_height(z)
    update_height(y)

    return y

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def insert(root, key):
    if not root:
        return TreeNode(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    update_height(root)

    balance = get_balance(root)

    # Left Left Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Right Right Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root
