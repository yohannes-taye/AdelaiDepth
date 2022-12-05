#!/bin/bash

output_folder=./test
train_dir=/home/tmc/project/AdelaiDepth/LeReS/Train/datasets/virtual_scene/annotations
# train_dir=./test2
cd /home/tmc/project/AdelaiDepth/annotations/


python /home/tmc/project/AdelaiDepth/annotations/new_split_data.py \
    --img_folder /home/tmc/Documents/virtual_scene_training_data2 \
    --output_folder $output_folder \

python /home/tmc/project/AdelaiDepth/annotations/new_annotations.py \
    --csv_file $output_folder/annotations.csv \
    --img_folder /home/tmc/Documents/virtual_scene_training_data2 \
    --ouput_folder $output_folder \
    --rgb_extention jpeg \
    # --debug

mv $output_folder/val_all_annotations.json \
   $output_folder/all_annotations.json

cp $output_folder/*.json $train_dir

# python /home/tmc/project/AdelaiDepth/annotations/annotations.py \
#     --csv_file /home/tmc/project/AdelaiDepth/annotations/output/annotations.csv \
#     --img_folder /home/tmc/Documents/virtual_scene_training_data \
#     --ouput_folder /home/tmc/project/AdelaiDepth/annotations/output \
#     --rgb_extention jpeg \
#     # --debug true 

# mv $output_folder/val_all_annotations.json \
#    $output_folder/all_annotations.json

# cp /home/tmc/project/AdelaiDepth/annotations/output/*.json \
#     /home/tmc/project/AdelaiDepth/LeReS/Train/datasets/virtual_scene/annotations
