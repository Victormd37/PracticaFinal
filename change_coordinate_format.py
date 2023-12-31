import pybboxes as pbx
import os
from PIL import Image 

# Set the path to your folder
folder_path = 'train_output'

# Function to replace animal strings with integers
def change_format_and_normalize_coord(file_label_path, W, H):
    with open(file_label_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        parts = line.strip().split()
        voc_bbox = [float(num) for num in parts[1:]]
        new_coord = pbx.convert_bbox(voc_bbox, from_type="voc", to_type="yolo", image_size=(W,H))
        new_coord_str = [str(num) for num in new_coord]
        # Guardem label numerica amb coord amb format yolo
        updated_lines.append(f"{parts[0]} {' '.join(new_coord_str)}\n")
        #print(file_label_path, W,H)
        #print(updated_lines)
        #print()
    with open(file_label_path, 'w') as file:
        file.writelines(updated_lines)
    
labels_folder = os.path.join(folder_path, 'labels')
images_folder = os.path.join(folder_path, 'images')

for filename in os.listdir(labels_folder):
    if filename.endswith(".txt"):
        file_label_path = os.path.join(labels_folder, filename)
        file_image_path = os.path.join(images_folder, f'{filename[:-4]}.jpg')
        img = Image.open(file_image_path)
        W,H = img.width, img.height
        # Read the file and replace animal strings with integers
        change_format_and_normalize_coord(file_label_path, W, H)
