from ultralytics import YOLO
import os

# Load the trained model.
model = YOLO('C:\\Users\\laure\\OneDrive\\Documents\\CEC_2025\\CEC_Repo\\CEC2025\\yolomodel\\YOLOModel\\runs\\train\\yolov8n_custom4\\weights\\best.pt')  # Path to your trained model weights

# Specify the folder containing images.
image_folder = 'C:\\Users\\laure\\OneDrive\\Documents\\CEC_2025\\CEC_2025\\created_testing_data'

# Iterate over all files in the folder.
for filename in os.listdir(image_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):  # Add other image formats if needed
        image_path = os.path.join(image_folder, filename)
        
        # Predict on the image.
        results = model.predict(source=image_path, save=True)  # Path to the image you want to classify

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

        if belongs_to_yes_class:
            print(f"The model believes the input image {filename} belongs to the 'yes' class with a confidence of {confidence:.2f}.")
        else:
            print(f"The model believes the input image {filename} belongs to the 'no' class with a confidence of {confidence:.2f}.")

        # Print the results.
        #print(results)