#!/bin/bash 

export PYTHONPATH="/home/tmc/project/AdelaiDepth/LeReS/Minist_Test"
export CUDA_VISIBLE_DEVICES=0

#Get path to video file
DEPTH_RESULT_FOLDER=/home/tmc/project/AdelaiDepth/LeReS/Train/scripts/output/depth_test
# VIDEO_PATH=/home/tmc/Documents/Data/depth_test_data/A011_04010827_C017/480x270
# VIDEO_PATH=/home/tmc/Documents/depth_test_data/real_life
VIDEO_PATH=/home/tmc/project/AdelaiDepth/LeReS/Train/scripts/output/depth_test/rgb/depth

declare -a IGNORE_FOLDERS=("rgb" "DPT" "base_line" "stage2" "stage3-noise2" "stage2-noise"   "stage3-noise")

########## 
############

#Get folders in depth result folder
for folder in $DEPTH_RESULT_FOLDER/*; do
    #Get folder name
    folder_name=$(basename $folder)
    
    #Check if folder is in ignore list
    if [[ " ${IGNORE_FOLDERS[@]} " =~ " ${folder_name} " ]]; then
        echo "Ignoring folder: $folder_name"
        continue
    fi

    echo "Processing folder: $folder_name"
    
    
    #Get the first file in the folder
    ckpt=$(ls "$folder/ckpt" | head -n 1)
    ckpt="$DEPTH_RESULT_FOLDER/$folder_name/ckpt/$ckpt"
    save_folder="$DEPTH_RESULT_FOLDER/$folder_name/depth"
    video_save_path="$DEPTH_RESULT_FOLDER/$folder_name"

    

    echo "Save folder: $save_folder"
    echo "Ckpt: $ckpt"
    echo "Video path: $VIDEO_PATH"
    echo "Video save path: $video_save_path"

    rm $save_folder/*
    rm $video_save_path/*.mp4


    python ./tools/test_depth.py \
        --load_ckpt $ckpt \
        --backbone resnet50 \
        --img_folder $VIDEO_PATH \
        --save_folder $save_folder \
        --video_save_path $video_save_path \
        # --create_video \
        # --video_name video.mp4 \
        # --fps 30 \
        # --stich_with_rgb \
     
done