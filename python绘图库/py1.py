import matplotlib.pyplot as plt
import numpy as np
data = np.arange(0, 1.1,0.01)
print(data)
plt.title('lines')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((0,1))
plt.ylim((0,1))
plt.xticks([0,0.2,0.4,0.6,0.8,1])
plt.yticks([0,0.2,0.4,0.6,0.8,1])
plt.plot(data. data**2) #添加y = x^2曲线
plt.plot(data. data**4) #添加y = x^4曲线
plt.legend(['y=x^2','y=x^4'])
plt.savefig('y=x^2.png')
plt.show()
