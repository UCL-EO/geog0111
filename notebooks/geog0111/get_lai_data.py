from geog0111.modis_annual import modis_annual
import numpy as np


def get_lai_data(year,tile,fips):
    '''
    Get the annual LAI dataset for fips, tile and year
    and return lai,std,doy
    '''
    # load some data
    sds     = ['Lai_500m','LaiStdDev_500m']
    product = 'MCD15A3H'

    warp_args = {
      'dstNodata'     : 255,
      'format'        : 'MEM',
      'cropToCutline' : True,
      'cutlineWhere'  : f"FIPS='{fips}'",
      'cutlineDSName' : 'data/TM_WORLD_BORDERS-0.3.shp'
    }
    
    mfiles = modis_annual(year,tile,product,\
                          step=4,sds=sds,warp_args=warp_args)
    # scale it
    lai = mfiles['Lai_500m'] * 0.1
    std = mfiles['LaiStdDev_500m'] * 0.1
    # doy from filenames
    doy = np.array([int(i.split('-')[1]) for i in mfiles['bandnames']])
    return lai,std,doy
