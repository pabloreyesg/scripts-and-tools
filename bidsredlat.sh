#!/bin/bash

from='/mnt/NAS-docs/Neuroimagenes/Kangaroo'
to='/media/pablo/8e95eef0-a766-496a-855d-1c15f66c6c39/KMC_data/raw'

for f in $(cat /lista.txt)
	do
cp $from/$f $to/
cd $to/$f
tar -xvzf *.tar.gz
mkdir sub-$f
dicomsorter dcm sub-$f


 
	
done


