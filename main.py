from factura import Factura
from producto import Producto

if __name__ == '__main__':

<<<<<<< HEAD
from ferreteria import Ferreteria

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
=======
    '''
    p = Producto("Leche", "12", 1000)
    fac = Factura()
    fac2 = Factura()
    p1 = Producto("tabla", "12", 1233)
>>>>>>> fact

    fac.recibe_item_comprado(p)
    fac.recibe_item_comprado(p1)
    fac.guarda_en_archivo()
    # fac.muestra_factura()

    '''
<<<<<<< HEAD
    lista = ListaDobleEnlazada()
    lista.agregar(1)
    lista.agregar(88)
    lista.agregar(789)
    print(lista.__repr__())
    print("Eliminando")
    lista.eliminar(0)
    print(lista.__repr__())
    lista.insertar(777, 1)
    print(lista.__repr__())
    print(f"Cantidad de nodos {lista.cantidad_nodos}")
'''
    '''lista = ListaDobleCircular()
    p1 =Producto("tablas de madera",21,2000)
    lista.agregar(p1)
    lista.display()
    print(lista.__repr__())'''

    ferre = Ferreteria()
    ferre.menuPrincipal()
=======
>>>>>>> fact
