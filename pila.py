class Pila:

    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agreagar(self, item):
        self.items.insert(0, item)

    def sacar(self):
        return self.items.pop()

    def tamnaio(self):
        return len(self.items)
