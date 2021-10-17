class Nodo:

    def __init__(self, dato):

        self.dato = dato
        self.ante = self
        self.sig = self


class ListaDobleCircular:

    def __init__(self):

        self.ini = None
        self.ante = self
        self.sig = self
        self.tamanio = 0

    def __repr__(self):  # para imprimir el objeto (como un toString)

        string = ""
        if self.ini is None:
            string += "\nLa lista esta vacia"
            return string

        string += f"\nLista:\n\n{self.ini.dato}"
        actual = self.ini.sig
        while actual != self.ini:
            string += f"{actual.dato}"
            actual = actual.sig
        return string

    def agregar(self, dato):  # agrega nodos en la ultima posicion de la lista, usa el contador global para saber donde
        self.insertar(dato, self.tamanio)
        return

    def insertar(self, dato, posi):  # aniade un nodo en una posicion dada, mientras que esta sea valida

        if posi > self.tamanio or posi < 0:
            return f"La posicion solicitada no puede ser usada, use una valida. Tamanio de la lista {self.tamanio}"

        if self.ini is None:  # si la lista esta vacia, se agrega en la primer posicion
            self.ini = Nodo(dato)
            self.tamanio = 1
            return

        actual = self.ini
        if posi == 0:
            actual = actual.ante
        else:
            for ele in range(posi - 1):
                actual = actual.sig

        actual.sig.ante = Nodo(dato)
        actual.sig.ante.sig, actual.sig.ante.ante = actual.sig, actual
        actual.sig = actual.sig.ante

        if posi == 0:
            self.ini = self.ini.ante
        self.tamanio += 1
        return

    def eliminar(self, posi):  # elimina un nodo por su posicion en la lista, mientras esta sea valida

        if posi >= self.tamanio or posi < 0:
            return f"La posicion solicitada no puede ser usada, use una valida. Tamanio de la lista {self.tamanio}"

        if self.tamanio == 1:  # si solo hay un elemento en la lista y este es eliminado
            self.ini = None
            self.tamanio = 0
            return

        target = self.ini  # busca el elemento a eliminar segun la posicion dada
        for ele in range(posi):
            target = target.sig

        if target is self.ini:  # si el nodo a eliminar es el inicial
            self.ini = self.ini.sig

        target.ante.sig, target.sig.ante = target.sig, target.ante  # eliminando nodo
        self.tamanio -= 1

    def get(self, posi):  # retorna el objeto de una posicion dada, mientras esta sea valida

        if posi >= self.tamanio or posi < 0:
            return f"La posicion solicitada no puede ser usada, use una valida. Tamanio de la lista {self.tamanio}"

        actual = self.ini
        for ele in range(posi):  # busca el nodo en la lista para devolverlo
            actual = actual.sig
        return actual.dato


    def get_tamanio(self):
        return self.tamanio

