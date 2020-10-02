#!/bin/bash

# MV LAI files
odir=/shared/groups/jrole001/geog0111/work/MCD15A3H
mkdir -p $odir
files=$(grep ucfalew /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/work/MCD15A3H/*| awk -F: '{print $1}')
for f in $files
do
of=$(echo $f |awk -F/ '{print $NF}')
sed < $f 's/\notebooks//' | sed  's/\/nfs\/cfs\/home3\/Uucfa6\/ucfalew\//\/shared\/groups\/jrole001\//' > ${odir}/$of

done

cp /shared/groups/jrole001/geog0111/work/database.db  /shared/groups/jrole001/geog0111/work/database.db.bak
sed < /shared/groups/jrole001/geog0111/work/database.db 's/notebooks\///'  | sed 's/\/nfs\/cfs\/home3\/Uucfa6\/ucfalew\//\/shared\/groups\/jrole001\//' > tmp.$$
paste /shared/groups/jrole001/geog0111/work/database.db  tmp.$$ | grep vrt | sed 's/-//g' | awk '{print("mv "$0)}' | /bin/bash
cp tmp.$$ /shared/groups/jrole001/geog0111/work/database.db 
mv tmp.$$ work/.db.yml
