import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline #for the ipython notebook

# Define the logistic function

def logistic(r, x):
    return(r*x*(1-x))

# Now feed the function our data.

n = 100000
r = np.linspace(2.5, 4.0, n)
iterations = 100
last = 100

## initialize the system

x = 1e-5*np.ones(n)


print(r)
print(x)

# first we initialize the lyapunov vector
lyapunov = np.zeros(n)

# now we simulate the system and plot the diagram

#plt.subplot(211)
for i in range(iterations):
    x = logistic(r,x)

## we compute the partial sum of the lyapunov exponent

lyapunov += np.log(abs(r-2*r*x))

#we display the bifurcation diagram
if i >= (iterations - last):
    plt.plot(r,x, ',k', alpha=0.02)
plt.xlim(2.5,4)
plt.title("Bifurcation Diagram")
plt.show()

# We display the Lyapunov exponent
plt.subplot(212)
plt.plot(r[lyapunov < 0], lyapunov[lyapunov< 0]/iterations, ',k', alpha=0.01)
plt.plot(r[lyapunov >= 0], lyapunov[lyapunov>= 0]/iterations, ',k',
alpha=0.25)
plt.xlim(2.5,4)
plt.ylim(-2,1)
plt.title("Lyapunov Exponent")
