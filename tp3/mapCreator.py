import csv
from tp3.newtonCoolingLaw import rk4

file = open("rungeKutta/t0.csv", 'r')  # read only

reader = csv.reader(file)

t0values = []

for row in reader:
    aux = []
    for i in range(0, 22):
        aux.append(int(row[i]))
    t0values.append(aux)

prevTemp = t0values


def ambientTemp(i, j, prevTemp):
    sum = 0.0
    for x in range(i - 1, i + 2):
        if x == i:
            sum += prevTemp[x][j - 1]
            sum += prevTemp[x][j + 1]
        else:
            for y in range(j - 1, j + 2):
                sum += prevTemp[x][y]

    return sum / 8.0


def createCsv(temps, time):
    file = open("rungeKutta/t" + str(time) + ".csv", "w")
    for i in range(0, 22):
        for j in range(0, 21):
            file.write("{0:.2f}".format(temps[i][j]) + ", ")
        file.write("{0:.2f}".format(temps[i][21]) + "\n")


for time in range(1, 11):
    newTemp = []

    wall = []
    for i in range(0, 22):
        wall.append(15)

    newTemp.append(wall)
    for i in range(1, 21):
        aux = [15]
        for j in range(1, 21):
            ambTemp = ambientTemp(i, j, prevTemp)
            temp = rk4(0, prevTemp[i][j], ambTemp, 10, 1)
            aux.append(temp)
        aux.append(15)
        newTemp.append(aux)

    newTemp.append(wall)
    createCsv(newTemp, time)
    prevTemp = newTemp