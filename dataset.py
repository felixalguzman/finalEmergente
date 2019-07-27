import random

ciudades = ['Santiago de los Caballeros', 'La Romana', 'San Pedro de Macoris', 'La Altagracia', 'San Cristobal',
            'Puerto Plata', 'Mao', 'Esperanza', 'La vega', 'Moca']
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre',
         'Diciembre']

f = open("dataset.txt", "a")
# print(f"Ciudad,Mes,MontoVenta", file=f)
for i in range(1000):
    print(f"{random.choice(ciudades)}\t{random.choice(meses)}\t{random.randrange(1000, 9500)}", file=f)

f.close()
