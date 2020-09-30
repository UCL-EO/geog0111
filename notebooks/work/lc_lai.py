#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# import required package(s)
from geog0111.modis_annual import modis_annual
import pandas as pd
from geog0111.modis import Modis
import scipy
import scipy.ndimage.filters
import numpy as np
import gdal
from pathlib import Path
'''
lc_lai

Purpose:

  generate a combined LAI and land cover dataset, for a given year, tile set, and country

  Formative Assessment: LAI
  
    Author: P. Lewis
    Email:  p.lewis@ucl.ac.uk
    Date:   28 Aug 2020

    In a file work/lc_lai.py, write a function called lc_lai that has has the following arguments:

        tile : list of MODIS tile names e.g ['h17v03','h18v03','h17v04','h18v04']
        year : integer, e.g. 2018
        fips : a FIPS country code string e.g. LU

    the following keyword options:

        sigma=5 : std dev for Gaussian smoothing filter (default 5)
    
    and returns a dictionary with the following keys:

        'Lai_500m' : regularised (interpolated) LAI: numpy float array of (Ndays,Nx,Ny) 
        'mask' : a mask True for valid pixels: numpy byte array of (Nx,Ny) 
        'LC_Type3' : Land cover: numpy byte array of (Nx,Ny)

'''

def get_lai(year,tile,fips):
    '''
    Get the LAI dataset for fips, tile and year
    and return lai,doy
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
                          sds=sds,warp_args=warp_args)
    # scale it
    lai = mfiles['Lai_500m'] * 0.1
    std = mfiles['LaiStdDev_500m'] * 0.1
    # doy from filenames
    doy = np.array([int(i.split('-')[1]) for i in mfiles['bandnames']])
    return lai,std,doy


def get_lc(year,tile,fips):
    '''
    Return LC mask for year,tile,fips
    '''
    kwargs = {
        'tile'      :    tile,
        'product'   :    'MCD12Q1',
    }
    doy = 1
    # get the LC data
    modis = Modis(**kwargs)

    warp_args = {
      'dstNodata'     : 255,
      'format'        : 'MEM',
      'cropToCutline' : True,
      'cutlineWhere'  : f"FIPS='{fips}'",
      'cutlineDSName' : 'data/TM_WORLD_BORDERS-0.3.shp'
    }

    # specify day of year (DOY) and year
    lcfiles = modis.get_modis(year,doy,warp_args=warp_args)
    # get the item we want
    g = gdal.Open(lcfiles['LC_Type3'])
    # error checking
    if not g:
        print(f"cannot open LC file {lcfiles['LC_Type3']}")
        return None
    lc = g.ReadAsArray()
    del g
    print(f"class codes: {np.unique(lc)}")
    return lc

# get_weight(lai)
def get_weight(lai,std):
    std[std<1] = 1
    weight = np.zeros_like(std)
    mask = (std > 0)
    weight[mask] = 1./(std[mask]**2)
    weight[lai > 10] = 0.

    return weight

# regularise
def regularise(lai,weight,sigma):
    ''' return regulaised dataset along axis 0'''
    x = np.arange(-3*sigma,3*sigma+1)
    gaussian = np.exp((-(x/sigma)**2)/2.0)

    numerator = scipy.ndimage.filters.convolve1d(lai * weight, gaussian, axis=0,mode='wrap')
    denominator = scipy.ndimage.filters.convolve1d(weight, gaussian, axis=0,mode='wrap')

    # avoid divide by 0 problems by setting zero values
    # of the denominator to not a number (NaN)
    denominator[denominator==0] = np.nan

    interpolated_lai = numerator/denominator
    return interpolated_lai

def make_mask(interpolated_lai):
    '''return True where there is no nan in axis 0'''
    return ~np.isnan(np.sum(interpolated_lai,axis=0))
    
# define a function lc_lai
def lc_lai(tile,year,fips,sigma=5):
    '''
    generate a combined LAI and land cover dataset, 
    for a given year, tile set, and country (defined by FIPS)
    
    Arguments:
    
    tile : list of MODIS tile names e.g ['h17v03','h18v03','h17v04','h18v04']
    year : integer, e.g. 2018
    fips : a FIPS country code string e.g. LU
    
    Options:
    
    sigma=5 : std dev for Gaussian smoothing filter (default 5)
    
    Output:
    
    a dictionary with the following keys:

        'Lai_500m' : regularised (interpolated) LAI: numpy float array of (Ndays,Nx,Ny) 
        'mask'     : a mask True for valid pixels: numpy bool array of (Nx,Ny) 
        'LC_Type3' : Land cover: numpy byte array of (Nx,Ny)

    '''
    lc               = get_lc(year,tile,fips)
    lai,std,doy      = get_lai(year,tile,fips)
    weight           = get_weight(lai,std)
    interpolated_lai = regularise(lai,weight,sigma)
    mask             = make_mask(interpolated_lai)
    odict = {
        'Lai_500m' : interpolated_lai,
        'LC_Type3' : lc,
        'mask'     : mask,
        'doy'      : doy
    }
    return odict


def get_lc_code(classy='Deciduous Broadleaf Forests'):
    '''
    Return lc_Type3 code for str classy
    '''
    # get the code for the LC class we want
    lc_Type3 = pd.read_csv('data/LC_Type3_colour.csv')
    code = int(lc_Type3['code'][lc_Type3['class'] == classy])
    return code

def write_dataset(dataset,ofile,classy='Deciduous Broadleaf Forests'):
    '''
     get dataset for given classy and save to CSV in ofile
    '''
    land_cover = dataset['LC_Type3']
    lai        = dataset['Lai_500m']
    valid_mask = dataset['mask']
    doy        = dataset['doy']
    # select pixels from combined masks
    code = get_lc_code(classy=classy)
    code_mask = (land_cover == code)
    mask = np.logical_and(code_mask,valid_mask)
    
    # 
    # The function should also print out the number 
    # of samples for that land cover type 
    # (Hint: sum the combined valid/land cover mask), 
    # and not proceed further if there are no samples 
    # for the given LC class.
    print(f'Class {classy} code {code} has {mask.sum()} samples')
    if mask.sum():
        # mean over axis 1
        mean_lai = np.mean(lai[:,mask],axis=(1))
        df = pd.DataFrame({'doy':doy,'Lai_500m':mean_lai})
        # save as csv without the index
        
    else:
        print(f"no data in Class {classy}")
        # return something appropriate
        df = pd.DataFrame({'doy':doy,'Lai_500m':[[0]]*len(doy)})
    # save to CSV
    df.to_csv(ofile,index=False)
    
# define a function main() to call when a script
def main():
    tile = ['h17v03','h18v03','h17v04','h18v04']
    year = '2018'
    fips = 'BE' 
    classy='Deciduous Broadleaf Forests'
    #classy='Grasslands'
    ofile = Path('work/mydata.{fips}.{year}.{"_".join(tile)}.{classy.replace(" ","_")}.csv')
    dataset = lc_lai(tile,year,fips,sigma=5)
    write_dataset(dataset,ofile,classy=classy)
    # read ofile
    df1=pd.read_csv(ofile)
    print(df1)
    
# calls main() if the file is run as a Python script
if __name__ == "__main__":
    main()
