from ultralytics import YOLO

if __name__ == '__main__':
    #freeze_support()
    # Load the model.
    model = YOLO('C:\\Users\\laure\\OneDrive\\Documents\\CEC_2025\\CEC_Repo\\CEC2025\\yolomodel\\yolov8n.pt')

    # Training.
    results = model.train(
        data='C:\\Users\\laure\\OneDrive\\Documents\\CEC_2025\\CEC_Repo\\CEC2025\\yolomodel\\YOLOModel.yaml',  # Path to your custom data YAML file
        imgsz=224,
        epochs=1,
        batch=8,
        name='yolov8n_custom',
        project='C:\\Users\\laure\\OneDrive\\Documents\\CEC_2025\\CEC_Repo\\CEC2025\\yolomodel\\YOLOModel\\runs\\train'
    )