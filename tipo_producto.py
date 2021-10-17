import csv
from producto import Producto
from pila import Pila

# sus objetos van a estar contenidos dentro de la DDE de secciones y va a contener pilas de los
# productos especificos de su tipo, para llenar las pilas, luego de crear el tipo de producto
# se les envia el nombre del archivo del cual van a contener los objetos


class tipoProducto:

    def __init__(self, tipoP):
        self.tipoP = tipoP
        self.producto1 = Pila()
        self.producto2 = Pila()
        #self.llena_producto1("puertaPino")
        #self.llena_producto2("puertaRoble")

    def llena_producto1(self, leerde):
        with open(f'{leerde}.csv', 'r') as f:
            csv_reader = csv.reader(f)
            for obj in csv_reader:
                self.producto1.agreagar(Producto(obj[0], obj[1], int(obj[2])))

    def llena_producto2(self, leerde):
        with open(f'{leerde}.csv', 'r') as f:
            csv_reader = csv.reader(f)
            for obj in csv_reader:
                self.producto2.agreagar(Producto(obj[0], obj[1], int(obj[2])))
    def agregaProducto(self, producto):
        self.producto2.agreagar(producto)
    def __repr__(self):
        string=""
        string = f'Tipo de producto: {self.tipoP}\n\nProductos:'

        string+= f'{self.producto1.top()} Cantidad: {self.producto1.tamnaio()}\n'
        return string
'''
    Ejp:
        puerta = tipoProducto("Puerta") 
        puerta.llena_producto1("puertaPino")
        puerta.llena_producto2("puertaRoble")
        
        -> meter a la listaDobleEnlazada de Tipos de productos

'''