from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    vertex: int
    parent: Node
    

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

node2 = Node(4, Node(5, Node(6, None)))
node2.parent.parent.parent = node2

print(node1)
node1.extend(node2)
print(node1)
