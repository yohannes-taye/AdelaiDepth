import argparse
import os 
import numpy as np 
import debugpy 


def split(data_folder): 
    #Get all folders in the data folder
    folders = os.listdir(data_folder)
    folders.sort()

    images = []

    train = []
    val = []
    test = []
    for folder in folders:
        #Check if directory
        if os.path.isdir(os.path.join(data_folder, folder)):
            #Join path to folder
            path = os.path.join(data_folder, folder, 'rgb')
            img_list =  os.listdir(path)

            #add images to list
            for img in img_list:
                images.append(os.path.join(path, img))

    #shuffle images
    np.random.shuffle(images)
    #split images into train, val and test
    train_size = int(0.7 * len(images))
    val_size = int(0.7 * (len(images) - train_size))
    test_size = len(images) - train_size - val_size

    images_length = len(images)

    train = images[:train_size]
    val = images[train_size:train_size + val_size]
    test = images[train_size + val_size:]

    print("Train size: ", len(train))
    print("Val size: ", len(val))
    print("Test size: ", len(test))
    print("Total size: ", len(train) + len(val) + len(test))
    print("Images length: ", images_length)
    return train, val, test


#Function to export train val and test to csv file in the following format
#image_name, 1 if image_name in train, 1 if image_name in val, 1 image_name if in test
def export_csv(output_folder, train, val, test):
    #create output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(os.path.join(output_folder, 'annotations.csv'), 'w') as f:
        for img in train:
            f.write(img + ',1,0,0\n')
        for img in val:
            f.write(img + ',0,1,0\n')
        for img in test:
            f.write(img + ',0,0,1\n')
    print("Exported to csv at: ", os.path.join(output_folder, 'annotations.csv'))



def main(): 
    #take arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_folder', type=str, default='./images')
    parser.add_argument('--output_folder', type=str, default='./images')
    parser.add_argument('--debug', default=False, action='store_true')
    
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