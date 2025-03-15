    
from ultralytics import YOLO
import os
import csv

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)

model = YOLO(parent_directory+'/yolomodel/YOLOModel/runs/train/yolov8n_custom4/weights/best.pt')  # Path to your trained model weights


 # Specify the folder containing images.
image_folder = parent_directory +'/TestLabelFolder'

def predict_images(image_path):
    # Iterate over all files in the folder.

        
        # Predict on the image.
    results = model.predict(image_path, save=True)  # Path to the image you want to classify

        # Extract the classification result.
    belongs_to_yes_class = False
    confidence = 0.0
    if results and hasattr(results[0], 'boxes'):
        for box in results[0].boxes:
                class_id = int(box.cls[0])
                class_name = results[0].names[class_id]
                confidence = box.conf[0]  # Extract the confidence score
                if class_name == 'yes':
                    belongs_to_yes_class = True
                    break


        
            
        #if belongs_to_yes_class:
        #    print(f"The model believes the input image {filename} belongs to the 'yes' class with a confidence of {confidence:.2f}.")
        #else:
        #    print(f"The model believes the input image {filename} belongs to the 'no' class with a confidence of {confidence:.2f}.")
        return(confidence, belongs_to_yes_class)



# Assuming parent_directory and model are already defined
image_folder = os.path.join(parent_directory, 'TestLabelFolder')


with open('predictedResults.csv', mode='w', newline='') as results_file, \
     open('predictedResults_Yes.csv', mode='w', newline='') as yes_only_file, \
     open('predictedResults_No.csv', mode='w', newline='') as no_only_file:
    
    results_writer = csv.writer(results_file)
    yes_only_writer = csv.writer(yes_only_file)
    no_only_writer = csv.writer(no_only_file)
    # Iterate over all files in the folder
    for filename in os.listdir(image_folder):
        if filename.endswith('.png') or filename.endswith('.jpg'):  # Add other image formats if needed
            image_path = os.path.join(image_folder, filename)
        
            # Predict on the image
            confidence, belongs_to_yes_class = predict_images(image_path)  # Path to the image you want to classify

            # Write the results to the CSV files
            if(belongs_to_yes_class):
                 yes_only_writer.writerow([float(confidence)])
                 results_writer.writerow(['yes'])

            if(not belongs_to_yes_class):
                no_only_writer.writerow([float(confidence)])
                results_writer.writerow(['no'])
