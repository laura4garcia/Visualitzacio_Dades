import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

data = pd.read_csv("wine.csv", sep=";")

# seleccionar variables
x_col = "Alcohol"
y_col = "Malic.acid"
group_col = "Wine"

plt.figure(figsize=(8,6))

# colors per grup
colors = ["red", "blue", "green"]

# recórrer cada grup
for i, wine_type in enumerate(data[group_col].unique()):
    subset = data[data[group_col] == wine_type]
    
    x = subset[x_col].values
    y = subset[y_col].values
    
    points = list(zip(x, y))
    
    # scatter
    plt.scatter(x, y, color=colors[i], label=f"Wine {wine_type}")
    
    # convex hull (mínim 3 punts)
    if len(points) >= 3:
        hull = ConvexHull(points)
        hull_points = hull.vertices
        
        for simplex in hull.simplices:
            plt.plot(x[simplex], y[simplex], colors[i])

# etiquetes
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title("Convex Hull - Wine Dataset")
plt.legend()

# guardar imatge
plt.savefig("convex_hull.png", dpi=300)

plt.show()

