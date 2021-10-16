import datetime
now = datetime.datetime.now()


class Factura:

    def __init__(self):
        self.hora_salida = now.hour, now.minute
        self.items = []  # se llena de productos

    def recibe_item_comprado(self, item):
        self.items.append(item)

    def muestra_factura(self):
        print(f"Hora de salida: {self.hora_salida}")
        for i in self.items:
            print(f'{i}')

    def guarda_en_archivo(self):
        with open("factura.csv", 'a') as f:
            f.write(f"{self.hora_salida}")
            for i in self.items:
                f.write(f"{i}")
            f.write("\n")
