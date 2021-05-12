import matplotlib.pyplot as plt

from numpy import pi, linspace, sin, cos

x1 = x2 = linspace(0,4*pi,100)
y1 = sin(x1)
y2 = cos(x2)


plt.figure(1)
plt.plot(x1,y2, "b-*")
plt.show()

x1 = x2 = linspace(0,10*pi,100)
y1 = sin(x1)
y2 = cos(x2)
plt.figure(2).canvas.set_window_title('Test')
plt.plot(x1,y2, "b-*")
plt.show()