class Nodo:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class ListaDobleEnlazada:

    def __init__(self):
        self.ini = None
        self.finale = None
        self.cantidad_nodos = 0

    def agregar(self, data):

        if self.ini is None:
            self.ini = Nodo(data)
            self.finale = self.ini
            self.cantidad_nodos += 1
            return
        
        self.finale.next = Nodo(data)
        self.finale.next.previous = self.finale
        self.finale = self.finale.next
        self.cantidad_nodos += 1

    def insertar(self, data, index):
        if (index > self.cantidad_nodos) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.cantidad_nodos}")

        if index is self.cantidad_nodos:
            self.agregar(data)
            return

        if index is 0:
            self.ini.previous = Nodo(data)
            self.ini.previous.next = self.ini
            self.ini = self.ini.previous
            self.cantidad_nodos += 1
            return

        start = self.ini
        for _ in range(index):
            start = start.next
        start.previous.next = Nodo(data)
        start.previous.next.previous = start.previous
        start.previous.next.next = start
        start.previous = start.previous.next
        self.cantidad_nodos += 1
        return

    def eliminar(self, index):
        if (index >= self.cantidad_nodos) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.cantidad_nodos}")

        if index is 0:
            self.ini = self.ini.next
            self.ini.previous = None
            self.cantidad_nodos -= 1
            return

        if index is (self.cantidad_nodos - 1):
            self.finale = self.finale.previous
            self.finale.next = None
            self.cantidad_nodos -= 1
            return

        start = self.ini
        for i in range(index):
            start = start.next
        start.previous.next, start.next.previous = start.next, start.previous
        self.cantidad_nodos -= 1
        return

    def __repr__(self):
        string = ""

        if (self.ini is None):
            string += "Doubly Linked List Empty"
            return string

        string += f"Doubly Linked List:\n{self.ini.data}"
        start = self.ini.next
        while (start != None):
            string += f" -> {start.data}"
            start = start.next
        return string
