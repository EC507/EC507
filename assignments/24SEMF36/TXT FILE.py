a = []
for i in range (10):
    b = []
    for j in range (10):
        b.append(j)
    a.append(b)
print (a)
import numpy as np
gdp = np.array([2.9,3.1,3.4])
print(gdp)
mean = np.mean(gdp)
print(f"mean: {mean}")

