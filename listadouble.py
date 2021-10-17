class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.sig = None
        self.ante = None


class ListaDobleEnlazada:

    def __init__(self):
        self.ini = None
        self.ulti = None
        self.tamanio = 0

    def si_vacia(self):
        return self.ini is None

    def agregar(self, dato):

        if self.si_vacia():  # si la lista esta vacia se agrega como inicio
            self.ini = self.ulti = Nodo(dato)
        else:  # si la lista tiene nodos
            aux = self.ulti
            self.ulti = aux.sig = Nodo(dato)
            self.ulti.ante = aux
        self.tamanio += 1

    def get_tamanio(self):
        return self.tamanio

    def insertar(self, dato, posi):  # aniade un nodo en una posicion dada, mientras que esta sea valida
        if posi > self.tamanio or posi < 0:
            return f"La posicion solicitada no puede ser usada, use una valida. Tamanio de la lista {self.tamanio}"

        if posi is self.tamanio:  # si es la posicion igual al numero de nodos de la lista
            self.agregar(dato)
            return

        if posi == 0:  # si es la posicion inicial de la lista
            self.ini.ante = Nodo(dato)
            self.ini.ante.sig = self.ini
            self.ini = self.ini.ante
            self.tamanio += 1
            return

        inicial = self.ini  # si es una posicion entre algun lugar de la lista
        for ele in range(posi):
            inicial = inicial.sig
        inicial.ante.sig = Nodo(dato)
        inicial.ante.sig.ante = inicial.ante
        inicial.ante.sig.sig = inicial
        inicial.ante = inicial.ante.sig
        self.tamanio += 1
        return

    def eliminar(self, posi):  # elimina un nodo por su posicion en la lista, mientras esta sea valida
        if posi >= self.tamanio or posi < 0:
            return f"La posicion solicitada no puede ser usada, use una valida. Tamanio de la lista {self.tamanio}"

        if self.tamanio == 1:
            self.ulti = None
            self.ini = None
            self.tamanio -=1
            return

        if posi == 0:  # si el nodo a eliminar es el primero
            self.ini = self.ini.sig
            self.ini.ante = None
            self.tamanio -= 1
            return

        if posi is (self.tamanio - 1):  # si el nodo a eliminar es el ultimo
            self.ulti = self.ulti.ante
            self.ulti.sig = None
            self.tamanio -= 1
            return

        inicial = self.ini  # si el nodo a eliminar esta en medio de la lista
        for ele in range(posi):
            inicial = inicial.sig
        inicial.ante.sig, inicial.sig.ante = inicial.sig, inicial.ante
        self.tamanio -= 1
        return

    def __repr__(self):  # para imprimir el objeto (como un toString)
        string = ""

        if self.ini is None:
            string += "Lista vacia"
            return string

        string += f"\nLista:\n\n{self.ini.dato}"
        inicial = self.ini.sig
        while inicial is not None:
            string += f"{inicial.dato}"
            inicial = inicial.sig
        return string

    def get(self, num):  # retorna el objeto de una posicion dada, mientras esta sea valida
        if num > self.tamanio or num < 0:
            return f"La posicion solicitada no puede ser usada, use una valida. Tamanio de la lista {self.tamanio}"

        actual = self.ini
        for ele in range(num):
            actual = actual.siguiente
        return actual.dato
