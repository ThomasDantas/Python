import pandas as pd
from matplotlib import pyplot as plt

temp = pd.read_csv('temp.csv')

plt.plot(temp.Year, temp.Glob)

plt.title("NASA")
plt.ylabel('Temperatura')
plt.xlabel('Anos')
plt.legend(["Temperatura passar dos anos"])

plt.show()
