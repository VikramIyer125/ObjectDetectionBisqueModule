import cv2 
import os 
from object_detection import * 
import pdb



def run_module(input_path_dict, output_folder_path): 
    input_img_path = input_path_dict['Input Image'] 
    output = detect(input_img_path)
    out_image_path = "out_"+os.path.basename(input_img_path)
    cv2.imwrite(out_image_path, output)
    output_paths_dict = {}
    output_paths_dict['Output Image'] = os.path.join(output_folder_path, out_image_path)
    return output_paths_dict 

if __name__ == '__main__':
    input_path_dict = {}
    current_directory = os.getcwd()
    input_path_dict['Input Image'] = os.path.join(current_directory,'street.jpeg') # KEY MUST MATCH INPUT NAME SET IN CLI
    output_folder_path = current_directory
    output_paths_dict = run_module(input_path_dict, output_folder_path)
    output_img_path = output_paths_dict['Output Image'] 
    out_img = cv2.imread(output_img_path, 0)
    cv2.imshow("Result", out_img)


