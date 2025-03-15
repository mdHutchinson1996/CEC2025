import os
import shutil
import random
import sys

# Define the dataset path
CEC_2025_dataset = 'C:\\Users\\laure\\OneDrive\\Documents\\CEC_2025\\CEC_2025'

# Define the source folders
yes_folder = os.path.join(CEC_2025_dataset, 'yes')
no_folder = os.path.join(CEC_2025_dataset, 'no')

# Define the destination folder
destination_folder = os.path.join(CEC_2025_dataset, 'created_testing_data')

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Get all image files from the 'yes' and 'no' folders
yes_images = [os.path.join(yes_folder, f) for f in os.listdir(yes_folder) if os.path.isfile(os.path.join(yes_folder, f))]
no_images = [os.path.join(no_folder, f) for f in os.listdir(no_folder) if os.path.isfile(os.path.join(no_folder, f))]

# Randomly select 500 images from each folder
selected_yes_images = random.sample(yes_images, 500)
selected_no_images = random.sample(no_images, 500)

# Copy the selected images to the destination folder
for image in selected_yes_images + selected_no_images:
    shutil.copy(image, destination_folder)

print(f"500 images from 'yes' and 'no' folders have been copied to {destination_folder}")