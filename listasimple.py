class Nodo:
    def __init__(self, dato = None):
        dato=dato
        sig=None

class ListaSimple:
    def __init__(self):
        cabeza = None

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
        while (final.cabeza):
            final = final.sigval
        final.sigval = Nodo

    def alMedio(self, actual, dato):
        if actual is None:
            print("The mentioned node is absent")
            return

        nuevo = Nodo(dato)
        nuevo.sig = actual.sigval
        actual.sig = nuevo

    def Remover(self, id):
        actual = self.head

        if (actual is not None):
            if (actual.dato == id):
                self.head = actual.sig
                actual = None
                return
        while (actual is not None):
            if actual.dato == id:
                break
            prev = actual
            actual = actual.sig

        if (actual == None):
            return

        prev.sig = actual.sig
        actual = None

