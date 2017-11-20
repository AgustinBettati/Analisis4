import csv
import matplotlib.pyplot as plt


def plot(name):
    file = open(name, 'r')
    reader = csv.reader(file)
    X = []
    Y = []
    T = []
    count = -1
    for row in reader:
        count = count + 1
        for i in range(0, 22, 1):
            X.append(float(i))
            Y.append(float(count))
            T.append(float(row[i]))
    plt.title(r"$\bf{" + file.name + "}$")
    ax = plt.gca()
    ttl = ax.title
    ttl.set_position([.5, 1.03])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(X, Y, c=T, cmap='jet', vmin=0, vmax=200, marker='o')
    plt.colorbar().set_label("Temperatura")
    plt.show()


for i in range(0, 10):
    plot("analytic/t" + str(i) + ".csv")
