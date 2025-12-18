# Inserting into an AVL Tree

# Write an insert function to insert a new element into an AVL tree.
# The function should take the root node of the tree and the value of the new element
# and return the updated tree.

### 🇺🇦 Ukrainian version:

# Вставка в AVL-дерево

# Напишіть функцію для insert вставки нового елемента в AVL-дерево.
# Функція повинна приймати кореневий вузол дерева і значення нового елемента
# і повертати оновлене дерево.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = max(get_height(y.left), get_height(y.right)) + 1
    x.height = max(get_height(x.left), get_height(x.right)) + 1

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = max(get_height(x.left), get_height(x.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1

    return y

def insert(root, key):
    # Write your code here
    if not root:
        return TreeNode(key)

    elif key < root.key:
        root.left = insert(root.left, key)

    else:
        root.right = insert(root.right, key)
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root
