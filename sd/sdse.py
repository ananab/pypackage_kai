import numpy as np
def standard_deviation(x):
    x = [i for i in x if ~np.isnan(i)]
    n = len(x)
    denumerator = sum(x)
    mean = denumerator / n
    ssq = sum((x_i-mean)**2 for x_i in x)
    stdev = (ssq/n)**0.5
    return(stdev)

standard_error = lambda x: standard_deviation(x)/len(x)**0.5

