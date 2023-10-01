#!/usr/bin/python3
"""This module contains an implementation of a node and Singly linked list."""


class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            new_node = Node(value)
            self.__head = new_node
        else:
            copy = self.__head
            print("head", self.__head)
            while copy is not None:
                print(f"inserting {value}")
                if copy.data > value:
                    new_node = Node(value, copy)
                    print("newnode", new_node)
                    copy = new_node
                    break
                if copy.next_node is None:
                    new_node = Node(value)
                    copy.next_node = new_node
                    break
                print("copy", copy)

    def __str__(self):
        if self.__head is None:
            return
        str_rep = ""
        while self.__head is not None:
            str_rep += "{:d}".format(self.__head.data)
            if self.__head.next_node is not None:
                str_rep += "\n"
            self.__head = self.__head.next_node
        return str_rep


sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
