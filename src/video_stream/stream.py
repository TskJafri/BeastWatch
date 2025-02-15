from ultralytics import YOLO
import cv2
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
# print(f"Using {device} device")

# Load YOLO model (Ensure you have the correct model file)
model = YOLO('yolov11n.pt')  # Use YOLOv8 model (nano version for speed)
model.to(device)

# Define path to video file
source = "../../sample_data/bear.mp4"

# Open video file
cap = cv2.VideoCapture(source)

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Process video frame-by-frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Stop if the video ends

    # Run YOLO inference on the frame
    results = model(frame)

    # Loop through results
    for result in results:
        boxes = result.boxes  # Bounding boxes object

        if boxes is not None:
            for box in boxes:
                xyxy = box.xyxy[0].cpu().numpy().astype(int)  # Bounding box coordinates
                confidence = box.conf[0].cpu().numpy().item()  # Confidence score
                class_id = int(box.cls[0])  # Class index
                
                label = f"{model.names[class_id]} {confidence:.2f}"
                
                # Draw bounding box and label on the frame
                cv2.rectangle(frame, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (0, 255, 0), 2)
                cv2.putText(frame, label, (xyxy[0], xyxy[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("YOLOv8 Inference", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
