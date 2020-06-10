import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt

# function that returns dy/dt
def model(z, t, Q, s, w):
    dydt = z[0];
    dxdt = -(1/Q) * z[0] + np.sin(z[1]) + s * np.cos(w*t);
    dzdt = [dxdt, dydt];
    return dzdt;
# z array definition. z[0], z[1] to x = epsilon, y = theta
# initial condition
z0 = [0, 0];

# time points
t = np.linspace(0, 300, 100);

# solve ODE
z = odeint(model, z0, t, args=(2.0, 1.8, 0.5));

# plot results
plt.figure('Result');
plt.plot(t,z[:,0], 'r-', label='1');
plt.plot(t, 'b-.', label='2');
plt.xlabel('time');
plt.ylabel('value');
plt.legend();
plt.show();