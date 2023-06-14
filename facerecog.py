import cv2 

print("Program created by mr Umair")

video_capt = cv2.VideoCapture(0)


while True:
    ret , video_data = video_capt.read()
    cv2.imshow('video_live',video_data)
    if cv2.waitKey(20) == ord('a'):
        break


video_capt.release()
cv2.destroyAllWindows()
