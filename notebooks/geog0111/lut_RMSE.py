#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

'''
In a file `lut_RMSE.py` do the following:

        import numpy as np
        # define the min and max and step for the grid we want
        p0min,p0max,p0step = 0.0,0.5,0.0025
        p1min,p1max,p1step = 0.0,0.001,0.000005

        gridp0,gridp1 = np.mgrid[p0min:p0max+p0step:p0step,\
                                 p1min:p1max+p1step:p1step]

* Write a function `gen_lut` to return a 2D parameter (Look up table -- LUT) grid using `np.mgrid` as above as `param = [gridp0,gridp1]`

        # simple model 
        def model(driver,param):
            2-parameter quadratic model with noise
            return param[0] + param[1] * driver * driver
          
* Write a function `model` to describe the model we will be using from the code above
            
        # code to use
        # time driver every 4 days for measurement    
        tmdriver = np.arange(0,365,4,dtype=np.int)
        # generate a pseudo-measurement
        p0 = np.array([5.0,0.0005])
        measure = model(tmdriver,p0) + 5*(np.random.random(tmdriver.shape)-0.5)
        # just make up some weights for this exercise
        measure_weight = (2 + np.random.random(tmdriver.shape))/4
        
* Write a function `gen_meas` to generate a pseudo-measurement based on the model and some noise. It should print the value of the parameters used in the model, and return `tmdriver, measure, measure_weight` corresponding to:

        * tmdriver:       array of (Nm,) floats of the day of year on which to do modelling
        * measure:        array of (Nm,) floats of measurements over sampled days of the year
        * measure_weight: array of (Nm,) floats of the weights associated with the measurements

* Write a function `lut_RMSE` that takes as inputs:

        * `param`:          list of `[p0,p1]` with `p0` and `p1` being arrays of shape `(Np0,Np1)` representing a the LUT grid over parameter space
        * `tmdriver`:       array of (Nm,) integers: the days on which the measurements occur 
        * `measure:`        array of (Nm,) floats of measurements over sampled days of the year
        * `measure_weight`: array of (Nm,) floats of the weights associated with the measurements
    
 That runs the model `model(tmdriver,param)`, calculates the weighted RMSE between the measurements and the modelled values for each parameter pair, and returns a grid of shape `(Np0,Np1)` values of RMSE associated with each param
 
 
 * Write a function `runner()` that 
   * gets a LUT `param` from `gen_lut`
   * gets a pseudo-measurement from `gen_meas`
   * gets a 2-D array of RMSE corresponding to the parameter grid
   * calculated and prints the value of the parameters corresponding to the minimum RMSE,
   * returns the RMSE array, the LUT, and the measurements
 
* Run `runner()` in a notebook
* Plot the RMSE values returned from this as an image
* Verify that you have identified the minimum RMSE
* Set different parameters in `gen_meas` to generate a different pseudo-measurement and repeat the process.
'''


def gen_lut():
    '''return 2D parameter LUT'''
    # define the min and max and step for the grid we want
    p0min,p0max,p0step = 0.0,10.0,0.05
    p1min,p1max,p1step = 0.0,0.001,0.000005
    gridp0,gridp1 = np.mgrid[p0min:p0max+p0step:p0step,\
                             p1min:p1max+p1step:p1step]
    return gridp0,gridp1

# simple model 
def model(driver,param):
    '''2-parameter quadratic model with noise'''
    return param[0] + param[1] * driver * driver

def gen_meas(p0=[0.4,0.0002]):
    '''
    generate a pseudo-measurement based on the model and some noise. 
    
    Optional:
    
    p0: allow different parameters to be used by keyword
    
    Outputs:
    
    tmdriver:       array of (Nm,) floats of the day of year on which to do modelling
    measure:        array of (Nm,) floats of measurements over sampled days of the year
    measure_weight: array of (Nm,) floats of the weights associated with the measurements
    '''
    print(f"original parameters: {p0}")
    # code to use
    # time driver every 4 days for measurement    
    tmdriver = np.arange(0,365,4,dtype=np.int)
    # generate a pseudo-measurement
    p0 = np.array(p0)
    measure = model(tmdriver,p0) + 5*(np.random.random(tmdriver.shape)-0.5)
    # just make up some weights for this exercise
    measure_weight = 1+ (2 + np.random.random(tmdriver.shape))/4
    return tmdriver,measure,measure_weight

def lut_RMSE(param,tmdriver,measure,measure_weight):
    '''
    
    Runs the model model(tdriver,param) and calculates the 
    weighted RMSE between the measurements and the modelled values 
    for each parameter pair
 
    Inputs:
    
    param:          list of [p0,p1] with p0 and p1 being arrays of shape
                    (Np0,Np1) representing a the LUT grid over parameter space
    tmdriver:       array of (Nm,) integers: the days on which the measurements occur 
    measure:        array of (Nm,) floats of measurements over sampled days of the year
    measure_weight: array of (Nm,) floats of the weights associated with the measurements
 
    Outputs:
    
    grid of shape `(Np0,Np1)` values of RMSE associated with each parameter pair.
    
    Comments: should put in some tests on the various array shapes here
    '''
    p0,p1 = param
    # flatten these
    p0_ = np.ravel(p0)
    p1_ = np.ravel(p1)
    
    # reconcile parameters to measurements assuming measurements are 1D
    p0_ext       = p0_[np.newaxis,:]
    p1_ext       = p1_[np.newaxis,:]
    tmdriver_ext = tmdriver[:,np.newaxis]

    # run the model
    tmoutput  = model(tmdriver_ext,[p0_ext,p1_ext])
    
    # extend measurements and weights
    measure_ext        = measure[:,np.newaxis]
    measure_weight_ext = measure_weight[:,np.newaxis]
    
    # error term
    error_ext = (tmoutput - measure_ext)*measure_weight_ext
    error_ext = error_ext*error_ext

    return np.sqrt(np.mean(error_ext,axis=0))

'''
* Write a function `runner()` that 
   * generates tdriver, the array of (365,) floats of the day of year on which to do modelling
   * gets a LUT `param` from `gen_lut`
   * gets a pseudo-measurement from `gen_meas`
   * gets a 2-D array of RMSE corresponding to the parameter grid
   * calculated and prints the value of the parameters corresponding to the minimum RMSE,
   * returns the RMSE array, the LUT, and the measurements
 '''

def runner():
    '''
    generates tmdriver, the array of (92,) floats for every 4 day of year on which to do modelling
    gets a LUT param from gen_lut
    gets a pseudo-measurement from gen_meas
    gets a 2-D array of RMSE corresponding to the parameter grid
    calculated and prints the value of the parameters corresponding to the minimum RMSE,
    returns the RMSE array, the LUT, and the measurements
    '''
    # generates tdriver, the array of (365,) 
    # floats of the day of year on which to do modelling
    tdriver = np.arange(0,365,1,dtype=np.int)
    # gets a LUT `param` from `gen_lut`
    param = gen_lut()
    # gets a pseudo-measurement from `gen_meas`
    tmdriver,measure,measure_weight = gen_meas()
    # gets a 2-D array of RMSE corresponding to the parameter grid
    RMSE = lut_RMSE(param,tmdriver,measure,measure_weight)
    # calculated and prints the value of the parameters corresponding to the minimum RMSE,
    min_rmse = RMSE.min()
    print(f'min rmse\n{min_rmse}')

    # use argmin to find min, but need to flatten/reshape arrays first
    p0,p1 = param
    p0_ = np.ravel(p0)
    p1_ = np.ravel(p1)
    # min over time axis
    imin = np.argmin(RMSE,axis=0)

    print(f'index: {imin}: {p0_[imin]},{p1_[imin]}')
    # back to 2D
    ip0min,ip1min = np.unravel_index(imin,p0.shape)
    p0min = p0[ip0min,ip1min]
    p1min = p1[ip0min,ip1min]

    p = np.array([p0min,p1min])
    print(f'parameters: {p[0]} {p[1]}')

    return RMSE,param,(measure,measure_weight,tmdriver)

def main():
  RMSE,param,m  = runner()

if __name__ == "__main__":
    main()    
