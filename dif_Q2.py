import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt

def model(y, t):
    if t < 5.0:
        u = 0;
    else:
        u = 2;
            
    dydt = (-y + u) / 5.0;
    
    return dydt;

y0 = 2;

t = np.linspace(0, 40, 101);

y = odeint(model, y0, t);

plt.figure("Result");
plt.plot(t, y);
plt.xlabel('time');
plt.ylabel("y(t)");
plt.show();