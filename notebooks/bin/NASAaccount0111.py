#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geog0111.cylog import Cylog
sites = ['https://n5eil01u.ecs.nsidc.org',\
         'https://urs.earthdata.nasa.gov',\
         'https://e4ftl01.cr.usgs.gov']
 
l = Cylog(sites)
test = l.login()

