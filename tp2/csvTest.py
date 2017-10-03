import csv

file = open("resource/geo_pos.csv", 'r')  # read only

reader = csv.reader(file)

next(reader)  # reader es un iterable de las rows del csv

altura = []
latitud = []
longitud =[]

for row in reader:
    altura.append(row[0])
    latitud.append(row[1])
    longitud.append(row[2])

