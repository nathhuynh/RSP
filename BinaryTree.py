class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

"""
Binary Search Tree class
"""
class BinaryTree:
    def __init__(self):
        self.root = None

    # Search the Binary Search Tree for a node with specified target value
    def search(self, target):
        return self.recursive_search(target, self.root)
    
    # Recursive helper function to return the node, search the left subtree or search the right subtree
    def recursive_search(self, target, curr):
        if not curr:
            return None
        if curr.val == target:
            return curr
        elif curr.val < target:
            return self.recursive_search(target, curr.right)
        else:
            return self.recursive_search(target, curr.left)

    # Insert a new node with specified value into the correct position in the BST, or return existing node
    def insert(self, value):
        self.root = self.recursive_insert(value, self.root)
    
    # Recursive helper function for insertion
    def recursive_insert(self, value, curr):
        if not curr:
            return TreeNode(value)

        if curr.val < value:
            curr.right = self.recursive_insert(value, curr.right)
        elif curr.val > value:
            curr.left = self.recursive_insert(value, curr.left)
        return curr
    
    # Delete a node in the BST with specified value if it exists
    def delete(self, value):
        self.root = self.recursive_delete(value, self.root)
    
    # Recursive helper function for deletion
    def recursive_delete(self, value, curr):
        if not curr:
            return None
        if curr.val < value:
            curr.right = self.recursive_delete(value, curr.right)
        elif curr.val > value:
            curr.left = self.recursive_delete(value, curr.left)
        elif curr.val == value:
            # Delete a leaf node
            if not curr.left and not curr.right:
                return None
            # Delete node with 1 child
            elif not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            # Delete node with 2 children
            else:
                # Find the smallest node in the right subtree
                inorder_successor = curr.right
                while inorder_successor.left:
                    inorder_successor = inorder_successor.left
                # Swap to-be-deleted node with inorder successor value
                curr.val = inorder_successor.val
                # Delete inorder successor from the right subtree
                curr.right = self.recursive_delete(inorder_successor.val, curr.right)
        return curr
    
    # Function to display the BST in a nice format
    def display_tree(self):
        if not self.root:
            return
        self.recursive_display_tree(self.root, 0)

    # Recursive helper to display the BST
    def recursive_display_tree(self, curr, level):
        if curr:
            # Print the right subtree first
            self.recursive_display_tree(curr.right, level + 1)
            print(' ' * 4 * level + '->', curr.val)
            # Print the left subtree
            self.recursive_display_tree(curr.left, level + 1)

if __name__ == "__main__":
    tree = BinaryTree()
    
    # Basic insertions
    print("Basic insertions")
    tree.insert(10)
    tree.insert(6)
    tree.insert(18)
    tree.insert(3)
    tree.insert(8)
    tree.insert(19)
    tree.display_tree()
    
    # Searching
    print("Searching")
    print("Searching for 8:", "Found" if tree.search(8) else "Not found")
    print("Searching for 100:", "Found" if tree.search(100) else "Not found")
    
    # Duplicate insertions
    print("Duplicate insertions")
    tree.insert(10)  # Attempt to insert existing value
    print("Tree unchanged:")
    tree.display_tree()
    
    # Deletion
    print("Delete leaf node (3)")
    tree.delete(3)
    tree.display_tree()
    tree.insert(3)
    
    print("Delete node with 1 child (18)")
    tree.delete(18)
    tree.display_tree()
    tree.insert(18)
    
    print("Delete node with 2 children (10)")
    tree.delete(10)
    tree.display_tree()
