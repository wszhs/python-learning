from scipy.optimize import fmin


def f(x):
    return x**2-4*x + 8


print (fmin(f, 0))
