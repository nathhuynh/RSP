class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Singly LinkedList class
"""
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node with specified value to the end of the LinkedList
    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
            return
        # Traverse to end of list and insert there
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(value)

    # Add a node with specified value to the front of the list
    def prepend(self, value):
        old_head = self.head
        self.head = ListNode(value, old_head)

    # Remove the first node found that has the specificed value
    def remove(self, value):
        prev, curr = None, self.head
        while curr:
            if curr.val == value:
                if not prev:
                    self.head = curr.next # Value to be removed is at the head
                else:
                    prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
        return False
    
    # Search for index of the first occurence of the specified value
    def search(self, value):
        i, curr = 0, self.head
        while curr:
            if curr.val == value:
                print(f"Value {value} found at Node {i}")
                return i
            curr = curr.next
            i += 1
        print(f"Value {value} not found in LinkedList.")
        return -1
    
    # Print all values in the LinkedList
    def display(self):
        i, curr = 0, self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
            i += 1
        print()
        
if __name__ == "__main__":
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.display()

    list.prepend(4)
    list.display()

    list.remove(4)
    list.display()

    list.search(4)
    list.search(3)
    