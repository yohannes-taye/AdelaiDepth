#!/bin/bash

python copy_to_server.py \
    --input '/home/tmc/project/AdelaiDepth/LeReS/Train/datasets/virtual_scene/annotations' \
    --output '/run/user/1000/gvfs/smb-share:server=tmc_datamanage.local,share=datasets/depthtraindata/AdelaiDepthTrainingData/DECEMBER-1-2022' \
    --debug

