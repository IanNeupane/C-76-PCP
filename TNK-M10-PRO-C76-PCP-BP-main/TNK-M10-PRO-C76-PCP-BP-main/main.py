from cvzone.FaceDetectionModule import FaceDetector
import cv2
import numpy as np
from keras.models import load_model
import os

path = 'Pneumothorax-New-Dataset'

img = cv2.imread("Pneumothorax-New-Dataset/1_image_100.jpg")

# Load the model
ageDetectionModel = load_model('age_model_50epochs.h5', compil e= False)

try:    
    resizedImg = cv2.resize(img, (200, 200))
    resizedImg = np.array([resizedImg])

    # Pridict if the image is infected or not and save it in variable 'prediction'
    prediction = ageDetectionModel.predict(resizedImg)

    # If prediction is less then 0.5 then save "infected" in variable 'text" else save "uninfected"
    img = cv2.putText(img, str(int(prediction[0][0])), (X, Y), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 2)
    
    img = cv2.rectangle(img, (10, 10), (300, 100), (255, 255, 255), -1)
    
    img = cv2.resize(img, (300, 400))  
    img = cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.4, (225, 0, 0), 1)
      
    cv2.imshow("Image", img)
except Exception as e:
    print(e)
cv2.waitKey(0)