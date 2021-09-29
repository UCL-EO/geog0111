from geog0111.im_display import im_display
import numpy as np


def data_mask(data,sds,scales,uthresh,lthresh):
    '''
    given:
    
    data     : data dictionary
    sds      : list of sds strings
    scales   : list of scale factors
    uthresh  : list of upper threshold values
    lthresh  : list of upper threshold values
    
    return the dictionary with the scaled 
    and masked datasets 
    '''
    for i,s in enumerate(sds):
        scale = scales[i]
        ds = data[s] * scale
        # mask invalid by setting to 
        if uthresh[i] !=  None:
            ds = ds.astype(np.float)
            ds[ds>=uthresh[i] * scale] = np.nan
        if lthresh[i] != None:
            ds = ds.astype(np.float)
            ds[ds<=lthresh[i] * scale] = np.nan
        # load back into data_MCD15A3H
        data[s] = ds
    return data
