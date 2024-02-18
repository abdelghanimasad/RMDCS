import cv2
import torch
from PIL import Image
from yolov5 import YOLOv5
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

def count_vehicles_and_draw_boxes(image_path, conf_thres=0.25):
    # Load YOLOv5 model
    model = YOLOv5("yolov5s.pt", device=device)

    # Load image
    img = Image.open(image_path).convert('RGB')

    # Run model
    results = model.predict(img, size=640)

    # Filter detections based on confidence threshold
    filtered_detections = results.xyxy[0][results.xyxy[0][:, 4] >= conf_thres]

    # Process detections
    vehicle_detections = {'car': [], 'bus': [], 'van': []}  # Add more types if needed
    for det in filtered_detections:
        x1, y1, x2, y2, conf, cls = det
        cls = int(cls)
        if cls in [2, 5, 7]:  # Assuming 2: car, 5: bus, 7: van (check your model's class IDs)
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            if cls == 2:
                vehicle_detections['car'].append((x1, y1, x2, y2))
            elif cls == 5:
                vehicle_detections['bus'].append((x1, y1, x2, y2))
            elif cls == 7:
                vehicle_detections['van'].append((x1, y1, x2, y2))

    # Draw bounding boxes for detected vehicles
    draw_boxes(image_path, vehicle_detections)

    # Print the number of detected vehicles
    for vehicle_type, detections in vehicle_detections.items():
        print(f"Number of {vehicle_type}s detected: {len(detections)}")

def draw_boxes(image_path, vehicle_detections):
    image = cv2.imread(image_path)
    
    # Define colors for different vehicle types
    colors = {'car': (0, 255, 0), 'bus': (255, 0, 0), 'van': (0, 0, 255)}  # Add more types if needed

    # Draw bounding boxes
    for vehicle_type, detections in vehicle_detections.items():
        for (x1, y1, x2, y2) in detections:
            cv2.rectangle(image, (x1, y1), (x2, y2), colors[vehicle_type], 2)

    # Save the image 
    cv2.imwrite('vehicle_detection_output.jpg', image)
    #cv2.imshow("Vehicle Detections", image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

image_path = 'image_path2.jpeg'
count_vehicles_and_draw_boxes("imagepath3.webp", conf_thres=0.05)

