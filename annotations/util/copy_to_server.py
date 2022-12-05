import json
import argparse
import os 



def printd(message, level=1): 
    if level == 1: 
        print(f"[INFO] {message}")
    else: 
        print(f"[DEBUG] {message}")

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', type=str)
    parser.add_argument('--output_folder', type=str)
    parser.add_argument('--debug', action='store_true', default=False)
    args = parser.parse_args()



    if args.debug:
        print('Press play!')
        import debugpy
        debugpy.listen(5678)
        debugpy.wait_for_client()

    make_dir(args.output_folder)

    # Get all json files
    json_files = [f for f in os.listdir(args.input_folder) if f.endswith('.json')]

    for f in json_files:
        with open(os.path.join(args.input_folder, f), 'r') as j:
            data = json.load(j)
            printd("Processing file: {}, with length {}".format(f, len(data)))
            
            make_dir(os.path.join(args.output_folder, f.split('.')[0]))
            rgb_output_path = os.path.join(args.output_folder, f.split('.')[0], 'rgb')
            depth_output_path = os.path.join(args.output_folder, f.split('.')[0], 'depth')
            make_dir(rgb_output_path)
            make_dir(depth_output_path)
            for i in range(len(data)):
                rgb_path = data[i]['rgb_path']
                depth_path = data[i]['depth_path']

                #Copy file in path rgp_path to output_path  
                os.system(f"cp {rgb_path} {rgb_output_path}")
                os.system(f"cp {depth_path} {depth_output_path}")

    # a = open(f'{output_folder}/test_annotations.json', 'w')
    # json.dump(test, a)

if __name__ == "__main__": 
    main()