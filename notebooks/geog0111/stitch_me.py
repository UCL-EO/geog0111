def stitch_me(year,doy,sds='Lai_500m',\
              tile=['h17v03','h18v03'],\
              product='MCD15A3H'):
    '''
    function called stitch_me with arguments:
    
    year
    doy

    keywords/defaults:

        sds      : 'Lai_500m'
        tile     : ['h17v03','h18v03']
        product  : 'MCD15A3H'

    generates a stitched VRT file with the appropriate data,

    returns VRT filename for this dataset.
    '''
    # set up kwargs for MODIS
    kwargs = {
        'tile'      :    tile,
        'product'   :    product,
        'sds'       :    sds,
    }
    # set up MODIS object
    modis = Modis(**kwargs)
    # get filenames and SDS for this year/doy
    files,sds = modis.get_files(year,doy)

    # Make sure to use the year and doy in the VRT filename.
    ofile = f"work/stitch_{year}_{doy:03d}.vrt"

    # build a VRT     
    stitch_vrt = gdal.BuildVRT(ofile, sds[0])
    return ofile

