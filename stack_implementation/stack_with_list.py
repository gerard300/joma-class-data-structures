class Stack:
    """
    Stack is an ADT (Abstract Data Type)

    Stack Rules:
        + You cannot pop the last element of the stack
        + If You want to pop off the first element you have to pop off all the previous elements
    
    Stack can be implemented with different data structures:
        + Fixed arrays: in case of Python Fixed Arrays doesn't exist
            push    -> O(1)
            pop     -> O(1)
            is_empty    -> O(1)
        + Dynamic arrays: in case of Python Dynamic arrays are Python lists
            push    -> Amortized O(1)
            pop     -> Amortized O(1)
            is_empty    -> O(1)
        + Linked List Tail
        + Linked List Head
    """
    def __init__(self):
        self.stack_list = []
        self.top_index = 0 # Index of the last element pushed of the Stack. 0 when stack is empty and 1 when It has 1 element

    def __str__(self) -> str:
        return " | ".join(map(str,self.stack_list))+"*"
    # Stacks have two basic operations
    def push(self,element):
        # Push elements in the stack following the LIFO (Last In First Out)
        # We don't have to check if the arrays exceed the maximum because Python uses a List which is inmutable and a Dynamic Array
        self.stack_list.append(element)
        self.top_index +=1

    def pop(self):
        # Removes the most recently added element
        if self.is_empty():
            return None
        else:
            self.stack_list.pop()
            self.top_index -= 1

    def top(self) -> str:
        # Allows you to get the last element you pushed in without popping
        if self.is_empty():
            return None
        else:
            return str(self.stack_list[self.top_index-1])

    def is_empty(self) -> bool:
        # Tells you if the Stack is empty
        return self.top_index == 0

if __name__ == '__main__':
    stack = Stack()
    print(f"Stack is empty? --> {stack.is_empty()}")
    print("Populating the stack with the next 3 elements: [1,2,3]")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"This is the stack status: {stack.__str__()} \nAnd this is the top_index element {stack.top()}")

    print("Popping the last two elements of the Stack [2,3]")
    stack.pop()
    stack.pop()
    print(f"This is the stack status: {stack.__str__()} \nAnd this is the top_index element {stack.top()}")

    print("Emptying the stack")
    stack.pop()
    print(f"This is the stack status: {stack.__str__()} \nAnd this is the top_index element {stack.top()}")

    print(f"The Stack is empty... Checking the last function pop()... and the result is: {stack.pop()}")