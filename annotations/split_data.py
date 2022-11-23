import argparse
import os 
import numpy as np 
import debugpy 


def split(data_folder): 
    #Get all folders in the data folder
    folders = os.listdir(data_folder)
    folders.sort()
    train = []
    val = []
    test = []
    for folder in folders:
        #Check if directory
        if os.path.isdir(os.path.join(data_folder, folder)):
            #Join path to folder
            path = os.path.join(data_folder, folder)
            img_list =  os.listdir(path)

            # Move 70% of images to train randomly
            while len(train) < 0.7*len(img_list):
                img = np.random.choice(img_list)
                train.append(os.path.join(path, img))
                img_list.remove(img) 
            
            # Move 70% of images to val randomly
            while len(val) < 0.7*len(img_list):
                img = np.random.choice(img_list)
                val.append(os.path.join(path, img))
                img_list.remove(img)
            
            for img in img_list:
                test.append(os.path.join(path, img))
    return train, val, test


#Function to export train val and test to csv file in the following format
#image_name, 1 if image_name in train, 1 if image_name in val, 1 image_name if in test
def export_csv(output_folder, train, val, test):
    with open(os.path.join(output_folder, 'annotations.csv'), 'w') as f:
        for img in train:
            f.write(img + ',1,0,0\n')
        for img in val:
            f.write(img + ',0,1,0\n')
        for img in test:
            f.write(img + ',0,0,1\n')
    print("Exported to csv at: ", os.path.join(args.output_folder, 'annotations.csv'))



def main(): 
    #take arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_folder', type=str, default='./images')
    parser.add_argument('--output_folder', type=str, default='./images')
    parser.add_argument('--debug', type=bool, default=False)
    
    args = parser.parse_args()

    if args.debug: 
        debugpy.listen(5678)
        print("Press play!")
        debugpy.wait_for_client()

    #get all the images in the folder and save path to list 
    train, val, test = split(args.img_folder)
    export_csv(args.output_folder, train, val, test)

    

if __name__ == '__main__':
    main()