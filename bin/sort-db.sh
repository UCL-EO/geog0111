#!/bin/bash 

# run as 
# bin/sort-db.sh > $CACHE_FILE

if  [[ -z "$CACHE_FILE" ]]; then
  export CACHE_FILE="work/database.db"
fi

if  [[ -z "$CACHE_FILE" ]]; then
  idir=$(echo $CACHE_FILE | awk -F/ 'BEGIN{str="/"} {for(i=1;i<NF;i++)str=str"/"$i} END{print(str)}')
else
  idir="work/datasets"
  export CACHE_FILE="$idir/database.db"
fi

cd $idir
#pwd
echo "query:"
ls */M*.store |  cut -d. -f1,2,3,4 | awk '{print("  https://"$0":");print("  - https://"$0)}'
ls */M*/*.store  | cut -d. -f1,2,3,4,5 | awk '{print("  https://"$0":");print("  - https://"$0)}'
ls */M*/*/*.store | cut -d. -f1,2,3,4,5,6,7 | awk '{print("  https://"$0":");print("  - https://"$0)}'

for site in $(ls -d *) ; do
  if [ -d $site ] ; then
    for mod in ${site}/* ; do
      if [ -d ${mod} ] ; then
        for prod in ${mod}/* ; do
          if [ -d ${prod} ] ; then
            for date in ${prod}/* ; do
              if [ -d ${date} ] ; then
                ls  ${date}/*hdf.store  | cut -d. -f1,2,3,4,5,6,7 > /tmp/base.$$
                ls  ${date}/*hdf.store  | cut -d. -f9 > /tmp/tile.$$
                ls  ${date}/*hdf.store | sed 's/hdf.store/hdf/' > /tmp/all.$$
                paste /tmp/base.$$ /tmp/tile.$$ /tmp/all.$$ | awk '{print("  https://"$1"*."$2"*.hdf:");print("  - https://"$3)}'
                rm -f /tmp/base.$$ /tmp/tile.$$ /tmp/all.$$
              fi
            done
          fi
        done
      fi
    done
  fi
done
exit 0
cat << EOF
SDS:
  MCD12Q1:
  - LC_Type1
  - LC_Type2
  - LC_Type3
  - LC_Type4
  - LC_Type5
  - LC_Prop1_Assessment
  - LC_Prop2_Assessment
  - LC_Prop3_Assessment
  - LC_Prop1
  - LC_Prop2
  - LC_Prop3
  - QC
  - LW
  MCD15A3H:
  - Fpar_500m
  - Lai_500m
  - FparLai_QC
  - FparExtra_QC
  - FparStdDev_500m
  - LaiStdDev_500m
  MOD10A1:
  - NDSI_Snow_Cover
  - NDSI_Snow_Cover_Basic_QA
  - NDSI_Snow_Cover_Algorithm_Flags_QA
  - NDSI
  - Snow_Albedo_Daily_Tile
  - orbit_pnt
  - granule_pnt
  MYD10A1:
  - NDSI_Snow_Cover
  - NDSI_Snow_Cover_Basic_QA
  - NDSI_Snow_Cover_Algorithm_Flags_QA
  - NDSI
  - Snow_Albedo_Daily_Tile
  - orbit_pnt
  - granule_pnt
EOF

rm -f /tmp/all.$$
touch /tmp/all.$$
echo "data:"
here=$(pwd)
for site in $(ls -d *) ; do
  if [ -d $site ] ; then
    for mod in ${site}/* ; do
      if [ -d ${mod} ] ; then
        for prod in ${mod}/* ; do
          if [ -d ${prod} ] ; then
            for date in ${prod}/* ; do
              if [ -d ${date} ] ; then
                ls ${site}/${mod}/${prod}/${date}/*hdf.store  | sed 's/hdf.store/hdf/' >> /tmp/all.$$
              fi
            done
          fi
        done
      fi
    done
  fi
done
awk < /tmp/all.$$ -v here=$here '{print("  https://"$1":");print("  - "here "/" $1 ".store")}'


