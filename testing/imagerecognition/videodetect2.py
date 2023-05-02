import cv2 # Import the OpenCV library to enable computer vision
 
# Author: Addison Sears-Collins
# https://automaticaddison.com
# Description: Detect pedestrians in an image using the 
#   Histogram of Oriented Gradients (HOG) method
 
# Make sure the image file is in the same directory as your code
filename = 'image.png'
 
def main():
 
  # Create a HOGDescriptor object
  hog = cv2.HOGDescriptor()
     
  # Initialize the People Detector
  hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
     
  # Load an image
  image = cv2.imread(filename)
         
  # Detect people
  # image: Source image
  # winStride: step size in x and y direction of the sliding window
  # padding: no. of pixels in x and y direction for padding of sliding window
  # scale: Detection window size increase coefficient   
  # bounding_boxes: Location of detected people
  # weights: Weight scores of detected people
  (bounding_boxes, weights) = hog.detectMultiScale(image, 
                                                   winStride=(4, 4),
                                                   padding=(8, 8), 
                                                   scale=1.05)
 
  # Draw bounding boxes on the image
  for (x, y, w, h) in bounding_boxes: 
    cv2.rectangle(image, 
                  (x, y),  
                  (x + w, y + h),  
                  (0, 0, 255), 
                   4)
                     
  # Create the output file name by removing the '.jpg' part
  size = len(filename)
  new_filename = filename[:size - 4]
  new_filename = new_filename + '_detect.jpg'
     
  # Save the new image in the working directory
  cv2.imwrite(new_filename, image)
     
  # Display the image 
  cv2.imshow("Image", image) 
     
  # Display the window until any key is pressed
  cv2.waitKey(0) 
     
  # Close all windows
  cv2.destroyAllWindows() 
 
main()