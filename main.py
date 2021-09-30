# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from cliente import Cliente
from producto import Producto

from listadouble import ListaDobleEnlazada

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    lista = ListaDobleEnlazada()
    lista.agregar(1)
    lista.agregar(88)
    lista.agregar(789)
    print(lista.__repr__())
    print("Eliminando")
    lista.eliminar(0)
    print(lista.__repr__())
    lista.insertar(777, 2)
    print(lista.__repr__())
    print(f"Cantidad de nodos {lista.cantidad_nodos}")
