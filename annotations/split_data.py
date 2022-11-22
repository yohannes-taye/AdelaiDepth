import argparse
import os 
import numpy as np 
import debugpy 


def split(img_folder): 
    img_list =  os.listdir(img_folder)
    
    train = []
    val = []
    test = []
    


    # Move 70% of images to train randomly
    while len(train) < 0.7*len(img_list):
        img = np.random.choice(img_list)
        train.append(img)
        img_list.remove(img) 
    
    # Move 70% of images to val randomly
    while len(val) < 0.7*len(img_list):
        img = np.random.choice(img_list)
        val.append(img)
        img_list.remove(img)
    
    test = img_list 
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
    print("Exported to csv at: ", os.path.join(output_folder, 'annotations.csv'))



def main(): 
    #take arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_folder', type=str, default='./images')
    parser.add_argument('--output_folder', type=str, default='./images')
    
    args = parser.parse_args()

    #get all the images in the folder and save path to list 
    train, val, test = split(args.img_folder)
    export_csv(args.output_folder, train, val, test)

    print("shit")
    

if __name__ == '__main__':
    debugpy.listen(5678)
    print("Press play!")
    debugpy.wait_for_client()
    main()