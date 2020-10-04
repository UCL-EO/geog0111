import numpy as np
import scipy
import scipy.ndimage.filters

# regularise
def regularise(lai,weight,sigma):
    '''
    takes as argument:
    
        lai     : MODIS LAI dataset:     shape (Nt,Nx,Ny)
        weight  : MODIS LAI weight:      shape (Nt,Nx,Ny)
        sigma   : Gaussian filter width: float
        
    returns an array the same shape as 
    lai of regularised LAI. Regularisation takes place along
    axis 0 (the time axis)
    '''
    x = np.arange(-3*sigma,3*sigma+1)
    gaussian = np.exp((-(x/sigma)**2)/2.0)

    numerator = scipy.ndimage.filters.convolve1d(lai * weight, gaussian, axis=0,mode='wrap')
    denominator = scipy.ndimage.filters.convolve1d(weight, gaussian, axis=0,mode='wrap')

    # avoid divide by 0 problems by setting zero values
    # of the denominator to not a number (NaN)
    denominator[denominator==0] = np.nan

    interpolated_lai = numerator/denominator
    # (Nt,Nx,Ny)
    return interpolated_lai


