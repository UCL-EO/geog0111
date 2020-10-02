# Formative Assessment: LAI

*Although we provide access to answers for this exercise, we want you to submit the codes you generate via Moodle, so that we can provide feedback. You should avoid looking at the answers before you submit your work. This submitted work does not count towards your course assessment, it is purely to allow us to provide some rapid feedback to you on how you are doing. You will need to put together a few elements from the notes so far to do all parts of this practical, but you should all be capable of doing it well. Pay attention to writing tidy code, with useful, clear comments and document strings.*



#### Exercise 1

Write a Python script to generate a combined LAI and land cover dataset, for a given year, tile set, and country

* In a file `work/lc_lai.py`, write a function called `lc_lai` that has has the following arguments:

        * tile     : list of MODIS tile names e.g `['h17v03','h18v03','h17v04','h18v04']`
        * year     : integer, e.g. `2018`
        * fips     : a FIPS country code string e.g. `LU`

  the following keyword options:
  
        * sigma=5  : std dev for Gaussian smoothing filter (default 5)

  and returns a dictionary with the following keys:

        'Lai_500m'   : regularised (interpolated) LAI: numpy float array of (Ndays,Nx,Ny) 
        'mask'       : a mask True for valid pixels: numpy bool array of (Nx,Ny)
        'LC_Type3'   : Land cover: numpy byte array of (Nx,Ny) 
        'doy'        : array of integers of the day of year the lai


* In the same file, write a function `write_dataset` that takes as argument:

         dataset     : the LAI, mask and LC dataset returned by  lc_lai
         ofile       : str or Path object for output file
         
   the following keyword options:
  
         classy='Deciduous Broadleaf Forests' : name for LC_Type3 LC class

    and saves the doy and  mean LAI over the specified country to a CSV text file in ofile.
    
    The function should also print out the number of samples for that land cover type (Hint: sum the combined valid/land cover mask), and not proceed further if there are no samples for the given LC class.

* In the same file, write a function  `main()` that runs a test of `lc_lai` and `get_dataset` for the following scenario:

        tile : `['h17v03','h18v03','h17v04','h18v04']`
        year : `2018`
        fips : 'BE' (Belgium)
    
  and them reads and prints the doy and mean LAI from the file you have saved.
  
* Run your script in a jupyter notebook, and and plot the dataset returned.

Hint, use existing codes as far as possible, and re-purpose to this task. For example, you may find it convenient to use `geog0111.modis_annual` to get teh MODIS dataset.

Rather than writing one huge function, you may find it useful to write a series of functions that you put together into the function `lc_lai`. For example, you might build a function to get the clipped LAI dataset, anothe to do the interpolation, another to get the land cover data, and another to build the mask. 

If you build the code as a series of smaller functions like this, test them as you go along. e.g. test that the function that getrs the LAI dataset works as intended before going on to the others. Check the data returned by looking at its shape, and perhaps doing some plots. You might find it useful to put all of thes tests into a notebook, so they become repeatable.

Try to put checks into your code to ensure it is operating as intended.

Hint: if you modularise your code in this way, the bare bones of the function will be as simple as something like:

        def lc_lai(tile,year,fips,sigma=5):
            lc               = get_lc(year,tile,fips)
            lai,std,doy      = get_lai(year,tile,fips)
            weight           = get_weight(lai,std)
            interpolated_lai = regularise(lai,weight,sigma)
            mask             = make_mask(interpolated_lai)
            odict = {
                'Lai_500m' : lai,
                'LC_Type3' : lc,
                'mask'     : mask,
                'doy'      : doy
            }
            return odict

You can then concentrate on writing and testing the various sub-codes `get_lc`, `get_lai` etc. We suggest that you start with defining `get_lc(year,tile,fips)` as above, and work your way through the sub-functions. You will find code to achieve most of these items in the notes.

Don't forget to make the file executable. Don't forget to import all of the packages you will use.
