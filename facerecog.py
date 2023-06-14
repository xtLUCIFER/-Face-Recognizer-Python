import cv2

# Print program information
print("Program created by Mr. Umair")

# Load face cascade classifier
face_cap = cv2.CascadeClassifier('/home/programmer/.local/share/virtualenvs/python-0P1cz62Y/lib/python3.10/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# Initialize video capture
video_capt = cv2.VideoCapture(0)

# Print information about face detection
print("Face is being detected in the camera feed. The detector is enabled!")

while True:
    # Read a frame from the video capture
    ret, video_data = video_capt.read()
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = face_cap.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the frame with face detections
    cv2.imshow('Video Live', video_data)
    
    # Check for 'a' key press to exit the program
    if cv2.waitKey(20) == ord('a'):
        break

# Release the video capture and close all windows
video_capt.release()
cv2.destroyAllWindows()

# Print program closing message
print("Program closed. Goodbye!")
