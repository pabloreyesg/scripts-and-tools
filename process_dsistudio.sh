#!/bin/bash

folder="/home/pablo/Documents/MRI-CLINICAL"

read -p "Enter foldername: " subject

cd $folder

dsi_studio --action=src --source=$folder/$subject/DTI_NX/bedpostxfolder/data.nii.gz
dsi_studio --action=rec --source=$folder/$subject/DTI_NX/bedpostxfolder/*.src.gz --method=4 --param0=1.25 --output=$folder/$subject/DTI_NX/bedpostxfolder/
dsi_studio --action=atk --source=$folder/$subject/DTI_NX/bedpostxfolder/*.fib.gz --tractography_atlas=4 --track_id=corticospinal
dsi_studio --action=atk --source=$folder/$subject/DTI_NX/bedpostxfolder/*.fib.gz