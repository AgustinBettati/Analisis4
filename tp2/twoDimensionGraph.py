import matplotlib.pyplot as plt
import csv

file = open("resource/interpolation.csv", 'r')

reader = csv.reader(file)

next(reader)

for row in reader:
    plt.plot(row[0], row[1], 'bo')

plt.xlabel('Altura')
plt.ylabel('Latitud')
plt.title('Latitud en funcion de la altura')
plt.axis([10100, -100, -91,-71])
plt.show()

