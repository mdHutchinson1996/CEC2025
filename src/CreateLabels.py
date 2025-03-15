import os

def create_label_files(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        # Create a .txt file with the same name
        base_name, _ = os.path.splitext(filename)
        txt_filename = f"{base_name}.txt"
        txt_filepath = os.path.join(directory, txt_filename)

        # Write the specified content to the .txt file
        with open(txt_filepath, 'w') as txt_file:
            txt_file.write("0 0.5 0.5 1 1\n")

        print(f"Created {txt_filename}")

# Specify the directory
directory_path = 'C:\\Users\\laure\\OneDrive\\Documents\\CEC_2025\\CEC_2025\\val\\yes'
create_label_files(directory_path)