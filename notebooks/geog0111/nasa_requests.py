import requests
from pathlib import Path
from geog0111.cylog import Cylog
from geog0111.gurlib import URL

__author__ = "P Lewis"
__copyright__ = "Copyright 2018 P Lewis"
__license__ = "GPLv3"
__email__ = "p.lewis@ucl.ac.uk"

'''
acts like request, but for NASA Earthdata URLs, it adds in your
username and password.
'''

def get(url):
    r1 = None
    r2 = None
    try:
        with requests.Session() as session:
            # get password-authorised url
            session.auth = cylog().login()
            r1 = session.request('get',url)
            # this gets the url with codes for login etc.
            if r1.url:
                r2 = session.get(r1.url)
                return(r2)
    except:
        for r in (r1,r2):
            if r:
                r.ok = False
                return r
    return(None)


def test(site=Nonei,file=None):
  site = site or 'https://e4ftl01.cr.usgs.gov'
  file = file or 'MOTA/MCD15A3H.006/2018.09.30/BROWSE.MCD15A3H.A2018273.h00v08.006.2018278143557.1.jpg'
  return URL(site,file).ping()
