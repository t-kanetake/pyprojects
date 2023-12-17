# project: face detector
# created: 12/15/2023

import cv2

# creates an object of cascadeclassifier class with xml file
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# reads images and detects faces in it
img = cv2.imread("")

# converts image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# detects faces in the image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# highlights faces in image
for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

# shows image with highlighted faces and waits for keypress to close window
cv2.imshow("img", img)
cv2.waitKey()

# saves image with face_detected name in disk
cv2.imwrite("face_detected.png", img)