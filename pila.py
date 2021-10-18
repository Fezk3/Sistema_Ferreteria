class Pila:

    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agreagar(self, item):
        self.items.insert(0, item)

    def sacar(self):
        if self.esta_vacia() is not True:
            return self.items.pop()

    def tamnaio(self):
        return len(self.items)

    def top(self):
        return self.items[0]
