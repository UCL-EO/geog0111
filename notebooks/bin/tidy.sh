#!/bin/bash

rm -rf rm /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks/work/M*
rm -f /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks/work/.db.yml*
rm -rf /nfs/cfs/home3/Uucfa6/ucfalew/.url_db/
export CACHE_FILE="/shared/groups/jrole001/geog0111/work/database.db"
rm -f /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks/work/.db.yml
cp -r /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks/work/e4ftl01.cr.usgs.gov/* /shared/groups/jrole001/geog0111/work/e4ftl01.cr.usgs.gov
rm -rf /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks/work/e4ftl01.cr.usgs.gov
rm -f /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks/work/e4ftl01.cr.usgs.gov.store
mv /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks/work/e4ftl01.cr.usgs.gov ~/.trash
bin/database.sh
