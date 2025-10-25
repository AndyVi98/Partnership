"""Functions used in Exercise 8 of Geol 197 GDAM"""

# Import any modules needed in your functions here
import math
import numpy as np

# Define your new functions below
def mean(x):
    # This is how a simple mean function is defined
    return sum(x) / len(x)

# Define the requested gaussian() function
def gaussian(x, mu, sigma):
    """
    This calculates the value of the Normal (Gaussian) distribution function.
    
    variables:
    x (float or array): The point at which to evaluate the function.
    mu (float): The mean of the distribution.
    sigma (float): The standard deviation of the distribution.
    """
    # The mathematical formula for the Gaussian distribution: in reference to the formula given previously in notebook
    # f(x) = (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sigma)^2)

    x = np.array(x, dtype=float)
    mu = np.array(mu, dtype=float)
    sigma = np.array(sigma, dtype=float)
    
    coeff = 1 / (sigma * np.sqrt(2 * np.pi))
    exponent = -0.5 * ((x - mu) / sigma)**2
    
    return coeff * np.exp(exponent)

#exercise 9
#defining linregress function
def linregress (x, y):
    delta = (len(x) * (x**2).sum()) - (x.sum())**2
    A = (((x**2).sum() * y.sum()) - (x.sum() * (x*y).sum())) / delta #y-intercept
    B = ((len(x) * (x*y).sum()) - (x.sum() * y.sum())) / delta #slope
    return A,B

#defining pearson function
def pearson (x, y):
    topsum = 0
    bottomsumx = 0
    bottomsumy = 0
    
    for i in range(len(x)):
        topsum = topsum + (x[i] - x.mean()) * (y[i] - y.mean())
        bottomsumx = bottomsumx + (x[i] - x.mean())**2
        bottomsumy = bottomsumy + (y[i] - y.mean())**2
        
        r = topsum / np.sqrt(bottomsumx * bottomsumy)

    return r
    
#defining chi_squared function


def chi_squared (obs, exp, std):
    f1 = 0
    
    for i in range(len(obs)):
        f1 += ((obs[i] - exp[i])**2 / (std[i])**2)
        cs = (1/len(obs)) * f1
    
    return cs
    











    
