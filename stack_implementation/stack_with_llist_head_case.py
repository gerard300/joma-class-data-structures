#from my_linked_list_implementation import LinkedList, Node

class Node:
    # This class represents each node of the linked list
    def __init__(self, data):
        # The Node has this two main elements
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class Stack:
    """
    Stack is an ADT (Abstract Data Type) and follows LIFO

    Stack Rules:
        + You cannot pop the last element of the stack
        + If You want to pop off the first element you have to pop off all the previous elements
    
    Stack can be implemented with different data structures:
        + Linked List Head implementation in this case
    """
    def __init__(self):
        self.head = None
        self.count = 0

    def __str__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return f"Head Node: {self.head} and Number of elements in the stack are: {self.count}\n State: "+" -> ".join(map(str, nodes))
        #self.stack_llist.__repr__() #" | ".join(map(str,self.stack_list))+"*"
    # Stacks have two basic operations
    def push(self,element):
        # Push elements in the stack following the LIFO (Last In First Out)
        # The cost of add new node at the beginning of the list is O(1)
        if self.count ==0:
            self.head = Node(element)
            self.count +=1
        else:
            node = Node(element)
            node.next = self.head
            self.head = node
            self.count +=1

        
    def __iter__(self):
        # The definition and implementation of this function is more Pythonic
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def pop(self):
        # Removes the most recently added element
        # If you want to pop the last in element you have to go over all the LinkedList/Stack
        # This Operations costs O(n)
        data = self.head.data
        self.head = self.head.next
        self.count -= 1
        return data
        

    def top(self) -> str:
        # Allows you to get the last element you pushed in without popping
        return self.head

    def is_empty(self) -> bool:
        # Tells you if the Stack is empty
        return self.count ==0

if __name__ == '__main__':
    stack = Stack()
    #print(f"Stack is empty? --> {stack.is_empty()}")
    print("Populating the stack with the next 3 elements: [1,2,3]")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    #print(f"This is the stack status: {stack.__str__()} \nAnd this is the top_index element {stack.top()}")
    print(f"This is the stack status: {stack.__str__()}")

    print("Popping the last two elements of the Stack [3,2]")
    print(f"Element {stack.pop()} popped!!")
    print(f"Element {stack.pop()} popped!!")

    print(f"This is the stack status: {stack.__str__()}")

    print(f"Element {stack.pop()} popped!!")

    print(f"This is the stack status: {stack.__str__()}")

    print("Populating the stack with the next 3 elements: [3,4,5]")
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(f"This is the stack status: {stack.__str__()}")
    # print(f"This is the stack status: {stack.__str__()} \nAnd this is the top_index element {stack.top()}")

    # print("Emptying the stack")
    # stack.pop()
    # print(f"This is the stack status: {stack.__str__()} \nAnd this is the top_index element {stack.top()}")

    # print(f"The Stack is empty... Checking the last function pop()... and the result is: {stack.pop()}")