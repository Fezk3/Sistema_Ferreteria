from factura import Factura
from producto import Producto
from ferreteria import Ferreteria

if __name__ == '__main__':

    '''
    p = Producto("Leche", "12", 1000)
    fac = Factura()
    fac2 = Factura()
    p1 = Producto("tabla", "12", 1233)

    fac.recibe_item_comprado(p)
    fac.recibe_item_comprado(p1)
    fac.guarda_en_archivo()
    # fac.muestra_factura()
   '''
    # ferre = Ferreteria()
    # ferre.menuPrincipal()

    from listadouble import ListaDobleEnlazada

    l = ListaDobleEnlazada()
    l.agregar(1)
    l.agregar(22)
    l.agregar(333)
    l.agregar(4444)
    l.agregar(55555)
    l.eliminar(0)
    print(l.insertar(88888888888, -1))
    print(l)
