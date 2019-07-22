
import random

ciudades = ['Santiago', 'La vega', 'Moca']
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo','Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
montos = [1000, 1500, 2000, 2500, 3000, 3500]
    
f = open("dataset.txt", "a")    
print(f"Ciudad\tMes\tMontoVenta", file=f)
for i in range(1000):   
    print(f"{random.choice(ciudades)}\t{random.choice(meses)}\t{random.choice(montos)}", file=f)

f.close()
