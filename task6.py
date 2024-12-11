class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def prefix_to_tree(expression):
            stack = []
            for char in reversed(expression):
                if char.isalnum():
                    stack.append(Node(char))
                else:
                    node = Node(char)
                    
                    node.left = stack.pop()
                    node.right = stack.pop()
                    stack.append(node)
            return stack[0]

def inorder_traversal(node):
            if not node:
                return ""
            return inorder_traversal(node.left) + str(node.value) + inorder_traversal(node.right)

pre_expr =   '-+a*bc' 
root = prefix_to_tree(pre_expr)   
print(inorder_traversal(root))  