import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('D:/html/New folder/haarcascade_frontalface_default.xml')
pic = cv2.imread('give the path of the picture')
scale_factor = 1.3
while 1:
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(pic,(x, y), (x+w, y+h), (225, 0, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic, 'me', (x, y), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

    print("number of faces found  {}".format(len(faces)))
     
    cv2.imshow('face', pic)
    k = cv2.waitkey(30) & 0xff
    if k == 2:
         break
cv2.destroyAllWindows()        
                                         
