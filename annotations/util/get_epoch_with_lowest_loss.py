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

def extract_data(epoch_step_data): 
    #Get first occurance of "Epoch"
    epoch_index = epoch_step_data.find("Epoch ")
    #Get first occurance of "/50"
    slash_index = epoch_step_data.find("/50")
    #Get the epoch number
    epoch = epoch_step_data[epoch_index + 6:slash_index]

    #Get first occurance of Step 
    step_index = epoch_step_data.find("Step ")
    shorted_string = epoch_step_data[step_index:]
    #Get first occurance of "]"
    close_bracket_index = shorted_string.find("/")
    #Get the step number
    step = shorted_string[5:close_bracket_index]

    #Get first occurance of "loss"
    loss_index = epoch_step_data.find("loss")
    shorted_string = epoch_step_data[loss_index:]
    #Get first occurance of ","
    comma_index = shorted_string.find(",")
    #Get the loss value
    loss = shorted_string[5:comma_index]
    loss = float(loss)

    return epoch, step, loss
    

    return 0 


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tensorlog', type=str)
    parser.add_argument('--debug', action='store_true', default=False)
    args = parser.parse_args()


    epoch_with_lowest_loss = {}
    min_loss = 999999999999; 
    if args.debug:
        print('Press play!')
        import debugpy
        debugpy.listen(5678)
        debugpy.wait_for_client()

    # Open tensorlog as text file
    with open(args.tensorlog, 'r') as f:
    
        lines = f.readlines()
        #Find the line with text "loss"
        for i in range(len(lines)):
            line = lines[i]
            if "save model" in line:

                epoch_step_data = lines[i - 4:i -2]
                epoch_step_data = "".join(epoch_step_data)
                epoch, step, loss = extract_data(epoch_step_data)
                if loss < min_loss: 
                    min_loss = loss
                    epoch_with_lowest_loss = {"epoch": epoch, "step": step, "loss": loss}


    printd(f"Epoch with lowest loss: {epoch_with_lowest_loss}")


if __name__ == "__main__": 
    main()