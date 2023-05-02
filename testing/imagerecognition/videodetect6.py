import cv2

# Load the video file
video_path = "video2.mp4"
cap = cv2.VideoCapture(video_path)

# Create a background subtractor object
backSub = cv2.createBackgroundSubtractorMOG2(history=600, varThreshold=80, detectShadows=False)

# Loop through the video frames
while cap.isOpened():
    # Read the next frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply background subtraction to get the foreground mask
    fgMask = backSub.apply(frame)
    
    # Apply morphological operations to remove noise from the mask
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_CLOSE, kernel)
    fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_OPEN, kernel)
    
    # Find contours in the mask
    contours, hierarchy = cv2.findContours(fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Select the largest bounding box and any additional boxes that are at least 2/3 the area of the largest box
    bounding_boxes = []
    if len(contours) > 0:
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w*h > 2200:
                bounding_boxes.append((x, y, x+w, y+h))
    
    selected_boxes = []
    if len(bounding_boxes) > 0:
        # Find the largest box
        largest_box = max(bounding_boxes, key=lambda box: (box[2]-box[0])*(box[3]-box[1]))
        selected_boxes.append(largest_box)
        
        # Find any additional boxes that are at least 2/3 the area of the largest box
        for box in bounding_boxes:
            if box != largest_box and (box[2]-box[0])*(box[3]-box[1]) >= 3/4*(largest_box[2]-largest_box[0])*(largest_box[3]-largest_box[1]):
                selected_boxes.append(box)
    

    # What to do for each person detected
    for box in selected_boxes:
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
    



    # Display the frame
    cv2.imshow("Frame", frame)
    
    # Exit on ESC key press
    if cv2.waitKey(1) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()