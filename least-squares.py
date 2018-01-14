import pandas as pd
from pandas import *
import matplotlib.pyplot as plt

data = pd.read_csv('LS.csv')
df = DataFrame(data)

XList = df['X'].tolist()
YList = df['Y'].tolist()

x = np.array(XList)
y = np.array(YList)

m, b = np.polyfit(x, y, 1)
z = np.poly1d([m, b])
print(z)

plt.plot(x, y, 'ro')
plt.plot(x, m*x + b, '-')
plt.show()

