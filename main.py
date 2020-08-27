#import librarities

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_eye_xml')
face_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

#video cam variable
cap = cv2.VideoCapture(0)

#
while True:
    ret, img = cap.read()
    gray = cv.cvycolor(img, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+h]

    
        eyes = eye_cascade.detectMultiScale(rooi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),

    #within the whileloop,outside the face and eyes loop
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
