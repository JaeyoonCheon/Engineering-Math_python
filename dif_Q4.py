import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt

# function that returns dy/dt
def model(z, t):
    k1 = 0.015;
    k2 = 0.004;
    dadt = -k1 * z[0];
    dbdt = k1 * z[0] - k2 * z[1];
    dvdt = k2 * z[1];
    dzdt = [dadt, dbdt, dvdt];
    return dzdt;

# initial condition
z0 = [1.2, 0, 0];

# time points
t = np.linspace(0, 500, 100);

# solve ODE
z = odeint(model, z0, t);

D_MAX = np.max(z[:,1]);
print(D_MAX);
# plot results
plt.figure('Result');
plt.plot(t,z[:,0], 'r-', label='A');
plt.plot(t,z[:,1], 'b-', label='D');
plt.plot(t,z[:,2], 'g-', label='U');
plt.xlabel('time');
plt.ylabel('value');
plt.legend();
plt.grid();
plt.show();