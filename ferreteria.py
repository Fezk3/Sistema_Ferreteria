from sucursal import Sucursal
from sucursal import Seccion
from seccion import tipoProducto
from tipo_producto import Producto
from cliente import Cliente

class Ferreteria:
    def __init__(self):
        self.listaSucursal = []
        self.cont = 0
        self.sucursalesPorDefecto()

    def menuPrincipal(self):
        opc = ''
        print('\n\t\t\tBienvenido Amigo al Martillazo Feliz!!')
        while opc != "salir":
            print('1 - Menu Administrativo')
            print('2 - Menu de Cliente')
            print('3 - Para salir ')
            opc = input('Que desea realizar?\n')

            if opc == "1":
                self.menuAdministrativo()
            if opc == "2":
                self.menuCompra()
            if opc == "3":
                print("Gracias por visitarnos!")
                exit(0)


    def menuCompra(self):
        sucur = ""

        while sucur.isdigit() is not True:
            print("Digite el numero sucursal en la que desea realizar la compra:   ")
            print("1. Salir")
            for su in range(len(self.listaSucursal)):
                print(f"{su + 2}. Sucarsal de {self.listaSucursal[su].ubicacion}")
            sucur = input()

            if not sucur.isdigit():
                 print(f'Digito una opcion invalida')

        #if int(sucur) > len(self.listaSucursal):
        #    return f'Digito una opcion invalida'
        if sucur == "1":
            self.menuPrincipal()
        elif sucur == "2":
            self.menu_sucursal(1)
        elif sucur == "3":
            self.menu_sucursal(2)
        elif sucur == "4":
            self.menu_sucursal(3)
        else:
            print("La sucursal aun no esta disponible")
            self.menuCompra()

    def menu_sucursal(self, n_su):
        n_su -= 1
        mad = True
        opci = ""
        op2 = ""

        while opci.isdigit() is not True:
            print(f"Bienvenido a la sucursal de {self.listaSucursal[n_su].ubicacion}")
            print(f"Digite el numero de la seccion de la que desea ver los tipos de productos: ")
            for n in range(self.listaSucursal[n_su].listaSeccion.tamanio):
                print(f"{n + 1}. {self.listaSucursal[n_su].listaSeccion.get(n).get_num_nomb()}")
            opci = input()

            if not opci.isdigit():
                print(f'Digito una opcion invalida')

        if opci == "1":
            self.mostrar_maderas(n_su)
            mad = False
        elif opci == "2":
            self.mostrar_metales(n_su)
        else:
            print(f'Digito una opcion invalida')
            self.menu_sucursal(n_su)

        while op2.isdigit() is not True:
            print("Digite el numero del que quiera ver sus productos especificos: ")
            op2 = input()

            if not op2.isdigit():
                print(f'Digito una opcion invalida')

        if op2 == "1" and mad is not True:  # TABLAS
            tabla = self.listaSucursal[n_su].listaSeccion.get(0).retornaTipo('Tabla')  # tablas
            print(f'Tablas disponibles: ')
            print(tabla.muestra_tops())
            self.compra(n_su, tabla)
        elif op2 == "2" and mad is not True:  # PUERTAS
            puerta = self.listaSucursal[n_su].listaSeccion.get(0).retornaTipo('Puerta')  # puertas
            print(f'\nPuertas disponibles: ')
            print(puerta.muestra_tops())
            self.compra(n_su, puerta)
        elif op2 == "1" and mad is True:  # PERLINS
            perlin = self.listaSucursal[n_su].listaSeccion.get(1).retornaTipo('Perlin')  # perlins
            print(f'Perlins disponibles: ')
            print(perlin.muestra_tops())
            self.compra(n_su, perlin)
        else:
            print(f'Digito una opcion invalida')
            self.menu_sucursal(n_su)

    def mostrar_maderas(self, n_su):  # muestra los tipos de producto
        maderas = self.listaSucursal[n_su].listaSeccion.get(0)
        print("Los tipos de producto de los que dispone esta seccion son:")
        maderas.muestra_tipo()

    def mostrar_metales(self, n_su):
        metales = self.listaSucursal[n_su].listaSeccion.get(1)
        print("Los tipos de producto de los que dispone esta seccion son:")
        metales.muestra_tipo()

    def compra(self, n_su, cual):
        p1 = False
        seguir = True
        y = ''
        p = ''
        op3 = ''
        while y.isdigit() is not True:
            print("Desea comprar un producto?")
            print("1. Si        2. No")
            y = input()

            if not y.isdigit():
                print(f'Digito una opcion invalida')

        if y == "1":  # si quiere comprar
            c = Cliente()
            while seguir:  # mientras quiera comprar escoge de la misma categoria

                print(cual.muestra_tops())
                print("Digite el numero del procuto que quiere comprar: ")
                p = input()

                if not p.isdigit():
                    print(f'Digito una opcion invalida')

                if p == "1":
                    c.agregar_producto_carrito(cual.producto1.sacar())  # aniade producto al carrito de la pila de productos
                    p1 = True
                elif p == "2" and p1 is not True:
                    c.agregar_producto_carrito(cual.producto2.sacar())  # aniade producto al carrito de la pila de productos
                else:
                    print("Opcion invalida")
                    self.menuCompra()

                    #  desea seguir comprando?

                print("Desea seguir comprando?")
                print("1. Si        2. No")
                op3 = input()

                if not op3.isdigit():
                    print(f'Digito una opcion invalida')

                if op3 == "1":
                    seguir = True
                elif op3 == "2":
                    seguir = False
                    self.listaSucursal[n_su].atiende_cliente(c)  # cliente pasa a la caja por su factura
                    self.menuCompra()

        elif y == "2":
            self.menuCompra()
        else:
            print(f'Digito una opcion invalida')  # vuelve al menu compra
            self.compra(n_su, cual)

    def menuAdministrativo(self):
        opc = ""
        while opc != "salir":
            print('\n\n1 - Agregar una sucursal')
            print('2 - Ver las sucursales')
            print('3 - Eliminar')
            print('4 - Agregar elementos en ferreteria')
            print('Para salir digite "salir"')
            opc = input('Que desea realizar?\n')

            if opc == "1":
                self.ingresarSucursal()
            elif opc == "2":
                self.imprimirSucursal()
            elif opc == "3":
                self.eliminar()
            elif opc == "4":
                self.agregarEnSucursal()
            else:
                return f'Digito una opcion invalida'

    def ingresarSucursal(self):
        nombreSu = ""
        nombreSu = input("Digite la ubicacion de la sucursal\n")
        sucursal = Sucursal(nombreSu, self.cont)

        ciclo = ''
        ciclo2 = ''
        ciclo3 = ''
        ciclo = input("cuantas secciones desea agregar: ")
        i = 0
        if not ciclo.isdigit():
            return f'Digito una opcion invalida'
        while int(ciclo) > i:
            nombreSe = ""
            nombreSe = input("Digite el nombre de la seccion:\n")
            seccion = Seccion(nombreSe, i)
            i += 1

            ciclo2 = input("Cuantos tipos de productos desea agregar: ")
            if not ciclo2.isdigit():
                return f'Digito una opcion invalida'
            j = int(ciclo2)
            while j > 0:
                tipo = ""
                tipo = input("Digite el nombre de tipo de productos que desea agregar:\n")
                tipoP = tipoProducto(tipo)
                '''
                ciclo3 = ""
                
                ciclo3 = input("Cuantos productos desea agregar: ")
                if not ciclo3.isdigit():
                    return f'Digito una opcion invalida'
                k = 0
                while k<int(ciclo3):
                    nom = ""
                    nom = input('Digite el nombre del producto\n')
                    precio =""
                    precio = input('Digite el precio de este producto\n')
                    if not precio.isdigit():
                        return f'Digito una opcion invalida\n'
                    cant = ""
                    cant = input('Digite el stock de este producto\n')

                    if not cant.isdigit():
                        return f'Digito una opcion invalida'
                    l = 0
                    while l < int(cant):
                        producto = Producto(nom,l,precio)
                        tipoP.agregaProducto(producto)
                        l+=1

                    tipoP.agregaPila()
                    k+=1
                    '''
                j -= 1
                seccion.agregarProducto(tipoP)

            sucursal.agregaSeccion(seccion)

        self.listaSucursal.insert(self.cont, sucursal)
        self.cont += 1

    def eliminar(self):
        opc = ""
        while opc != "salir":
            print('Que desea eliminar?')
            print('1 -Sucursal')
            print('2 -Seccion')
            print('3 -Tipo de producto')
            print('Para salir digite "salir"')

            opc = input("Elija una opcion: ")

            if not opc.isdigit():
                return f'Digito una opcion invalida'

            if opc == "1":
                print(self.eliminarSucursal())

            if opc == "2":
                print(self.eliminarSeccion())

            if opc == "3":
                print(self.eliminarTipo())


    def imprimirSucursal(self):
        for sucursal in self.listaSucursal:
            print(sucursal)

    def eliminarSucursal(self):
        self.imprimirSucursal()
        opc = input("Digite el id de la sucursal que desea elimjnar ")

        if not opc.isdigit() or int(opc) >= len(self.listaSucursal):
            return f'Digito una opcion invalida'

        index = int(opc)
        del self.listaSucursal[index]
        return f'Sucursal eliminada exitosamente'

    def eliminarSeccion(self):
        self.imprimirSucursal()
        opc = input("Digite el id de la sucursal en la que esta la seccion que desea eliminar ")

        if not opc.isdigit() or int(opc) >= len(self.listaSucursal):
            return f'Digito una opcion invalida'

        index = int(opc)
        print(self.listaSucursal[index].listaSeccion)
        eliminado = input("digite la seccion que desea eliminar ")
        tam = self.listaSucursal[index].listaSeccion

        if not eliminado.isdigit() or int(eliminado) >= tam.get_tamanio():
            return f'Digito una opcion invalida'

        self.listaSucursal[index].eliminarSeccion(int(eliminado))
        return f'Seccion eliminada exitosamente'

    def eliminarTipo(self):
        self.imprimirSucursal()
        opc = input("Digite el id de la sucursal ")

        if not opc.isdigit() or int(opc) >= len(self.listaSucursal):
            return f'Digito una opcion invalida'

        index = int(opc)
        print(self.listaSucursal[index])
        seccion = input("digite la seccion donde se encuentra el tipo de producto ")
        tam = self.listaSucursal[index].listaSeccion

        if not seccion.isdigit() or int(seccion) >= tam.get_tamanio():
            return f'Digito una opcion invalida'

        print(self.listaSucursal[index].retornarSeccion(int(seccion)))
        tipo = input('Digite el tipo de producto que desee eliminar ')

        if not opc.isdigit() or int(tipo) >= self.listaSucursal[index].retornarSeccion(int(seccion)).listaTipoProductos.get_tamanio():
            return f'Digito una opcion invalida'

        self.listaSucursal[index].retornarSeccion(int(seccion)).eliminarTipo(int(tipo))
        return f'Tipo de producto eliminado exitosamente'

    def agregarEnSucursal(self):
        opc = ""
        while opc != "salir":
            print('Que desea agregar?')
            print('1 -Sucursal')
            print('2 -Seccion')
            print('3 -Tipo de producto')
            print('Para salir digite "salir"')

            opc = input("Elija una opcion: ")

            if not opc.isdigit():
                return f'Digito una opcion invalida'

            if opc == "1":
                print(self.agregarSucursal())

            if opc == "2":
                print(self.agregarSeccion())

            if opc == "3":
                print(self.agregarTipo())

    def agregarSucursal(self):
        index = ""
        index = input('Digite la posicion en el que quiere la sucursal: ')
        if not index.isdigit() or int(index) > len(self.listaSucursal):
            return f'Digito una opcion invalida'
        nombre = ""

        nombre = input('Ingrese la ubicacion de la sucursal:\n')
        sucursal =Sucursal(nombre, int(index))
        self.listaSucursal.insert(int(index),sucursal)
        i=int(index)+1
        while i < len(self.listaSucursal):
            self.listaSucursal[i].id+=1
            i+=1

        self.cont+=1
        return f'Sucursal guardada exitosamente'


    def agregarSeccion(self):
        self.imprimirSucursal()
        opc = input("Digite el id de la sucursal ")

        if not opc.isdigit() or int(opc) >= len(self.listaSucursal):
            return f'Digito una opcion invalida'

        print(self.listaSucursal[int(opc)])
        pos = ""
        pos = input('Digite la posicion en la que quiere agregar la seccion')
        if not pos.isdigit() or int(pos) > self.listaSucursal[int(opc)].listaSeccion.get_tamanio():
            return f'Digito una opcion invalida'
        nombre = ""
        nombre = input('Digite el nombre de la seccion\n')
        seccion = Seccion(nombre,int(pos))
        self.listaSucursal[int(opc)].listaSeccion.insertar(seccion, int(pos))
        i=int(pos)+1
        while  self.listaSucursal[int(opc)].listaSeccion.get_tamanio() > i:
            self.listaSucursal[int(opc)].listaSeccion.get(i).numero+=1
            i+=1
        return f'Seccion guardada exitosamente'

    def agregarTipo(self):
        self.imprimirSucursal()
        opc = input("Digite el id de la sucursal ")

        if not opc.isdigit() or int(opc) >= len(self.listaSucursal):
            return f'Digito una opcion invalida'

        print(self.listaSucursal[int(opc)])
        pos = ""
        pos = input('Digite la seccion en la que quiere agregar el tipo de producto')
        if not pos.isdigit() or int(pos) >= self.listaSucursal[int(opc)].listaSeccion.get_tamanio():
            return f'Digito una opcion invalida'
        print(self.listaSucursal[int(opc)].retornarSeccion(int(pos)).listaTipoProductos)
        index = ""
        index = input('Digite la posicion en la que quiere el tipo de producto')
        if not index.isdigit() or int(index) > self.listaSucursal[int(opc)].retornarSeccion(int(pos)).listaTipoProductos.get_tamanio():
            return f'Digito una opcion invalida'

        tipo = ""
        tipo = input("Digite el nombre de tipo de productos que desea agregar:\n")
        tipoP = tipoProducto(tipo)
        '''
        ciclo3 = input("Cuantos productos desea agregar: ")
        if not ciclo3.isdigit():
            return f'Digito una opcion invalida'
        k = 0
        while k < int(ciclo3):
            nom = ""
            nom = input('Digite el nombre del producto\n')
            precio = ""
            precio = input('Digite el precio de este producto\n')
            if not precio.isdigit():
                return f'Digito una opcion invalida\n'
            cant = ""
            cant = input('Digite el stock de este producto\n')

            if not cant.isdigit():
                return f'Digito una opcion invalida'
            l = 0
            while l < int(cant):
                producto = Producto(nom, l, precio)
                tipoP.agregaProducto(producto)
                l += 1

            tipoP.agregaPila()
            k += 1
        '''
        self.listaSucursal[int(opc)].retornarSeccion(int(pos)).agregarProductoEspecifico(tipoP,int(index))
        return f'Tipo de producto guardado exitosamente'

    def sucursalesPorDefecto(self):
        sucursal = Sucursal('Alajuela', 1)
        sucursal2 = Sucursal('Heredia', 2)
        sucursal3 = Sucursal('Cartago', 3)

        for n in range(3):
            if n == 0:
                seccion = Seccion('Madera', 0)
                tipo = tipoProducto('Tabla')
                tipo2 = tipoProducto('Puerta')
                tipo.llena_producto1('tablaPino')
                tipo.llena_producto2('tablaRoble')
                tipo2.llena_producto1('puertaPino')
                tipo2.llena_producto2('puertaRoble')
                seccion.agregarProducto(tipo)
                seccion.agregarProducto(tipo2)
                seccion2 = Seccion('Hierro', 1)
                tipo3 = tipoProducto('Perlin')
                tipo3.llena_producto1('perlin')
                seccion2.agregarProducto(tipo3)
                sucursal.agregaSeccion(seccion)
                sucursal.agregaSeccion(seccion2)
                self.listaSucursal.append(sucursal)
            elif n == 1:
                seccion = Seccion('Madera', 0)
                tipo = tipoProducto('Tabla')
                tipo2 = tipoProducto('Puerta')
                tipo.llena_producto1('tablaPino')
                tipo.llena_producto2('tablaRoble')
                tipo2.llena_producto1('puertaPino')
                tipo2.llena_producto2('puertaRoble')
                seccion.agregarProducto(tipo)
                seccion.agregarProducto(tipo2)
                seccion2 = Seccion('Hierro', 1)
                tipo3 = tipoProducto('Perlin')
                tipo3.llena_producto1('perlin')
                seccion2.agregarProducto(tipo3)
                sucursal2.agregaSeccion(seccion)
                sucursal2.agregaSeccion(seccion2)
                self.listaSucursal.append(sucursal2)

            else:
                seccion = Seccion('Madera', 0)
                tipo = tipoProducto('Tabla')
                tipo2 = tipoProducto('Puerta')
                tipo.llena_producto1('tablaPino')
                tipo.llena_producto2('tablaRoble')
                tipo2.llena_producto1('puertaPino')
                tipo2.llena_producto2('puertaRoble')
                seccion.agregarProducto(tipo)
                seccion.agregarProducto(tipo2)
                seccion2 = Seccion('Hierro', 1)
                tipo3 = tipoProducto('Perlin')
                tipo3.llena_producto1('perlin')
                seccion2.agregarProducto(tipo3)
                sucursal3.agregaSeccion(seccion)
                sucursal3.agregaSeccion(seccion2)
                self.listaSucursal.append(sucursal3)
