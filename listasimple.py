class Nodo:
    def __init__(self, dato = None):
        dato=dato
        sig=None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def __repr__(self):
        actual=self.cabeza
        salida=""
        while actual is not None:
            salida+=f'{self.__repr__()}\n'
            actual=actual.sig
        return salida

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

        nuevo = Node(dato)
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