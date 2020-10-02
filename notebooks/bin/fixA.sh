#!/bin/bash

cd notebooks/bak

mv A01_Groups.ipynb 060_Groups.ipynb
mv A02_Script.ipynb 061_Script.ipynb
mv A03_Part1.ipynb 062_Part1.ipynb
mv  A03_Part1_code.ipynb 063_Part1_code.ipynb
mv A04_Numpy.ipynb 064_Numpy.ipynb
mv A05_LAI.ipynb 065_LAI.ipynb
mv A06_Part2.ipynb 066_Part2.ipynb

for i in * ; do
  sed < $i 's/A01_/060_/g' | sed 's/A02_/061_/g' | sed 's/A03_Part1_code.iynb/063_Part1_code.ipynb/g'  | sed 's/A03_Part1.ipynb/062_Part1.ipynb/g'  | sed 's/A04_/064_/g' | sed 's/A05_/065_/g' | sed 's/A06_/066_/g' > ../$i
done



