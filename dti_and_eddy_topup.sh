#!/bin/bash

cd /home/pablo/Documents/MRI-CLINICAL/MELO-LAURA1/DTI_NX



echo "make folders"

mkdir top
mv DTI_NX_SENSE.nii top/data.nii
mv DTI_OPP_B0_1_SENSE.nii top/P2A_b0.nii
mv DTI_NX_SENSE.bvec top/bvecs
mv DTI_NX_SENSE.bval top/bvals

echo "make images for preprocess"

cd top
fslroi data A2P_b0 0 1
fslmerge -t A2P_P2A_b0 A2P_b0 P2A_b0
printf "0 1 0 0.03\n0 -1 0 0.03" > acqparams.txt 
topup --imain=A2P_P2A_b0 --datain=acqparams.txt --config=b02b0.cnf --out=my_topup_results --iout=my_hifi_b0
fslmaths my_hifi_b0 -Tmean my_hifi_b0
bet my_hifi_b0 my_hifi_b0_brain -m -f 0.35

indx=""
for ((i=1; i<=33; i+=1)); do indx="$indx 1"; done
echo $indx > index.txt

echo "start eddy"

eddy --imain=data --mask=my_hifi_b0_brain_mask --acqp=acqparams.txt --index=index.txt --bvecs=bvecs --bvals=bvals --topup=my_topup_results --out=eddy_corrected_data

cd ../
mkdir bedpostxfolder
cp top/eddy_corrected_data.nii.gz bedpostxfolder/data.nii.gz
cp top/my_hifi_b0_brain_mask.nii.gz bedpostxfolder/nodif_brain_mask.nii.gz
cp top/bvecs bedpostxfolder/
cp top/bvals bedpostxfolder/

echo "start bedpostx"

bedpostx_datacheck bedpostxfolder

#bedpostx_gpu bedpostxfolder

bedpostx bedpostxfolder



