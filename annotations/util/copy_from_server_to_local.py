import json
import argparse
import os 

import cv2
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
import numpy as np 

def printd(message, level=1): 
    if level == 1: 
        print(f"[INFO] {message}")
    elif level == 2: 
        print(f"[WARNING] {message}")
    else: 
        print(f"[DEBUG] {message}")


def chunk(l, n):
	# loop over the list in n-sized chunks
	for i in range(0, len(l), n):
		# yield the current n-sized chunk to the calling function
		yield l[i: i + n]

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def apply_agumentation(rgb_image, depth_image, agumentation_type):
    if agumentation_type == 0: 
        rgb_image = cv2.flip(rgb_image, 1)
        depth_image = cv2.flip(depth_image, 1)
    elif agumentation_type == 1:
        rgb_image = cv2.flip(rgb_image, 0)
        depth_image = cv2.flip(depth_image, 0)
    return rgb_image, depth_image


def process_images(payload): 
    printd(f"Process {payload['id']} started")
    agument_type = payload['agument_type']
    printd(f"Applying agumentation type -> {agument_type}")
    for data in payload['data']:
        printd(f"Processing {data['rgb_input_path']}")
        rgb_image = cv2.imread(data['rgb_input_path'])
        depth_image = cv2.imread(data['depth_input_path'])
        
        depth_image = cv2.cvtColor(depth_image, cv2.COLOR_BGR2GRAY)
        
        rgb_image, depth_image = apply_agumentation(rgb_image, depth_image, agument_type)

        printd(f"RGB image saved to {data['rgb_output_path']}")
        printd(f"Depth image saved to {data['depth_output_path']}")

        make_dir(data['rgb_output_path'])
        make_dir(data['depth_output_path'])

        rgb_image_name = data['rgb_input_path'].split("/")[-1]
        rgb_image_save_path = os.path.join(data['rgb_output_path'], rgb_image_name)

        depth_image_name = data['depth_input_path'].split("/")[-1]
        depth_image_name = depth_image_name.split(".")[0] + ".png"
        depth_image_save_path = os.path.join(data['depth_output_path'], depth_image_name)

        cv2.imwrite(rgb_image_save_path, rgb_image)
        cv2.imwrite(depth_image_save_path, depth_image)

    # for data in payload['data']:

    #     printd(f"Processing {data['rgb_input_path']}")
    printd(f"DONE: Process {payload['id']}") 




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', type=str)
    parser.add_argument('--output_folder', type=str)
    parser.add_argument('--ignore_folders', type=str, nargs='+', default=[])
    parser.add_argument('--debug', action='store_true', default=False)
    parser.add_argument('--rgb_folder_name', type=str, default='rgb')
    parser.add_argument('--depth_folder_name', type=str, default='depth')
    parser.add_argument('--agument_type', type=int, default=-1)
    parser.add_argument('--tag', type=str,  default="")
    args = parser.parse_args()

    #Aguement type 0: Flip rgb and depth images horizontally 
    #Aguement type 1: Flip rgb and depth images vertically


    if args.debug:
        print('Press play!')
        import debugpy
        debugpy.listen(5678)
        debugpy.wait_for_client()


    make_dir(args.output_folder)



    # Get all folders in input folder
    folders = [f for f in os.listdir(args.input_folder) if os.path.isdir(os.path.join(args.input_folder, f))]
    payloads = [] 


    #rgb_input_path
    #depth_input_path
    #rgb_output_path
    #depth_output_path
    for folder in folders: 

        if folder in args.ignore_folders:
            printd(f"Skipping folder {folder}", 2)
            continue


        rgb_images = [f for f in os.listdir(os.path.join(args.input_folder, folder, args.rgb_folder_name)) if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')]
        depth_images = [f for f in os.listdir(os.path.join(args.input_folder, folder, args.depth_folder_name)) if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')]
        rgb_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
        depth_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

        if len(rgb_images) != len(depth_images): 
            printd(f"Folder {folder} has different number of rgb images and depth images", level=2)
            continue
        

        for rgb_image, depth_image in zip(rgb_images, depth_images):
            payloads.append({
                'rgb_input_path': os.path.join(args.input_folder, folder, args.rgb_folder_name, rgb_image),
                'depth_input_path': os.path.join(args.input_folder, folder, args.depth_folder_name, depth_image),
                'rgb_output_path': os.path.join(args.output_folder, folder + args.tag, args.rgb_folder_name),
                'depth_output_path': os.path.join(args.output_folder, folder + args.tag, args.depth_folder_name)
            })
            
            # print(payloads[-1])
    
    if args.debug:
        payloads = payloads[:10]


    procs = os.cpu_count()

    numImagesPerProc = len(payloads) / float(procs)
    numImagesPerProc = int(np.ceil(numImagesPerProc))
    chunkedData = list(chunk(payloads, numImagesPerProc))
   
    #Prepare payload for each process
    payloads = []
    procs = min(procs, len(chunkedData))
    for i in range(procs):
        payloads.append({
            'id': i, 
            'data': chunkedData[i],
            'agument_type': args.agument_type
        })

    print(f"Starting {procs} processes")
    pool = Pool(processes=procs)
    payloads = payloads[:-1]
    pool.map(process_images, payloads)
    printd("waiting for processes to finish...")
    pool.close()
    pool.join()
    printd("multiprocessing complete")

if __name__ == "__main__": 
    main()