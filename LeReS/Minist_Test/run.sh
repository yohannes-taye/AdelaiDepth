export PYTHONPATH="/home/tmc/project/AdelaiDepth/LeReS/Minist_Test"
# run the ResNet-50

# /home/tmc/Documents/Data/depth_test_data/A008_10281559_C028
# /home/tmc/Documents/Data/depth_test_data/A011_04010827_C017/480x270
#/home/tmc/Documents/Data/depth_test_data/images2_
# /home/tmc/Documents/virtual_scene_training_data/rgbs/4_020
# /home/tmc/Documents/depth_test_data/rgb
# /run/user/1000/gvfs/smb-share:server=tmc_datamanage.local,share=datasets/depth train data/S2/4_020/rgb

python ./tools/test_depth.py \
    --load_ckpt /home/tmc/project/AdelaiDepth/LeReS/Train/scripts/output/Nov28-10-48-13_tmc-lali/ckpt/epoch43_step17400.pth \
    --backbone resnet50 \
    --img_folder "/run/user/1000/gvfs/smb-share:server=tmc_datamanage.local,share=datasets/depth train data/S2/4_020/rgb" \
    --save_folder /home/tmc/project/AdelaiDepth/LeReS/Train/scripts/output/depth_test/stage2-noise/depth \
    --create_video \
    --video_name A008_10281102_C023_AdelaiDepth.mp4 \
    --fps 30 \
    --stich_with_rgb \
    --video_save_path /home/tmc/project/AdelaiDepth/LeReS/Train/scripts/output/depth_test/2/depth \
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
