import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt

# function that returns dy/dt
def model(z, t):
    dxdt = 3.0 * np.exp(-t);
    dydt = -z[1] + 3;
    dzdt = [dxdt, dydt];
    return dzdt;
# z 배열 선언 z[0], z[1]에 x, y
# initial condition
z0 = [0, 0];

# time points
t = np.linspace(0, 3, 31);

# solve ODE
z = odeint(model, z0, t);

# plot results
plt.figure('Result');
plt.plot(t,z[:,0], 'r-', label=r'$\frac{dx}{dt}=3exp(-t)$');
plt.plot(t,z[:,1], 'b-.', label=r'$\frac{dy}{dt}=-y+3$');
plt.xlabel('time');
plt.ylabel('value');
plt.legend();
plt.show();