#!/bin/bash 

output_folder=./test 


rm -r $output_folder/*


python /home/tmc/project/AdelaiDepth/annotations/util/copy_from_server_to_local.py \
    --input_folder '/run/user/1000/gvfs/smb-share:server=tmc_datamanage.local,share=datasets/depthtraindata/depth' \
    --output_folder ./test \
    --ignore_folders x\
    --rgb_folder_name rgb \
    --depth_folder_name depth \
    --agument_type 1 \
    --tag _FV \
    # --debug \
 