import matplotlib.pyplot as plt
import numpy as np 

x= np.arange(10)
y = 3*x + 1
z = -4*x -10
plt.plot(x,y,"r-.",label="Red line")
plt.plot(x,z,"b-",label="Blue line")
plt.legend()
plt.show()
