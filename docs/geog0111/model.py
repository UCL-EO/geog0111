from scipy.special import expit
import scipy
import scipy.ndimage.filters
import numpy as np


__author__    = "P. Lewis"
__email__     = "p.lewis@ucl.ac.uk"
__date__      = "28 Aug 2020"
__copyright__ = "Copyright 2020 P. Lewis"
__license__   = "GPLv3"


'''
UCL snowmelt model for GEOG0111

'''


def model(T0,f,T,p,xp=1.0):
    '''
    snow melt model
    
    parameters:
        T0 - Temperature threshold (C): float or shape (Np)
             Typical range: 0.0 to 20.0
        f  - NRF filter decay rate    : float or shape (Np)
             Trypical range: 0.05 to 0.2
    Drivers:
        T  - Temperature (C)         : shape (Nd,)
        p  - snow cover (proportion) : shape (Nd,)
        
    Option:
        xp - float. logistic decay rate in Temperature function 
             typical range 1.0-4.0
    
    Output:
    
        Normalised river flow resulting from snowmelt. 
        Normalised to sum to 1.0 over all days
    '''
    # force T0 and f into 1D -> arrays
    f = np.array(f).ravel()[np.newaxis,:]
    T0 = np.array(T0).ravel()[np.newaxis,:]
    # treat T and p into 1D -> 2D arrays
    T = T.ravel()[:,np.newaxis]
    p = p.ravel()[:,np.newaxis]
    
    # logistic for temperature threshold effect
    y = p * expit(xp*(T-T0))
    
    # centred filter time 
    nrf_x = (np.arange(p.shape[0]) - p.shape[0]/2)
    # 1-sided NRF filter
    nrf = np.exp(-f*nrf_x[:,np.newaxis])    
    nrf[nrf_x<0,:] = 0
    
    # modelled flow : loop is inefficent by 
    # necessary if using convolution routine
    Q_nrf = np.array([scipy.ndimage.filters.convolve1d(y[:,i], nrf[:,i]) \
                       for i in range(y.shape[1])]).T
    return Q_nrf/Q_nrf.sum(axis=0)
