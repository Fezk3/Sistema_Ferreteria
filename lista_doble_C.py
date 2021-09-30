class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None



def insertEnd(value):
    global start

    if (start == None):
        new_node = Node(0)
        new_node.data = value
        new_node.next = new_node.prev = new_node
        start = new_node
        return

    last = (start).prev


    new_node = Node(0)
    new_node.data = value

    new_node.next = start

    (start).prev = new_node

    new_node.prev = last

    last.next = new_node


def insertBegin(value):
    global start


    last = (start).prev

    new_node = Node(0)
    new_node.data = value

    new_node.next = start
    new_node.prev = last

    last.next = (start).prev = new_node


    start = new_node


def insertAfter(value1, value2):
    global start
    new_node = Node(0)
    new_node.data = value1


    temp = start
    while (temp.data != value2):
        temp = temp.next
    next = temp.next


    temp.next = new_node
    new_node.prev = temp
    new_node.next = next
    next.prev = new_node


def display():
    global start
    temp = start


    while (temp.next != start):
        print(temp.data, end=" ")
        temp = temp.next

    print(temp.data)

    
    last = start.prev
    temp = last
    while (temp.prev != last):
        print(temp.data, end=" ")
        temp = temp.prev

    print(temp.data)
