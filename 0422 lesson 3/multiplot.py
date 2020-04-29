import matplotlib.pyplot as plt
import numpy as np

pltlist = plt.style.available
print(pltlist)

x = 1
y = 0
z = 2
print([x, y, z])

#linear
plt.subplot(3, 1, 1)
plt.style.use('seaborn')
x1 = np.linspace(0, 2, 400)
y1 = np.sin((1.5*np.pi*x1)**2)
plt.plot(x1, y1, 'r', label='linspace')
plt.legend(loc='best')
plt.title('Linear')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#scatter
plt.subplot(3, 1, 2)
plt.style.use('seaborn-deep')
x2 = 10*np.random.rand(200, 1)
y2 = (0.2 + 0.8*x2) * \
     np.sin(2*np.pi*x2) + \
     np.random.randn(200, 1)
plt.scatter(x2, y2, color='m')
plt.title('Scatter')

#histogram
plt.subplot(3, 1, 3)
plt.style.use('ggplot')
x3 = 10*np.random.rand(100, 1)
y3 = (0.2 + 0.8*x3) * \
     np.sin(2*np.pi*x3) \
     + np.random.randn(100, 1)
plt.hist(y3, bins=150)
plt.title('Histogram')

plt.axis('tight')
plt.tight_layout()
plt.show()
