import os
import numpy as np
import shutil
import csv
import json
import cv2
import debugpy 


def collect_imgs_num():
    path = '/mnt/taskonomy/Taskonomy/Selected_Images'
    depth_path = path + '/depths'
    rgb_path = path + '/rgbs'
    scenes = os.listdir(rgb_path)
    scenes.sort()
    num = 0
    for s in scenes:
        s_d_path = os.listdir(os.path.join(depth_path, s))
        s_i_path = os.listdir(os.path.join(rgb_path, s)) 
        d_num = len(s_d_path)
        i_num = len(s_i_path)
        if d_num != i_num:
            print(s, d_num, i_num, 'Not equal!!!')
        else:
            num += i_num
    print(num)

def split_train_val_test_scenes(csv_file):
    csv_file = open(csv_file, 'r')
    all_list = list(csv.reader(csv_file))
    train = []
    val = []
    test = []
    for i, v in enumerate(all_list):
        if i == 0:
            continue
        if int(v[1]) == 1:
            train.append(v[0].strip())
        elif int(v[2]) == 1:
            val.append(v[0].strip())
        elif int(v[3]) == 1:
            test.append(v[0].strip())
    print('train scenes num: %d, val scenes num: %d, test scenes num: %d' % (len(train), len(val), len(test)))
    return train, val, test, train+val+test

def create_annotations(csv_file, img_folder, output_folder):
    train_scene, val_scene, test_scene, all_scene = split_train_val_test_scenes(csv_file)
    path = img_folder
    depths_dir = path + '/depths'
    rgbs_dir = path + '/rgbs'
    scenes = os.listdir(rgbs_dir)
    scenes.sort()
    num = 0
    train = []
    val = []
    test = []
    for s in scenes:
        if s not in all_scene:
            print(s)
        
        s_i = os.listdir(os.path.join(rgbs_dir, s)) 
        s_d = os.listdir(os.path.join(depths_dir, s))
        for d in s_d:
            if d.replace('png', 'jpg') in s_i:
                depth_path = os.path.join(f'{img_folder}/depths', s, d)
                rgb_path = os.path.join(f'{img_folder}/rgbs', s, d.replace('png', 'jpg'))
                anno = {}
                anno['rgb_path'] = rgb_path
                anno['depth_path'] = depth_path
                if d.replace('png', 'jpg') in train_scene:
                    train.append(anno)
                elif d.replace('png', 'jpg') in val_scene:
                    val.append(anno)
                elif d.replace('png', 'jpg') in test_scene:
                    test.append(anno)
                #else:
                    #print(s, 'not specified')
            else:
                 print(d)


    print('train size:', len(train))
    print('val size:', len(val))
    print('test size:', len(test))
    val_small = np.random.choice(val, 1000)
    a= open(f'{output_folder}/train_annotations.json', 'w')
    json.dump(train, a)
    a.close()
    a= open(f'{output_folder}/val_all_annotations.json', 'w')
    json.dump(val, a)
    a.close()
    a= open(f'{output_folder}/test_annotations.json', 'w')
    json.dump(test, a)
    a.close()
    print('val_small size:', len(val_small))
    a= open(f'{output_folder}/val_annotations.json', 'w')
    json.dump(list(val_small), a)
    a.close()   

def depth_statistics():
    path = '/mnt/taskonomy/Taskonomy/Selected_Images'
    depths_dir = path + '/depths'
    scenes = os.listdir(depths_dir)
    scenes.sort()
    num = 0
    dmax = 0
    dmin = 60000
    for s in scenes:
        s_d = os.listdir(os.path.join(depths_dir, s))
        for d in s_d:
            depth_path = os.path.join(depths_dir, s, d)
            depth = cv2.imread(depth_path, -1)
            depth[depth == 65535] = 0
            print(depth.max(), depth[depth>1e-8].min())
            dmax = depth.max() if depth.max() > dmax else dmax
            dmin = depth[depth>1e-8].min() if depth[depth>1e-8].min() < dmin else dmin
    print(dmax, dmin)

if __name__ == '__main__':

    # Get images folder 
    import argparse
    parse_args = argparse.ArgumentParser()
    parse_args.add_argument('--csv_file', type=str, default='cvv.csv')
    parse_args.add_argument('--img_folder', type=str, default='./images')
    parse_args.add_argument('--ouput_folder', type=str, default='./output')
    args = parse_args.parse_args()


    debugpy.listen(5678)
    print("Press play!")
    debugpy.wait_for_client()

    # collect_imgs_num()

    #If output folder does not exist, create it
    if not os.path.exists(args.ouput_folder):
        os.makedirs(args.ouput_folder)

    create_annotations(args.csv_file, args.img_folder, args.ouput_folder)
    #depth_statistics()


