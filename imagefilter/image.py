import cv2
import numpy as np

def open_image():
    image = cv2.imread('amongus.jpeg')
    return image



def nb(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray
def blur(image):
    ksize = (10, 10)
    blur = cv2.blur(image, ksize)
    return blur
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(image,kernel ,20)
    return dilation
def save(imageToSave):
    cv2.imwrite('imagesvg/image.jpeg', imageToSave)



image = open_image()
dilatation = dilate(image)
save(dilatation)