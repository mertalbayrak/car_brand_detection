# Python 2/3 uyumluluk
from __future__ import print_function
import cv2
import numpy as np
import os

# Dataset'i klasörden çekilip, belirli bir düzen üzerine başka bir dosyaya kaydediliyor.
# Örnek kaydetme: neg/1.jpg
def storeImages():
    if not os.path.exists('neg'):
        os.makedirs('neg')

    pictureNumber = 1
    # /home/mert/Downloads/DataSets/1524400000
    for fileType in ['images']:
        for image in os.listdir(fileType):
            try:
                print("Image: "+str(pictureNumber))
                # Resim okunup, siyah beyaz yapılıyor
                image = cv2.imread(str(fileType) + '/' + str(image), cv2.IMREAD_GRAYSCALE)
                # Resim yeniden boyutlandırılıyor.
                resizeImage = cv2.resize(image, (100, 100))
                # Örnek kaydetme: neg/1.jpg
                # Resim yeni rengi ve boyutu ile tekrardan dosyaya kaydediliyor.
                cv2.imwrite("neg/"+ str(pictureNumber)+ '.jpg',resizeImage)
                pictureNumber += 1

            except Exception as e:
                print(str(e))

def find_crash_image():
    for file_type in ['neg']:
        for image in os.listdir(file_type):
            for crash in os.listdir('data/crash_image'):
                try:
                    
                    current_image_path = str(file_type) + '/' + str(image)
                    crash = cv2.imread('data/crash_image/'+str(crash))
                    question = cv2.imread(current_image_path)
                    # Url'den hatalı inmiş olan resimler, 
                    # örnek hatalı bir resim ile xor işleminden geçiyor ve hatalı resim siliniyor.
                    if crash.shape == question.shape and not(np.bitwise_xor(crash, question).any()):
                        print('Broken image')
                        print(current_image_path)
                        os.remove(current_image_path)
                    
                except Exception as e:
                    print(str(e))


def createPosAndNeg():
    for fileType in ['neg']:
        for image in os.listdir(fileType):
            if fileType == 'neg':
                # neg dosyanın içindeki resimler kullanılarak bg.txt dosyası oluşturuluyor.
                # bg.txt -> Resim bilgilerinin tutulduğu txt.
                line = fileType+'/'+image+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
            elif fileType == 'pos':
                line = image+ ' 1 0 0 50 50\n'
                with open('pos/pos.txt', 'a') as f:
                    f.write(line)
    
storeImages()
find_crash_image()
createPosAndNeg()
