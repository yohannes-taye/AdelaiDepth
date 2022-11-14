export PYTHONPATH=/home/tmc/project/AdelaiDepth/LeReS/Minist_Test

# python ./tools/test_depth.py --load_ckpt res50.pth --backbone resnet50

python ./tools/test_depth.py --load_ckpt res101.pth --backbone resnext101
