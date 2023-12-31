import os
import shutil
from sklearn.model_selection import train_test_split

def split_validation_dataset(input_test_folder, output_validate_folder, validation_size=0.5, random_seed=42):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_validate_folder):
        os.makedirs(output_validate_folder)

    # List image files in the input test folder
    image_files = [f for f in os.listdir(os.path.join(input_test_folder, 'images')) if os.path.isfile(os.path.join(input_test_folder, 'images', f))]

    # Split the test dataset into validation and remaining test sets
    remaining_test_images, validate_images = train_test_split(image_files, test_size=validation_size, random_state=random_seed)

    # Create folders for validation images and labels
    output_validate_images_folder = os.path.join(output_validate_folder, 'images')
    output_validate_labels_folder = os.path.join(output_validate_folder, 'labels')

    if not os.path.exists(output_validate_images_folder):
        os.makedirs(output_validate_images_folder)
    if not os.path.exists(output_validate_labels_folder):
        os.makedirs(output_validate_labels_folder)

    # Move validation images and labels to the output validation folder
    for image_file in validate_images:
        shutil.move(os.path.join(input_test_folder, 'images', image_file), os.path.join(output_validate_images_folder, image_file))
        shutil.move(os.path.join(input_test_folder, 'labels', f"{image_file.split('.')[0]}.txt"), os.path.join(output_validate_labels_folder, f"{image_file.split('.')[0]}.txt"))

# Example usage
input_test_folder = "test_output"
output_validate_folder = "val_output"

split_validation_dataset(input_test_folder, output_validate_folder)
