from datetime import datetime

def get_doy(year,month,day):
    '''
    function that is given 
    
    the year 
    and month integer 
        
    and returns the day of year
    '''
    doy = (datetime(year,month,day) - datetime(year-1,12,31)).days
    return doy

