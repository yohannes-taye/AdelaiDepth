cd /home/tmc/project/AdelaiDepth/annotations/


python /home/tmc/project/AdelaiDepth/annotations/annotations.py \
    --csv_file /home/tmc/project/AdelaiDepth/annotations/output/annotations.csv \
    --img_folder /home/tmc/Documents/virtual_scene_training_data \
    --ouput_folder /home/tmc/project/AdelaiDepth/annotations/output \
    --rgb_extention jpeg \
    # --debug true 

mv /home/tmc/project/AdelaiDepth/annotations/output/val_all_annotations.json \
    /home/tmc/project/AdelaiDepth/annotations/output/all_annotations.json


cp /home/tmc/project/AdelaiDepth/annotations/output/*.json \
    /home/tmc/project/AdelaiDepth/LeReS/Train/datasets/virtual_scene/annotations

 