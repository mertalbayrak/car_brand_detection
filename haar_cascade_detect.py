# Python 2/3 uyumluluk
from __future__ import print_function
import cv2
import numpy as np
import os

carCascade = cv2.CascadeClassifier('data/cascade.xml')
pictureNumber = 1
# /home/mert/Downloads/DataSets/1524400000
for fileType in ['/home/mert/Downloads/DataSets/1524400000']:
    for image in os.listdir(fileType):
        print(image)
        image = cv2.imread(str(fileType) + '/' + str(image))
        # Yüklenen resim siyah beyaz renge dönüştürülüyor.
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        car = carCascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (35,35))
        for (x,y,w,h) in car:
            # Ekranda çizilen dikdörtgen üzerine açıklama yazılıyor.
            #cv2.putText(image, "Logo", (x-w, y-h), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1, cv2.LINE_AA)
            cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0), 2)
        
        # Resim yakalanmış hali ile test klasörü altına kaydediliyor.
        cv2.imwrite("test/"+str(pictureNumber)+'.jpg', image)
        pictureNumber += 1