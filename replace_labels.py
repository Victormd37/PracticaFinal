# Substituim labels per números enlloc d'strings
import os


# Function to replace animal strings with integers
def replace_animals_with_integers(file_path, animal_mapping):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        parts = line.strip().split()
        animal = ' '.join([part for part in parts if not part.replace('.', '', 1).isdigit()])
        if animal in animal_mapping:
            updated_lines.append(f"{animal_mapping[animal]} {' '.join(parts[len(animal.split()):])}\n")
    
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)
    

# Create a mapping of animal strings to integers
animal_names = ['Bear', 'Brown bear', 'Bull', 'Butterfly', 'Camel', 'Canary', 'Caterpillar', 'Cattle', 'Centipede', 'Cheetah', 'Chicken', 'Crab', 'Crocodile',
                'Deer', 'Duck', 'Eagle', 'Elephant', 'Fish', 'Fox', 'Frog', 'Giraffe', 'Goat', 'Goldfish', 'Goose', 'Hamster', 'Harbor seal', 'Hedgehog', 
                'Hippopotamus', 'Horse', 'Jaguar', 'Jellyfish', 'Kangaroo', 'Koala', 'Ladybug', 'Leopard', 'Lion', 'Lizard', 'Lynx', 'Magpie', 'Monkey', 
                'Moths and butterflies', 'Mouse', 'Mule', 'Ostrich', 'Otter', 'Owl', 'Panda', 'Parrot', 'Penguin', 'Pig', 'Polar bear', 'Rabbit', 'Raccoon', 
                'Raven', 'Red panda', 'Rhinoceros', 'Scorpion', 'Sea lion', 'Sea turtle', 'Seahorse', 'Shark', 'Sheep', 'Shrimp', 'Snail', 'Snake',
                'Sparrow', 'Spider', 'Squid', 'Squirrel', 'Starfish', 'Swan', 'Tick', 'Tiger', 'Tortoise', 'Turkey', 'Turtle', 'Whale', 'Woodpecker', 'Worm', 
                'Zebra']


# Create animal mapping (animal name to integer)
animal_mapping = {animal: index for index, animal in enumerate(animal_names)}

print("Animal Mapping:")
print(animal_mapping)

for folder_path in ['train_output', 'val_output']:
    # Iterate through each file in the labels folder
    labels_folder = os.path.join(folder_path, 'labels')
    for filename in os.listdir(labels_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(labels_folder, filename)

            # Read the file and replace animal strings with integers
            replace_animals_with_integers(file_path, animal_mapping)
