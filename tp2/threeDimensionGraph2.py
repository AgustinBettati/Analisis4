import csv

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
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

fig = plt.figure()
ax = fig.gca(projection='3d')

X, Y = np.meshgrid(X, Y)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0,10000)
ax.zaxis.set_major_formatter(FormatStrFormatter('%.f'))

ax.set_xlabel("Longitud")
ax.set_ylabel("Latitud")
ax.set_zlabel("Altura")

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.4, aspect=5)

plt.show()
