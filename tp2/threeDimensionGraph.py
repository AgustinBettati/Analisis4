import matplotlib.pyplot as plt
import csv
import numpy as np

file = open("resource/interpolation.csv", 'r')

reader = csv.reader(file)

next(reader)
X = []
Y = []
Z = []

for row in reader:
    X.append(float(row[2]))
    Y.append(float(row[1]))
    Z.append(float(row[0]))

fig = plt.figure('Latitud y longitud en funcion de la altura')
ax1 = fig.add_subplot(111, projection='3d')

x = np.array(X)
y = np.array(Y)
z = np.array(Z)

ax1.scatter(x, y, z)
ax1.set_xlabel('Longitud')
ax1.set_ylabel('Latitud')
ax1.set_zlabel('Altura')

plt.show()
