from factura import Factura
from producto import Producto
from ferreteria import Ferreteria
import time
from cliente import Cliente

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

    ferre = Ferreteria()
    ferre.menuPrincipal()
    ferre.menuCompra()
'''
    from factura import Factura
    from cola_clientes import ColaClientes

    fact = Factura()
    ca = ColaClientes()
    cli = Cliente("Victor", "13")
    cli.agregar_producto_carrito(Producto('Puerta Roble', "7", 90000))
    ca.agregar_cliente(cli)

    for cliente in ca.cola_clientes:
        print("Esperando a que se termine de atender al cliente de adelante")
        time.sleep(10)
        fact.recibe_item_comprado(cliente.saca_producto_carrito())
    fact.guarda_en_archivo()

'''



