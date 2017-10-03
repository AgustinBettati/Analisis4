import csv

file = open("resource/geo_pos.csv", 'r')  # read only

reader = csv.reader(file)

next(reader)  # reader es un iterable de las rows del csv

for row in reader:
    print("Altura: " + row[0] + " , Latitud: " + row[1] + " , Longitud: " + row[2])
