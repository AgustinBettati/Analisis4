import matplotlib.pyplot as plt
import csv

file = open("resource/geo_pos.csv", 'r')

reader = csv.reader(file)

next(reader)

for row in reader:
    plt.plot(row[0], row[2], 'bo')

plt.xlabel('Altura')
plt.ylabel('Longitud')
plt.title('Longitud en funcion de la altura')
plt.axis([10100, 0, -3, 41])
plt.show()

