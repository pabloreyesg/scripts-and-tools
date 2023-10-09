#!/bin/bash


pathbids="/home/labneuro/Documents/Kangaroo/bids"


for code in sub-9 sub-9c sub-15 sub-19 sub-20 sub-25 sub-29 sub-31 sub-35 sub-44 sub-51 sub-53a sub-53c sub-54 sub-56 sub-64 sub-65 sub-69 sub-71 sub-72 sub-75 sub-83 sub-90 sub-93 sub-95 sub-107 sub-108 sub-113 sub-119 sub-121 sub-123 sub-124 sub-125 sub-128 sub-129 sub-134 sub-138 sub-141 sub-143 sub-144 sub-145 sub-149 sub-150 sub-151 sub-153 sub-154 sub-155 sub-156 sub-157 sub-161 sub-161c sub-165 sub-172 sub-172a sub-172c sub-173 sub-175 sub-176 sub-177 sub-182 sub-185 sub-186 sub-186c sub-195 sub-197 sub-198 sub-201 sub-202 sub-205 sub-208 sub-210a sub-210c sub-212a sub-212c sub-216 sub-219 sub-221 sub-225 sub-227 sub-230 sub-231 sub-232 sub-235 sub-237 sub-253 sub-256 sub-261 sub-263 sub-266 sub-274 sub-277 sub-288a sub-288c sub-292 sub-293 sub-300 sub-301 sub-307 sub-310 sub-312 sub-313 sub-314 sub-319 sub-320 sub-322 sub-327 sub-331 sub-332 sub-333 sub-344 sub-346 sub-348 sub-353 sub-355 sub-356 sub-357 sub-358 sub-364 sub-369 sub-371 sub-374 sub-381 sub-382 sub-390 sub-396 sub-399 sub-402 sub-409 sub-413 sub-416 sub-417 sub-423 sub-424 sub-426 sub-427 sub-429 sub-431 sub-432 sub-440 sub-441 sub-452 sub-456 sub-458 sub-464 sub-469 sub-472 sub-478 sub-480 sub-483 sub-484 sub-485 sub-491 sub-496 sub-499 sub-504 sub-517 sub-526 sub-532 sub-535 sub-536 sub-537 sub-542 sub-544 sub-545 sub-547 sub-548 sub-549 sub-552 sub-566 sub-568a sub-568c sub-576 sub-577 sub-579 sub-580 sub-586 sub-592 sub-593 sub-595 sub-598a sub-598c sub-599 sub-600 sub-602 sub-610 sub-611 sub-615 sub-616 sub-619 sub-623 sub-625 sub-630 sub-631 sub-645 sub-650 sub-651 sub-662 sub-665 sub-670 sub-675 sub-678a sub-678c sub-684 sub-686 sub-689 sub-691 sub-694 sub-696 sub-712 sub-715 sub-734 sub-737 sub-739a sub-739c sub-748 sub-752a sub-752c sub-754 sub-758 sub-761 sub-765 sub-769 sub-783 sub-784 sub-786 sub-789 sub-790 sub-791 sub-795 sub-799a sub-799c sub-804 sub-806 sub-815 sub-818 sub-820 sub-821 sub-829 sub-840 sub-841 sub-848 sub-850 sub-858 sub-861 sub-863 sub-868 sub-869 sub-874 sub-876 sub-877 sub-878 sub-879 sub-884 sub-891 sub-892 sub-893 sub-894 sub-898 sub-905 sub-906 sub-912 sub-913 sub-914 sub-918 sub-928 sub-932 sub-934 sub-935 sub-939 sub-940 sub-942 sub-953 sub-954 sub-965 sub-966 sub-971 sub-973 sub-982 sub-984 sub-992 sub-994 sub-996 sub-1005 sub-1006 sub-1021 sub-1026 sub-1039 sub-1049 sub-1063 sub-1063c sub-1076 sub-1077 sub-1213a sub-1213c sub-1218 sub-1221 sub-1224 sub-1227 sub-1232 sub-1234a sub-1234c sub-1237 sub-1239a sub-1239c sub-1242 sub-1244 sub-1247a sub-1247c sub-1249 sub-1251a sub-1251c sub-1253 sub-1260 sub-1262 sub-1265 sub-1267 sub-1268a sub-1268c sub-1269a sub-1269c sub-1271a sub-1271c sub-1278a sub-1278c sub-1283a sub-1283c sub-1291a sub-1291c sub-1304a sub-1304c sub-1318a sub-1318c sub-1322 sub-1326 sub-1333 sub-1336 sub-1337 sub-1338 sub-1340 sub-1357; do

filename=/home/labneuro/Documents/Kangaroo/bids/$code/anat/$code'_acq-MPRAGE_run-1_T1w.nii'

filename2=/home/labneuro/Documents/Kangaroo/bids/sub-35/derivates/prepro-coord/$code'_task-coordinacion_run-1_bold.nii'


if [ -f "$filename" ];

then

    echo "$filename found"
    
    if [ -f "$filename2" ];
    
    then
    
        echo "$filename2 found"
    
	sed -i "s/sub-000/$code/g" coordderiva_mprage_job.m 

	matlab -nodesktop -nosplash -r "coordderiva_mprage"

	sed -i "s/$code/sub-000/g" coordderiva_mprage_job.m 

	else
	
	echo "$filename2 has not been found" >> notfouncoor.txt
	
	fi
   else
   echo "$filename has not been found" >> notfoundmprage.txt
   fi

echo 


done
