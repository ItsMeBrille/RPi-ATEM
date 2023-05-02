import cv2

# Load the video file
video_path = "video2.mp4"
cap = cv2.VideoCapture(video_path)

# Create a background subtractor object
backSub = cv2.createBackgroundSubtractorMOG2(history=10000, varThreshold=150, detectShadows=False)

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
    
    # Draw bounding boxes around the contours (i.e. people)
    if len(contours) > 0:
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w*h > 2000:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow("Frame", frame)
    
    # Exit on ESC key press
    if cv2.waitKey(1) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()