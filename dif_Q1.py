import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt

def model(y, t, k):
    dydt = -y + k * np.exp(-t);
    return dydt;

y0 = 1;

t = np.linspace(0, 10, 101);

k = 0.1
y1 = odeint(model, y0, t, args = (k,));

k = 0.25
y2 = odeint(model, y0, t, args = (k,));

k = 0.4
y3 = odeint(model, y0, t, args = (k,));

plt.figure("Result");
plt.plot(t, y1, 'r-', label = 'k = 0.1');
plt.plot(t, y2, 'g--', label = 'k = 0.25');
plt.plot(t, y3, 'b:', label = 'k = 0.4');
plt.xlabel('time');
plt.ylabel("y(t)");
plt.legend();
plt.show();