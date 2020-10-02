import numpy as np

'''
a function `get_weight` that takes as argument:

lai  : MODIS LAI dataset
std  : MODIS LAI uncertainty dataset 
'''
def get_weight(lai,std):
    std[std<1] = 1
    weight = np.zeros_like(std)
    mask = (std > 0)
    weight[mask] = 1./(std[mask]**2)
    weight[lai > 10] = 0.

    return weight

