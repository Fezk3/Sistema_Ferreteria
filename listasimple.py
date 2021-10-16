class Nodo:
    def __init__(self, dato = None):
        self.dato=dato
        self.sig=None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def __repr__(self):

        string=""
        if self.cabeza is None:
            string += "La lista esta vacia"
            return string

        string += f"Lista:\n{self.cabeza.dato.__repr__()}"
        actual = self.cabeza.sig
        while actual != None:
            string += f" -> {actual}"
            actual = actual.sig
        return string


    def alfinal(self, nuevo):
        actual = Nodo(nuevo)
        if self.cabeza is None:
            self.cabeza = actual
            return
        final= self.cabeza

        while final:
            final = final.sig
        final.sig = nuevo


    def alMedio(self, actual, dato):
        if actual is None:
            print("The mentioned node is absent")
            return

        nuevo = Nodo(dato)
        nuevo.sig = actual.sigval
        actual.sig = nuevo

    def Remover(self, id):
        actual = self.cabeza

        if actual is not None:
            if actual.dato == id:
                self.cabeza = actual.sig
                actual = None
                return

        while actual is not None:
            if actual.dato == id:
                break
            prev = actual
            actual = actual.sig

        if actual == None:
            return

        prev.sig = actual.sig
        actual = None

    def get(self, id):
        actual =self.cabeza
        while actual is not None:
            if actual.dato is id:
                return actual.dato

        return None