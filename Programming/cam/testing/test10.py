from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    vertex: int
    parent: Node

    def reverse(self) -> None:
        '''
        reverses the order of self
        '''
        next_node = self
        new_node = Node(next_node.vertex, None)
        while next_node.parent != None and next_node.parent != self:
            new_node = Node(next_node.vertex, new_node)

            next_node = next_node.parent

        self = new_node

    @property
    def does_loop(self) -> bool:
        '''
        return if it loops
        '''
        next_node = self
        while next_node.parent != None and next_node.parent != self:
            next_node = next_node.parent

        if next_node.parent == self:
            return True
        else:
            return False

    def make_it_loop(self) -> None:
        '''
        converts a non looping linkedlist to a looping linkedlist
        '''
        next_node = self
        while next_node.parent != None and next_node.parent != self:
            next_node = next_node.parent

        next_node.parent = self
        
    @property
    def last_node(self) -> Node:
        '''
        returns last node in the linkedlist
        '''
        next_node = self
        while next_node.parent != None and next_node.parent != self:
            next_node = next_node.parent

        return next_node
   
    @classmethod
    def reversed(cls, node: Node) -> Node:
        '''
        reverses the argument node
        '''
        print('\n\nnew call ')
        new_node = Node(node.vertex, None)
        print(new_node, 'new_node')
        print()
        next_node = node.parent
        while next_node.parent != None and next_node.parent != node:
            new_node = Node(next_node.vertex, new_node)
            print(new_node, 'new_node')

            next_node = next_node.parent
            print(next_node, 'next_node')
            print()

        new_node = Node(next_node.vertex, new_node)
        print(new_node, 'new_node')

        if node.does_loop:
            new_node.make_it_loop()

        return new_node

    def extend(self, other_node: Node) -> None:
        '''
        just like list.extend() it extends the current linkedlist with other linkedlist
        finds the last node, the node with parent none (or head for looping linkedlists) 
        then attaches the other_node node to it and joins the loop or not depending on 
        original state

        :param other_node: the node to make parent of the last node in the current linkedlist
        :return: the new head Node of the extended linkedlist
        '''
        next_node = self
        while next_node.parent != None and next_node.parent != self:
            next_node = next_node.parent


        if next_node.parent == None:
            # just join
            next_node.parent = other_node

        else:
            next_node.parent = other_node

            # must join the last node with the first node to make the loop
            next_node2 = other_node
            while next_node2.parent != None and next_node2.parent != other_node:
               next_node2 = next_node2.parent

            next_node2.parent = self

    def __repr__(self) -> str:
        return f"{self.vertex}, Parent: {self.parent.vertex}"

    def __str__(self) -> str:
        '''
        string representation of the linkedlist made of nodes
        '''

        string_representation = ""

        next_node = self
        while next_node.parent != None and next_node.parent != self:
            string_representation += f"{next_node.vertex}, "
            next_node = next_node.parent

        string_representation += f"{next_node.vertex}, "

        if next_node.parent == self:
            string_representation += f"{next_node.parent.vertex}, ... (loops)"

        else:
            string_representation += f"{next_node.parent}"

        return string_representation


node1 = Node(1, Node(2, Node(3, None)))
node1.parent.parent.parent = node1
print(node1.last_node)

node2 = Node(4, Node(5, Node(6, None)))
node2.parent.parent.parent = node2

# print(node1)
# node1.extend(node2)
# print(node1)

# node1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, None))))))))
# node1.parent.parent.parent.parent.parent.parent.parent.parent = node1

# print(node1)
# node1 = Node.reversed(node1)
# print('\nreturn: ', node1)
