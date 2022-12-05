#!/bin/bash
cd /home/tmc/project/AdelaiDepth/annotations/split_data

python new_split_data.py \
    --img_folder /home/tmc/Documents/virtual_scene_training_data2 \
    --output_folder ./test \


# python new_split_data.py \
#     --img_folder /home/tmc/Documents/virtual_scene_training_data/rgbs \
#     --output_folder /home/tmc/project/AdelaiDepth/annotations/output \
    # --debug true 