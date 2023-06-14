import cv2 

print("Program created by mr Umair")
face_cap = cv2.CascadeClassifier('/home/programmer/.local/share/virtualenvs/python-0P1cz62Y/lib/python3.10/site-packages/cv2/data/haarcascade_frontalface_default.xml')
video_capt = cv2.VideoCapture(0)

print("face is showing in camera & detector is enabled!")
while True:
    ret , video_data = video_capt.read()
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE

    )
    for (x,y,w,h) in faces :
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('video_live',video_data)
    
    if cv2.waitKey(20) == ord('a'):
        break



video_capt.release()
cv2.destroyAllWindows()
print("program closed ...bye.")
