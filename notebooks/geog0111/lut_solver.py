#!/usr/bin/env python
# -*- coding: utf-8 -*-
from geog0111.get_lai_data import get_lai_data
from geog0111.regularise import regularise
import numpy as np

'''
* From the code above, develop a function `solver` in a file 
  `work/lut_solver.py` that takes the following inputs:
    
    * lai, weight : datasets of shape (Nt,Nx,Ny) for observations and reliability
    * 2D parameter grids for model parameters p3 and p5 with shape (Np0,Np1)
    * function slope parameters p2 and p4 for the double sigmoid: float
    * function vertical min and extent parameters p0 and p1 of shape (Nx,Ny)
    
  and solves for the optimal weighted fit between LAI and modelled LAI using the parameters pi
  It should return:
  
    *  p : list of 6 parameter arrays solved for, so 6 of shape (Nx,Ny)
    * RMSE : the RMSE 
    
* The code could be made more efficient by not processing invalid pixels. 
  Develop and use a mask of valid pixels to implement this.
'''
def dbl_sigmoid_function(p, t):
    """The double sigmoid function defined over t (where t is an array).
    Takes a vector of 6 parameters"""

    sigma1 = 1./(1+np.exp(p[2]*(t-p[3])))
    sigma2 = 1./(1+np.exp(-p[4]*(t-p[5])))
    y = p[0] - p[1]*(sigma1 + sigma2 - 1)
    return y

def lut_solver(doy,lai,weight,p0,p1,p2,sp3,p4,sp5):
    ''' Solve for optimum model fit with LUT
    
    Inputs:
    - doy : days for which there are samples of shape (Nt)
    - lai, weight : datasets of shape (Nt,Nx,Ny) for observations and reliability
    - 2D parameter grids for model parameters p3 and p5 with shape (Np0,Np1)
    - function slope parameters p2 and p4 for the double sigmoid: float
    - function vertical min and extent parameters p0 and p1 of shape (Nx,Ny)
  
    Outputs:
    -  p : list of 6 parameter arrays solved for, so 6 of shape (Nx,Ny)
    - RMSE : the RMSE 
    '''
    # sort ravel and shapes
    sp3_ = sp3.ravel()
    sp5_ = sp5.ravel()
    param0_ = p0.ravel()
    param1_ = p1.ravel()

    newshape = (*lai.shape[:1],np.prod(np.array(lai.shape[1:])))
    # reshape 
    lai_    = lai.reshape(newshape)
    weight_ = weight.reshape(newshape)
    
    param3_ext = sp3_[np.newaxis,np.newaxis,:]
    param5_ext = sp5_[np.newaxis,np.newaxis,:]
    lai_ext    = lai_[:,:,np.newaxis]
    weight_ext = weight_[:,:,np.newaxis]
    t_ext      = doy[:,np.newaxis,np.newaxis]
    param0_ext = param0_[np.newaxis,:,np.newaxis]
    param1_ext = param1_[np.newaxis,:,np.newaxis]
    param2_ext = p2
    param4_ext = p4
    t = doy[:,np.newaxis]
    p = [param0_ext,param1_ext,param2_ext,\
         param3_ext,param4_ext,param5_ext]

    # run the model
    y = dbl_sigmoid_function(p,t_ext)
    
    # error
    error_ext = (y - lai_ext)*weight_ext
    error_ext = error_ext*error_ext
    rmse = np.sqrt(np.mean(error_ext,axis=0))
    
    imin = np.argmin(rmse,axis=1)
    p3min,p5min = sp3_[imin],sp5_[imin]
    
    # other parameters for outout
    p2min = np.zeros_like(p3min) + p2
    p4min = np.zeros_like(p3min) + p4
    p0min = p0
    p1min = p1
    
    imshape = lai[0].shape
    p = [p0min.reshape(imshape), p1min.reshape(imshape),\
         p2min.reshape(imshape), p3min.reshape(imshape),\
         p4min.reshape(imshape), p5min.reshape(imshape)]
    
    return rmse.reshape,p

def get_lai():
    # load some data
    tile    = ['h17v03','h18v03','h17v04','h18v04']
    year    = 2019
    fips    = "LU"
    lai,std,doy =  get_lai_data(year,tile,fips)
    std[std<1] = 1
    weight = np.zeros_like(std)
    mask = (std > 0)
    weight[mask] = 1./(std[mask]**2)
    weight[lai > 10] = 0.
    return lai,weight,doy

def get_p0p1(lai,weight,sigma=5.0):
    '''get the p0 p1 estimates'''
    interpolated_lai = regularise(lai,weight,sigma)
    param0 = np.min(interpolated_lai,axis=0)
    param1 = np.max(interpolated_lai,axis=0) - param0
    return param0,param1
    
def main():
    lai,weight,doy = get_lai()
    sp0min,sp0max,sp0step = 100,250,10
    sp1min,sp1max,sp1step = 100,300,10
    sp0,sp1 = np.mgrid[sp0min:sp0max+sp0step:sp0step,\
                     sp1min:sp1max+sp1step:sp1step]
    width,centre = sp0,sp1
    sp3 = centre - width/2.
    sp5 = centre + width/2.
    p2 = p4 = 0.07
    p0,p1 = get_p0p1(lai,weight)
    
    rmse,p = lut_solver(doy,lai,weight,p0,p1,p2,sp3,p4,sp5)
    return rmse,p

if __name__ == "__main__":
    main()    
