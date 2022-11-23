export PYTHONPATH="/home/tmc/project/AdelaiDepth/LeReS/Minist_Test"
# run the ResNet-50
python ./tools/test_depth.py \
    --load_ckpt /home/tmc/project/AdelaiDepth/LeReS/Train/scripts/output/Nov22-15-07-59_tmc-lali/ckpt/epoch49_step2400.pth \
    --backbone resnet50 \
    --img_folder /home/tmc/Documents/Data/depth_test_data/A011_04010827_C017/480x270 \
    --save_folder /home/tmc/project/AdelaiDepth/LeReS/Train/scripts/output/depth_test/1/depth \
    --create_video \
    --video_name A008_10281102_C023_AdelaiDepth.mp4 \
    --fps 30 \
    --stich_with_rgb 
    --video_save_path /home/tmc/project/AdelaiDepth/LeReS/Train/scripts/output/depth_test/1/depth \
    # --debug



# python ./tools/test_depth.py \
#     --load_ckpt res50.pth \
#     --backbone resnet50 \
#     --img_folder /home/tmc/Documents/Data/depth_test_data/A011_04010827_C017/480x270 \
#     --save_folder /home/tmc/Documents/Data/depth_test_data/A011_04010827_C017/depth \
#     --create_video \
#     --video_name A008_10281102_C023_AdelaiDepth.mp4 \
#     --fps 30 \
#     --debug \
#     --trained_ckpt /home/tmc/project/AdelaiDepth/LeReS/Train/scripts/output/Nov17-09-59-01_tmc-lali/ckpt/epoch2_step40000.pth \
