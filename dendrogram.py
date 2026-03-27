import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# cargar datos
data = pd.read_csv("iris.csv", sep=";")

# seleccionar variables numéricas
X = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]

# clustering
linked = linkage(X, method='ward')

# dibujar dendrograma
plt.figure(figsize=(10, 6))
dendrogram(linked)

plt.title("Dendrograma Iris Dataset")
plt.xlabel("Observaciones")
plt.ylabel("Distancia")

plt.tight_layout()
plt.savefig("dendrogram.png", dpi=300, bbox_inches='tight')

plt.show()
