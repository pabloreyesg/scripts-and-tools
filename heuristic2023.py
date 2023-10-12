import os
import re
def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes
def infotodict(seqinfo):
    t1w = create_key('sub-{subject}/anat/sub-{subject}_run-1_T1w')
    t2w = create_key('sub-{subject}/anat/sub-{subject}_run-1_T2w')
    FLAIR = create_key('sub-{subject}/anat/sub-{subject}_run-1_FLAIR')
    dwi = create_key('sub-{subject}/dwi/sub-{subject}_dir-AP_run-1_dwi')
    rest = create_key('sub-{subject}/func/sub-{subject}_task-RESTING_run-1_bold')
    fmap_rev_phase_dwi =  create_key('sub-{subject}/extra_data/sub-{subject}_dir-PA_dwi')
    fmap_rev_phase_func =  create_key('sub-{subject}/extra_data/sub-{subject}_dir-PA_func')
    swi = create_key('sub-{subject}/extra_data/sub-{subject}_run-1_SWI')
    info = {t1w: [], t2w:[], FLAIR: [], dwi: [], rest: [], fmap_rev_phase_dwi: []}
    for s in seqinfo:
        if (s.dim3 == 180) and (s.dim4 == 1) and ('T1' in s.protocol_name):
          info[t1w] = [s.series_id] # assign if a single series meets criteria
        if (s.dim3 == 170) and (s.dim4 == 1) and ('T2' in s.protocol_name):
          info[t2w] = [s.series_id] # assign if a single series meets criteria
        if (s.dim3 == 180) and (s.dim4 == 1) and ('FLAIR' in s.protocol_name):
          info[FLAIR] = [s.series_id] # assign if a single series meets criteria
        if (s.dim3 == 2040) and (s.dim4 == 1) and ('DTI32' in s.protocol_name):
          info[dwi].append(s.series_id) # append if multiple series meet criteria
        if (s.dim3 == 9456) and ('rsfMRI' in s.protocol_name):
          info[rest] = [s.series_id] # append if multiple series meet criteria
        if (s.dim3 == 60) and ('DTI32_OPP_B0_1' in s.protocol_name):
          info[fmap_rev_phase_dwi] = [s.series_id] # pepolar to DWI
        if (s.dim3 == 48) and ('rsfMRI_OPP_b0' in s.protocol_name):
          info[fmap_rev_phase_func] = [s.series_id] # append if multiple series meet criteria
        if (s.dim3 == 186) and ('VEN' in s.protocol_name):
          info[swi] = [s.series_id] # append if multiple series meet criteria
    return info
