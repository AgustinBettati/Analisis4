import csv
import numpy as np

from tp2.newtonFormula import coef

from tp2.newtonFormula import eval

file = open("resource/geo_pos.csv", 'r')  # read only

reader = csv.reader(file)

next(reader)  # reader es un iterable de las rows del csv

altura1 = []
latitud1 = []
longitud1 = []

altura2 = []
latitud2 = []
longitud2 = []

altura3 = []
latitud3 = []
longitud3 = []

altura4 = []
latitud4 = []
longitud4 = []

count = 0

# TODO metodo que no repita codigo
for row in reader:
    if count <= 30:
        altura1.append(float(row[0]))
        latitud1.append(float(row[1]))
        longitud1.append(float(row[2]))
    if 30 < count <= 60:
        altura2.append(float(row[0]))
        latitud2.append(float(row[1]))
        longitud2.append(float(row[2]))
    if 60 < count <= 90:
        altura3.append(float(row[0]))
        latitud3.append(float(row[1]))
        longitud3.append(float(row[2]))
    if count > 90:
        altura4.append(float(row[0]))
        latitud4.append(float(row[1]))
        longitud4.append(float(row[2]))
    count += 1

coefLat1 = coef(np.array(altura1), np.array(latitud1))
coefLat2 = coef(np.array(altura2), np.array(latitud2))
coefLat3 = coef(np.array(altura3), np.array(latitud3))
coefLat4 = coef(np.array(altura4), np.array(latitud4))

coefLong1 = coef(np.array(altura1), np.array(longitud1))
coefLong2 = coef(np.array(altura2), np.array(longitud2))
coefLong3 = coef(np.array(altura3), np.array(longitud3))
coefLong4 = coef(np.array(altura4), np.array(longitud4))

file = open("resource/interpolation.csv", "w")

file.write("Altura,Latitud,Longitud\n")

for i in range(0, 3000, 1):
    file.write(str(10000 - i))
    file.write(",")
    file.write(str(eval(np.array(coefLat1), np.array(altura1), 10000 - i)))
    file.write(",")
    file.write(str(eval(np.array(coefLong1), np.array(altura1), 10000 - i)))
    file.write("\n")

for i in range(3000, 6000, 1):
    file.write(str(10000 - i))
    file.write(",")
    file.write(str(eval(np.array(coefLat2), np.array(altura2), 10000 - i)))
    file.write(",")
    file.write(str(eval(np.array(coefLong2), np.array(altura2), 10000 - i)))
    file.write("\n")

for i in range(6000, 9000, 1):
    file.write(str(10000 - i))
    file.write(",")
    file.write(str(eval(np.array(coefLat3), np.array(altura3), 10000 - i)))
    file.write(",")
    file.write(str(eval(np.array(coefLong3), np.array(altura3), 10000 - i)))
    file.write("\n")

for i in range(9000, 10001, 1):
    file.write(str(10000 - i))
    file.write(",")
    file.write(str(eval(np.array(coefLat4), np.array(altura4), 10000 - i)))
    file.write(",")
    file.write(str(eval(np.array(coefLong4), np.array(altura4), 10000 - i)))
    file.write("\n")
