try:
  from geog0111.get_doy import get_doy
except:
  from get_doy import get_doy
import numpy as np


def yeardays(year,step=1):
    '''return list of doy values for month'''
    full = np.arange(get_doy(year, 1, 1),get_doy(year,12,31)+1)
    if step == 1:
         return full
    # start on doy 1
    mask = np.remainder(full,step)
    select = full[mask==1]
    return select


def monthdays(year,month,step=1):
    '''return list of doy values for month'''
    assert month >= 1
    assert month <= 12

    if month < 12:
        full = np.arange(get_doy(year, month, 1),get_doy(year, month+1, 1))
    else:
        # December case
        full = np.arange(get_doy(year, month, 1),get_doy(year, month, 31)+1)
    # mod
    if step == 1:
         return full
    # start on doy 1
    mask = np.remainder(full,step)
    select = full[mask==1]
    return select

