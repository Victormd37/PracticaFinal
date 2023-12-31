
import os
import shutil

def restructure_dataset(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each animal folder in the input dataset
    for animal_folder in os.listdir(input_folder):
        animal_path = os.path.join(input_folder, animal_folder)

        # Check if the item in the animal folder is a directory
        if os.path.isdir(animal_path):
            # Create the output subfolders for images and labels
            output_images_folder = os.path.join(output_folder, 'images')
            output_labels_folder = os.path.join(output_folder, 'labels')

            if not os.path.exists(output_images_folder):
                os.makedirs(output_images_folder)

            if not os.path.exists(output_labels_folder):
                os.makedirs(output_labels_folder)

            print(os.listdir(animal_path)[:-1])
            label_path = os.path.join(animal_path, 'Label')
            # Loop through images in the animal folder Excepte l'ultima que es Label
            for image_file in os.listdir(animal_path)[:-1]:
                image_path = os.path.join(animal_path, image_file)

                # Move images to the output images folder
                image_source = image_path
                image_destination = output_images_folder
                shutil.copy(image_source, image_destination)

            for label_file in os.listdir(label_path):
                # Move labels to the output labels folder
                label_source = os.path.join(label_path, label_file)
                label_destination = os.path.join(output_labels_folder, label_file)
                shutil.copy(label_source, label_destination)

            # Remove the animal folder and its subfolders
            #shutil.rmtree(animal_path)

# Example usage
input_dataset_folder = "test"
output_dataset_folder = "test_output"

restructure_dataset(input_dataset_folder, output_dataset_folder)