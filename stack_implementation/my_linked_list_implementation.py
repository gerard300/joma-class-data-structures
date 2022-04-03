# Base example
class Node:
    # This class represents each node of the linked list
    def __init__(self, data):
        # The Node has this two main elements
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None # New part
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            if len(nodes) ==0:
                self.tail=self.head
            else:
                for elem in nodes:
                    node.next = Node(data=elem)
                    node = node.next
                    self.tail = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return f"Head Node: {self.head} and Tail Node: {self.tail}\n State: "+" -> ".join(map(str, nodes))  # Output is something like this: "a -> b -> c -> None"

    def __iter__(self):
        # The definition and implementation of this function is more Pythonic
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        # The node I'm going to put at the beginning, first needs to put at the previous HEAD!!
        node.next = self.head
        # Then your HEAD is pointing at your new node
        self.head = node

    def add_last(self, node):
        node.next = None
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        self.tail = current_node.next

    # def add_after(self, target_node_data, new_node):
    #     # This functions pass data of the target_node and a new node
    #     # First Check
    #     if self.head is None:
    #         raise Exception("List is empty...")
    #     for n in self:
    #         if target_node_data == n.data:
    #             new_node.next = n.next
    #             n.next = new_node
    #             return
    #     raise Exception(f"Node with data '{target_node_data}' not found")

    # def add_before(self, target_node_data, new_node):
    #     if self.head is None:
    #         raise Exception("List is empty...")
    #     if self.head.data == target_node_data:
    #         return self.add_first(new_node)
    #     for n in self:
    #         if n.next.data == target_node_data:
    #             new_node.next = n.next
    #             n.next = new_node
    #             return
    #     raise Exception(f"Node with data '{target_node_data}' not found")

    # def remove_node(self, target_node_data):
    #     if self.head is None:  # Difference between == and is??
    #         raise Exception("List is empty...")
    #     if self.head.data == target_node_data:
    #         # if self.head.next is None:
    #         #     self.
    #         self.head = self.head.next
    #         return
    #     prev_node = self.head
    #     for n in self:
    #         if n.data == target_node_data:
    #             prev_node.next == n.next
    #             return
    #         prev_node = n
    #     raise Exception(f"Node with data '{target_node_data}' not found")
    def get_head(self):
        return self.head
    def get_tail(self):
        return self.tail
