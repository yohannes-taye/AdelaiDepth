export PYTHONPATH="/home/tmc/project/AdelaiDepth/LeReS/Minist_Test"
# run the ResNet-50
python ./tools/test_depth.py \
    --load_ckpt res50.pth \
    --backbone resnet50 \
    --img_folder /home/tmc/Documents/Data/chui/A008_10281102_C023 \
    --save_folder /home/tmc/Documents/Data/chui/A008_10281102_C023_AdelaiDepth \
    --create_video \
    --video_name A008_10281102_C023_AdelaiDepth.mp4 \
    --fps 30
