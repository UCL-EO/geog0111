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
    snow melt model by P. Lewis (C) UCL 2010-2022

    parameters:
        T0 - Temperature threshold (C): float or shape (Np)
             Typical range: 0.0 to 20.0 C
        f  - NRF filter decay rate (days) : float or shape (Np)
             Trypical range: 5 to 20 days
    Drivers:
        T  - Temperature (C)         : shape (Nd,)
        p  - snow cover (proportion) : shape (Nd,)
        
    Option:
        xp - float. logistic decay rate in Temperature function 
             typical range 0.25 to 1.0
    
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
    y = p * expit((T-T0)/xp)
    
    # centred filter time 
    nrf_x = (np.arange(p.shape[0]) - p.shape[0]/2)
    # 1-sided NRF filter scaled by parameter f
    nrf = np.exp(-nrf_x[:,np.newaxis]/f)    
    nrf[nrf_x<0,:] = 0
    
    # modelled flow : loop is inefficent by 
    # necessary if using convolution routine
    Q_nrf = np.array([scipy.ndimage.filters.convolve1d(y[:,i], nrf[:,i]) \
                       for i in range(y.shape[1])]).T

    Q_nrf -= Q_nrf.min(axis=0)[np.newaxis,:]
    return Q_nrf/Q_nrf.sum(axis=0)


