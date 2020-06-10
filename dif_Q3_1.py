import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt

# function that returns dy/dt
def model(z, t, Q, s, w):
    theta, epsilon = z;
    dzdt = [epsilon, -(1/Q)*epsilon + np.sin(theta) + s*np.cos(w*t)];
    return dzdt;
# z array definition. z[0], z[1] to x = epsilon, y = theta
# initial condition
z0 = [0, 0];

# time points
t = np.linspace(0, 300, 101);

# solve ODE
z = odeint(model, z0, t, args=(2.0, 1.8, 0.5));

# plot results
plt.figure('fig_1');

a = plt.subplot(311);
b = plt.subplot(312);
c = plt.subplot(313);

a.plot(t,z[:,1], 'r-', label='theta');
a.plot(t, 'b-', label='t');

b.plot(t,z[:,0], 'r-', label='epsilon');
b.plot(t, 'b-', label='t');

c.plot(t,z[:,1], 'r-', label='epsilon');
c.plot(t, 'b:', label='t');

plt.xlabel('time');
plt.ylabel('value');

a.legend();
b.legend();
c.legend();

plt.show();