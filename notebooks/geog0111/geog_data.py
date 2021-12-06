#!/usr/bin/env python
"""Procuring datasets for geog0111
The functions in this file deal with obtaining datasets for the Geog0111 course
at UCL Geography. The datasets are available over the internet, and are also
stored locally in the server. In case you're local to UCL Geography, symbolic
links will be created in your local folder, to avoid copying files across. If
you are outside, the files will be downloaded.

In either case, a directory called `data` will be created and things will end up
there.

From the user's provided perspective, each dataset will be a folder within somewhere
in the system. I recommend using symbolic links to make it accessible to the outside
work through e.g. `~/public_html`. Each folder should just contain a bunch of files,
so if you want to provide data in folders, provide a dataset for each of the folders.
"""

import urllib.request
from pathlib import Path
from socket import getfqdn
from geog0111.get_modis_files import get_modis_files
from bs4 import BeautifulSoup
import requests
__author__ = "J Gomez-Dans"
__copyright__ = "Copyright 2018 J Gomez-Dans"
__license__ = "GPLv3"
__email__ = "j.gomez-dans@ucl.ac.uk"
 
def procure_dataset(dataset_name, destination_folder="data",verbose=False,
                    locations=["/data/selene/ucfajlg/geog0111_data/",\
                               "/data/selene/ucfajlg/geog0111_data/lai_data/",\
                               "/archive/rsu_raid_0/plewis/public_html/geog0111_data"][::-1],\
                    modis_urls=['https://e4ftl01.cr.usgs.gov/MOTA',\
                                'https://e4ftl01.cr.usgs.gov/MOLT',\
                                'https://e4ftl01.cr.usgs.gov/MOLA',\
                                'https://e4ftl01.cr.usgs.gov//MODV6_Cmp_C/MOTA/',\
                                'https://e4ftl01.cr.usgs.gov/VIIRS',\
                                'https://n5eil01u.ecs.nsidc.org/MOST/',\
                                'https://n5eil01u.ecs.nsidc.org/MOSA/',\
                                'https://n5eil01u.ecs.nsidc.org/VIIRS/'],\
                    urls=["http://www2.geog.ucl.ac.uk/~ucfajlg/geog0111_data/",\
                          "http://www2.geog.ucl.ac.uk/~plewis/geog0111_data/",\
                          "http://www2.geog.ucl.ac.uk/~plewis/geog0111_data/lai_files/"][::-1]):

    """Procure a Geog0111 dataset. This function will look for the dataset called
    `dataset_name`, and either provide symbolic links or download the relevant
    files to a local folder called by default `data`, or with a user-provided name.
    The other two options are to do with the location of the dataset witin the UCL
    filesystem (`location`), and the external URL (list `urls`). It is assumed that in
    either case, `datasest_name` is a valid folder under both `location` and `url`.
    """
    dest_path = Path(destination_folder)
    if not dest_path.exists():
        dest_path.mkdir()
    output_fname = dest_path.joinpath(dataset_name)
    if output_fname.exists():
        return True

    done = False
    fully_qualified_hostname = getfqdn()
    if fully_qualified_hostname.find("geog.ucl.ac.uk") >= 0:
        if(verbose): print("Running on UCL's Geography computers")
        for location in locations:
            if(verbose): print(f'trying {location}')
            done =generate_symlinks(dataset_name, location, 
                                    destination_folder=destination_folder, verbose=verbose)
            if done:
                break
    else:
        if(verbose): print("Running outside UCL Geography. Will try to download data.\n",\
                            dataset_name,"\nThis might take a while!")
        for url in list(urls):
            if(verbose): print(f'trying {url}')
            done=download_data(dataset_name, url, verbose=verbose,destination_folder=destination_folder)
            if done:
                break
        if not done:
           # maybe a modis dataset: try that if its an hdf
           try:
               info = dataset_name.split('.')
               product = info[0]
               tile = info[2]
               version = int(info[3])
               year = int(info[1][1:5])
               doy = int(info[1][5:])
               dtype = info[-1]
               if dtype in ['hdf','tif']:
                   for url in modis_urls:
                       try:
                           filename = get_modis_files(doy,year,[tile],base_url=url,\
                                           version=version,\
                                           destination_folder=destination_folder,\
                                           product=product)[0]
                           done = True
                       except:
                           pass
           except:
               pass
    return(done)           
          
def generate_symlinks(dataset_name, location, destination_folder, verbose=True):
    """Generates symbolic links for a given dataset."""
    dest_path = Path(destination_folder)
    if not dest_path.exists():
        dest_path.mkdir()
        if verbose:
             print(f"Creating {str(dest_path):s}")
    the_path = Path(location)/Path(dataset_name)
    
    if the_path.exists():
        files = [f for f in the_path.rglob("**/*")]
        for fich in files:
            try:
                (dest_path/Path(fich.name)).symlink_to(fich)
            except FileExistsError:
                (dest_path/Path(fich.name)).unlink()
                (dest_path/Path(fich.name)).symlink_to(fich)
            if verbose:
                print(f"Linking {fich} to {dest_path/Path(fich.name)}")
        return(True)


def download_data(dataset_name, url, destination_folder, noclobber=True,verbose=True):
    """Downloads a dataset from UCL servers."""
    dest_path = Path(destination_folder)
    if not dest_path.exists():
        if verbose:
            print("Creating destination directory")
        dest_path.mkdir()
    try:
        resp = urllib.request.urlopen(f"{url:s}/{dataset_name:s}")
    except:
        return False
    if resp.code != 200:
        return False

    # try some easy things
    this_url = f"{url:s}/{dataset_name:s}"
    suffix = this_url.split('.')[-1]
    outfile = str(dest_path.joinpath(dataset_name))

    if (suffix=='npz') or (suffix=='zip') or (suffix=='hdf') \
       or (suffix=='nc') or (suffix=='bin'):
        try:
            with open(outfile,'wb') as fp:
                d = fp.write(requests.get(this_url).content)
            if d:
                return(True)
            else:
                Path(outfile).unlink()
        except:
            return(False)

    if (verbose):
        print(f'Now looking into {url:s}/{dataset_name:s}:')
    soup = BeautifulSoup(resp, "lxml",
                         from_encoding=resp.info().get_param('charset'))

    # this approach tries all the links if finds
    # at the url  

    for pos, link in enumerate(soup.find_all('a', href=True)):
        try:
            # Skip first crufty links...
            file_to_download = f"{url:s}/{dataset_name:s}/{link['href']:s}"
            dest_file = dest_path/Path(link['href'])
            #if dest_file.exists():
            #    dest_file.unlink()
            if dest_file.exists():
                local_size = dest_file.stat().st_size
                req = urllib.request.urlopen(file_to_download)
                hdrs = req.getheaders()
                for hdr in hdrs:
                    if hdr[0] == "Content-Length":
                        remote_size = int(hdr[1])
                if local_size != remote_size:
                    if verbose:
                        print('deleting unsound local file')
                    dest_file.unlink()
                if verbose:
                    print(f"Remote file: {link['href']:s} ({remote_size:d} bytes) " +
                          f"-> {dest_file.absolute()} ({local_size:d} bytes) -> " + u'\u2713')

            if not dest_file.exists():
                with open(dest_file, 'wb') as filep:
                    req = urllib.request.urlopen(file_to_download)
                    filep.write(req.read())
                hdrs = req.getheaders()
                for hdr in hdrs:
                    if hdr[0] == "Content-Length":
                        remote_size = int(hdr[1])
                local_size = dest_file.stat().st_size
                if local_size != remote_size:
                    raise IOError("Remote and local file sizes differ!")
                if verbose:
                    print(f"Remote file: {link['href']:s} ({remote_size:d} bytes) " +
                          f"-> {dest_file.absolute()} ({local_size:d} bytes) -> " + u'\u2713')
        except:
            pass
    return True    
