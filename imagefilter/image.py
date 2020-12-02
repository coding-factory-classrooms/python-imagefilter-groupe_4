import cv2
import numpy as np
import sys

def open_image():


        image = cv2.imread('amongus.jpeg')
        print("l'image est ouverte")
        return image
def nb(image):
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("l'image est noir est blanc")
        return gray
    except:
        print("l'image n'est pas bonne")
        sys.exit()
def blur(image):
    try:

        ksize = (10, 10)
        blur = cv2.blur(image, ksize)
        print("l'image est floue")
        return blur
    except:
        print("l'image n'est pas bonne ou la valeur du flou est negative")
        sys.exit()
def dilate(image):
    try:
        kernel = np.ones((5, 5), np.uint8)
        dilation = cv2.dilate(image,kernel ,20)
        print("l'image est dilate")
        return dilation
    except:
        print("l'image n'est pas bonne")
        sys.exit()
def save(imageToSave):
    cv2.imwrite('imagesvg/image.jpeg', imageToSave)
    print("l'image est sauvegarder")


image = open_image()
image = nb()
save(image)
