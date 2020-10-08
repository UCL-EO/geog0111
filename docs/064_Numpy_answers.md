# Formative Assessment: `numpy` : Answers to exercises

#### Exercise 1

Recall from [previous sections](030_NASA_MODIS_Earthdata.md#MOTA) how to retrieve a MODIS LAI dataset for a particular date. Recall also values of greater than 100 are invalid, and that a scaling of 0.1 should be applied to the LAI.

* Load a MODIS LAI dataset SDS `Lai_500m` for tile `h17v03` day of year 41, 2019. 
* Call the 2D array `data` and confirm that it has a shape (2400, 2400)
* build a mask called `mask` of invalid pixels 
* print the percentage of invalid pixels to 2 decimal places (hint: sum with `sum`)
* scale the data array as appropriate to obtain LAI
* set invalid data values to 'not a number' `np.nan`
* display the resulting image


```python
# ANSWER
import numpy as np
from geog0111.modis import Modis

# Load a MODIS LAI dataset SDS 
# `Lai_500m` for tile `h17v03` day of year 41, 2019
kwargs = {
    'tile'      :    ['h17v03'],
    'product'   :    'MCD15A3H',
    'sds'       :    'Lai_500m',
}
modis = Modis(**kwargs)
# specify day of year (DOY) and year
data_MCD15A3H = modis.get_data(2019,doy=1+4*10)

# Call the 2D array `data` and 
# confirm that it has a shape (2400, 2400)
data = data_MCD15A3H['Lai_500m']
assert data.shape == (2400,2400)

# build a mask called `mask` of invalid pixels
mask = (data > 100)

# count how many invalid pixels there are (`sum`)
perc = 100 * mask.sum()/(mask.shape[0] * mask.shape[1])
print(f'{perc : .2f}% invalid pixels')

# scale the data array as appropriate to obtain LAI
data = data * 0.1

# set invalid data values to 'not a number' np.nan
data[mask] = np.nan
```

     77.22% invalid pixels



```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1,1,figsize=(16,8))
# plot image data: use vmin and vmax to set limits
im = axs.imshow(data,vmax=10,interpolation=None)
fig.colorbar(im, ax=axs)
```




    <matplotlib.colorbar.Colorbar at 0x7f1cca4e4850>




    
![png](064_Numpy_answers_files/064_Numpy_answers_3_1.png)
    

