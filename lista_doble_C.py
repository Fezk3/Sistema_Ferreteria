class Nodo:
    def __init__(self, dato = None):
        self.dato = dato
        self.anterior = self
        self.siguiente = self

class DCLL:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = self
        self.siguiente = self

    def __repr__(self):
        string = ""

        if (self.ini is None):
            string += "La lista esta vacia"
            return string

        string += f"Lista:\n{self.ini.da}"
        actual = self.ini.siguiente
        while (actual != self.ini):
            string += f" -> {actual.dato}"
            actual = actual.siguiente
        return string

    def agregar(self, dato):
        self.insert(dato, self.cont)
        return

    def insertar(self, dato, num):
        if (num > self.cont) | (num < 0):
            raise ValueError(f"numero fuera del rango: {num}, rango: {self.cont}")

        if self.ini is None:
            self.ini = Node(dato)
            self.cont = 1
            return

        actual = self.ini
        if (num is 0):
            actual = actual.anterior
        else:
            for _ in range(num - 1):
                actual = actual.siguiente

        actual.siguiente.anterior = Node(dato)
        actual.siguiente.anterior.siguiente, actual.siguiente.anterior.anterior = actual.siguiente, actual
        actual.siguiente = actual.siguiente.anterior
        if (num is 0):
            self.ini = self.ini.anterior
        self.cont += 1
        return

    def eliminar(self, num):
        if (num >= self.cont) | (num < 0):
            raise ValueError(f"numero fuera del rango: {num}, rango: {self.cont}")

        if self.cont is 1:
            self.ini = None
            self.cont = 0
            return

        target = self.ini
        for _ in range(num):
            target = target.siguiente

        if target is self.ini:
            self.ini = self.ini.siguiente

        target.anterior.siguiente, target.siguiente.anterior = target.siguiente, target.anterior
        self.cont -= 1

    def num(self, dato):
        actual = self.ini
        for i in range(self.cont):
            if (actual.dato is dato):
                return i
            actual = actual.siguiente
        return None

    def get(self, num):
        if (num >= self.cont) | (num < 0):
            raise ValueError(f"numero fuera del rango: {num}, rango: {self.cont}")

        actual = self.ini
        for _ in range(num):
            actual = actual.siguiente
        return actual.dato

    def size(self):
        return self.cont

    def display(self):
        print(self)
