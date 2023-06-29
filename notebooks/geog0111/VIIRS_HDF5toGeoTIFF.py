# -*- coding: utf-8 -*-
"""
VIIRS HDF-EOS5 Import, Georeference, and Export as GeoTIFF Tool
How to Reformat and Georeference VIIRS Surface Reflectance HDF-EOS5 Files 
Tool imports VIIRS HDF5, georeferences, and exports geoTIFFs
Authors:
Cole Krehbiel1 and Aaron Friesz1
1 Innovate!, Inc., contractor to the U.S. Geological Survey, Earth Resources 
Observation and Science (EROS) Center, Sioux Falls, South Dakota, USA. 
Work performed under USGS contract G15PD00766 for LP DAAC2.
2 LP DAAC Work performed under NASA contract NNG14HH33I.
Contact:
Phone: 866-573-3222
E-mail: LPDAAC@usgs.gov

Organization: Land Processes Distributed Active Archive Center
Date last modified: 05-05-2020
-------------------------------------------------------------------------------
OBJECTIVE:
This tutorial demonstrates how R and Python scripts can be used to open 
Visible Infrared Imaging Radiometer Suite (VIIRS) Hierarchical Data Format 
version 5 (HDF-EOS5, .h5) surface reflectance files, correctly define the 
coordinate reference system (CRS), and export each science dataset as GeoTIFF 
files that can be loaded with spatial reference into GIS and Remote Sensing 
software programs. Both the R and Python scripts will batch process all VIIRS 
HDF-EOS5 surface reflectance (VNP09) files contained in the input directory.

The Land Processes Distributed Active Archive Center (LP DAAC) distributes 
VIIRS surface reflectance products. The VIIRS surface reflectance collection 
is archived in HDF-EOS5 format. There is a known issue that prevents users 
from viewing the data in its correct spatial orientation when using common 
image processing software programs. When brought into a GIS or Remote Sensing 
software program, the VNP09 HDF-EOS5 files are displayed without a CRS. 
The scripts provided here correct this issue. 

For specific information on the VIIRS surface reflectance products, see the 
additional information section below.  VIIRS surface reflectance files can be 
downloaded from the LP DAAC Data Pool.  Results from this tutorial are output 
in the native coordinate reference system for each specific VIIRS VNP09 product 
as GeoTIFF files for each science dataset contained in the input file.
 
The output naming convention for each band is:
VNP09[specific prod].AYYYYDOY.h##v##.001_[process date]_sciencedatasetname.tif

This tutorial was specifically developed for VIIRS Surface Reflectance HDF-EOS5
files and should only be used for those data products listed below:
- VNP09A1
- VNP09GA
- VNP09H1
- VNP09CMG
-------------------------------------------------------------------------------
PREREQUISITES:
This script has been tested with the specifications listed below.
- Windows 7 and 10 64-bit OS
- Python (Version 2.7, 3.4, and 3.7.6):
- Libraries
    • osgeo with gdal and gdal_array – 1.11.1/3.0.2
    • numpy – 1.11.0/1.18.1
    • h5py, os, glob, sys, getopt, argparse, re
-------------------------------------------------------------------------------
PROCEDURES:
VIIRS_HDF5toGeoTIFF.py (URL to Python Script)
1. Download VIIRS VNP09 HDF-EOS5 data and the VIIRS_HDF5toGeoTIFF.py script 
    from the LP DAAC to a local directory
2. Open a Command Prompt window and navigate to the directory where you 
    downloaded the VIIRS_HDF5toGeoTIFF.py script or use the absolute path to 
    the VIIRS_HDF5toGeoTIFF.py file.
3. Activate python in the Command Prompt window
    a. > activate [python environment name]
4. Once python is activated, run the script with the following command in your 
    Command Prompt:
    a. > python VIIRS_HDF5toGeoTIFF.py [input directory containing VNP09 files]
        i. Example of input directory: C:/users/johndoe/VIIRS/VNP_HDF5/
-------------------------------------------------------------------------------
ADDITIONAL INFORMATION:
VIIRS Overview: 
 https://lpdaac.usgs.gov/data/get-started-data/collection-overview/missions/s-npp-nasa-viirs-overview/  
VNP09A1 - VIIRS/NPP Surface Reflectance 8-Day L3 Global 1km SIN Grid Product Page
 https://doi.org/10.5067/VIIRS/VNP09A1.001
VNP09GA - VIIRS/NPP Surface Reflectance Daily L2G Global 1km and 500m SIN Grid Product Page
 https://doi.org/10.5067/VIIRS/VNP09GA.001
VNP09H1 - VIIRS/NPP Surface Reflectance 8-Day L3 Global 500m SIN Grid Product Page
 https://doi.org/10.5067/VIIRS/VNP09H1.001
VNP09CMG - VIIRS/NPP Surface Reflectance Daily L3 Global 0.05 Deg CMG Product Page
https://doi.org/10.5067/VIIRS/VNP09CMG.001


This tool will batch process VIIRS HDF-EOS5 files if more than 1 is located in 
the input directory.
-------------------------------------------------------------------------------
RELATED RESOURCES:
Additional LP DAAC Data Prep Scripts can be found at: 
    https://lpdaac.usgs.gov/tools/data-prep-scripts/
Additional Tutorials can be found at: 
    https://lpdaac.usgs.gov/resources/e-learning/
-------------------------------------------------------------------------------
LABELS:
Georeference, GeoTIFF, HDF-EOS5, LP DAAC, Python, R, Surface Reflectance, VIIRS

"""
#------------------------------------------------------------------------------
# Load necessary packages into Python
import h5py, glob, sys, getopt, argparse, re, os
import numpy as np
# Import gdal_array to match numpy data type names to gdal data type names
from osgeo import gdal, gdal_array
#------------------------------------------------------------------------------
# Define Script and handle errors
def main(argv):
    parser = argparse.ArgumentParser()
    try:
        opts, args = getopt.getopt(argv,"hi:",["input_directory"])   
        if len(sys.argv[1:])==0:
            class MyParser(argparse.ArgumentParser):
                def error(self, message):
                    sys.stderr.write('error: %s\n' % message)
                    self.print_help()
                    sys.exit(2)
            parser=MyParser()
            # Add command line argument for input directory            
            parser.add_argument('input_directory', nargs='+')
            args=parser.parse_args()
            # below are a series of potential common errors and responses
        elif "'" in sys.argv[1] or '"' in sys.argv[1]:
            parser.error('error: Do not include quotes in input dir argument')
        elif len(sys.argv) > 2:
            parser.error('error: Only 1 Argument is allowed (input_directory)')
        elif sys.argv[1][-1] != '/' and sys.argv[1][-1] != '\\':
            parser.error('error: Please end directory location with / or \\')
    except getopt.GetoptError:
        print('error: Invalid option passed as argument')      
        print('VIIRS_HDF5toGeoTIFF.py <input_directory>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('VIIRS_HDF5toGeoTIFF.py <input_directory>')
            sys.exit()
    try:
        os.chdir(sys.argv[1])
    except FileNotFoundError:
        print('error: input_directory does not exist or cannot be found')
        sys.exit(2)
#------------------------------------------------------------------------------
    # Set input/current working directory from user defined argument
    in_dir = sys.argv[1]
    
    # Create and set output directory
    out_dir = os.path.normpath((os.path.split(in_dir)[0] + os.sep + 
        'output_py/'))+ '\\'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
                
    # Create a list of All VIIRS Surface Reflectance HDF-EOS5 files in the dir
    file_list = glob.glob(in_dir + 'VNP09**.h5')
    if len(file_list) == 0:
        print('Error: no valid VNP09 h5 files were found in this directory')
        sys.exit(2)
    # The projection information can not be obtained as a WKT of Proj4 string 
    # from the VIIRS file. Proj info is hard coded to match proj of MODIS tile.
    # projInfo[0] = Sinusoidal info, projInfo[1] = CMG (geo) info
    projInfo = 'PROJCS["unnamed",GEOGCS["Unknown datum based upon the custom spheroid", DATUM["Not specified (based on custom spheroid)", SPHEROID["Custom spheroid",6371007.181,0]],PRIMEM["Greenwich",0], UNIT["degree",0.0174532925199433]], PROJECTION["Sinusoidal"],PARAMETER["longitude_of_center",0],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["Meter",1]]',\
               'GEOGCS["Unknown datum based upon the Clarke 1866 ellipsoid", DATUM["Not specified (based on Clarke 1866 spheroid)", SPHEROID["Clarke 1866",6378206.4,294.9786982139006]], PRIMEM["Greenwich",0], UNIT["degree",0.0174532925199433]]'
    format = "GTiff"    
    #--------------------------------------------------------------------------
    # Function to get geoinformation from the StructMetadata object
    def GetGeographicInfo(input_file):
        # Get info from the StructMetadata Object
        f_Metadata = input_file['HDFEOS INFORMATION']['StructMetadata.0'][()].split()
        # Info returned is of type Byte, must convert to string before using it
        f_Metadata_byte2str = [s.decode('utf-8') for s in f_Metadata]
        # Get upper left points
        ulc = [i for i in f_Metadata_byte2str if 'UpperLeftPointMtrs' in i]
        ulcLon = float(ulc[0].replace('=', ',').replace('(', '') \
                .replace(')', '').split(',')[1])
        ulcLat = float(ulc[0].replace('=', ',').replace('(', '') \
                .replace(')', '').split(',')[2])
        return((ulcLon,  0, ulcLat, 0))
     #-------------------------------------------------------------------------
    # Function to read all datasets in the VIIRS HDF-EOS5 file
    def GetDatasetList(input_file):
        all_h5_objs = []
        input_file.visit(all_h5_objs.append)
        all_datasets = [str(obj) for obj in all_h5_objs if \
                        isinstance(f[obj],h5py.Dataset) and 'GRIDS' in obj]
        return(all_datasets)   
    #--------------------------------------------------------------------------
    # Batch process all files in input directory
    for vnp in file_list:
        # Maintain original filename convention    
        vnp_name = vnp.split('\\')[-1][:-3]  
        # Read in the VIIRS HDF-EOS5 file
        f = h5py.File(vnp, "r")
        # Retrieve Geolocation information for the file    
        geoInfo = GetGeographicInfo(f)
        # Retrieve list of VIIRS datasets    
        dsList = GetDatasetList(f)
        print('Processing: {}.h5'.format(vnp_name))
    #--------------------------------------------------------------------------
        # Loop through each dataset in the file and output as GeoTIFF
        for ds in dsList:
            dsName = ds.split('/')[-1]
            # Create array and read dimensions            
            dsArray = f[ds][()]
            nRow = dsArray.shape[0]
            nCol = dsArray.shape[1]
            geoInfo_sd = list(geoInfo)
            # Cell size not specified in the metadata of VIIRS version 001
            if nRow == 1200:    # VIIRS VNP09A1, VNP09GA - 1km
                yRes = -926.6254330555555    
                xRes = 926.6254330555555
            elif nRow == 2400:  # VIIRS VNP09H1, VNP09GA - 500m
                yRes = -463.31271652777775
                xRes = 463.31271652777775
            elif nRow == 3600 and nCol == 7200: # VIIRS VNP09CMG
                yRes = -0.05
                xRes = 0.05
                # Set upper left dims for CMG product                
                geoInfo_sd[0] = -180.00 
                geoInfo_sd[2] = 90.00
            # Set cell size and data type for output files
            geoInfo_sd.insert(1, xRes)    
            geoInfo_sd.insert(5, yRes)     
            dataType = gdal_array.NumericTypeCodeToGDALTypeCode(dsArray.dtype)
            # Output raster array to GeoTIFF file            
            driver = gdal.GetDriverByName(format)
            out_ds = driver.Create('{}/{}_{}.tif'.format(out_dir, vnp_name, \
                        dsName), nCol, nRow, 1, dataType)
            out_ds.SetGeoTransform(geoInfo_sd)        
            # Set output coordinate referense system information            
            if vnp_name[5:8] == 'CMG':  
                out_ds.SetProjection(projInfo[1])
            else:
                out_ds.SetProjection(projInfo[0])
            out_ds.GetRasterBand(1).WriteArray(dsArray)
            out_ds = None
            del geoInfo_sd, dataType, ds, dsArray, nCol, nRow, xRes, yRes
        print('Output location: {}'.format(out_dir))
#------------------------------------------------------------------------------
if __name__ == "__main__":
   main(sys.argv[1:])
#------------------------------------------------------------------------------       
