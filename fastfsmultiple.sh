#!/bin/bash

out="/media/pablo/Kirk/REDLATMA/FS"
bids="/media/pablo/Kirk/REDLATMA/bids"

for code in $(cat /media/pablo/Kirk/REDLATMA/subjectslist.txt)
	do

run_fastsurfer.sh --sd $out --sid sub-$code --t1 $bids/sub-$code/anat/sub-$code"_T1w.nii.gz" 

echo "done $code"

done
