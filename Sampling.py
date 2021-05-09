import numpy as np
import matplotlib.pyplot as plt

#Defining our target function
def f(x):
    return 1.3-x**3

xs = np.linspace(0, 1, 1000)
ys = f(xs)

plt.plot(xs, ys, label="Target Function")
plt.fill_between(xs, ys, 0, alpha=0.2)

#Sampling
def sample(function, xmin=0, xmax=1, ymax=1.3):
    while True:
        x = np.random.uniform(low=xmin, high=xmax)
        y = np.random.uniform(low=0, high=ymax)
        if y < function(x):
            return x
        
samps = [sample(f) for i in range(10000)]

#Plotting the results for visualisation
plt.hist(samps, density=True, alpha=0.2, label="Sample distribution")
plt.xlim(0, 1), plt.ylim(0, 1.4), plt.xlabel("x"), plt.ylabel("y"), plt.legend();
plt.show()
