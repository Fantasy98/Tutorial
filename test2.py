import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(10)

y = -3 * x +10
z = y*2 

plt.plot(x,y,"r-.",label="red")
plt.plot(x,z,"b-",label="blue")
plt.show()
