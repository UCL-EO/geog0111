#!/usr/bin/env python

import requests
import numpy as np

class nsat():
    '''
    Get information on the number of satellite launches
    for all months in some range of years
    
    Data scraped from https://www.n2yo.com for
    years year0 to year1 (not inclusive)
    
    __author__ = "P Lewis"
    __copyright__ = "Copyright 2018 P Lewis"
    __license__ = "GPLv3"
    __email__ = "p.lewis@ucl.ac.uk"
    
    '''

    def __init__(self,year1=2020):
        '''
        check to see if data table available
        else, scrape
        '''
        year0=1957
        self.years = (year0,year1+1)
        filename = f'data/satellites-{self.years[0]}-{self.years[1]}.gz'
        try:
            data=np.loadtxt(filename)
        except:
            print(f'scraping {filename}')
            data = self.scrape_data(self.years)
            np.savetxt(filename,data,fmt='%d')
        self.data = data.astype(int)
            
    def scrape_data(self,years):
        # array of zeros
        nyears = years[1]-years[0]
        nmonths = 12

        data = np.zeros((nmonths,nyears),dtype=np.int) -1
        old = np.loadtxt('data/satellites-1957-2019.gz')
        # fill with what weve got but dont trust last year
        data[...,:old.shape[1]-1] = old[...,:old.shape[1]-1]
        indices = np.where(data == -1)
        newyears = indices[1] + years[0]  
        newmonths = indices[0] + 1 
        for j,i,mon,year in zip(indices[0],indices[1],newmonths,newyears):
          # find number of satellite launches
          # by scraping https://www.n2yo.com/browse/
          url = f"https://www.n2yo.com/browse/?y={year}&m={mon:02d}"
          try:
            r = int(requests.get(url).text.count('<a href="/satellite/?s='))
            data[j,i] = r
            print(year,mon,r)
          except:
            pass
        # tidy up
        data[data == -1] = 0 
        return data
