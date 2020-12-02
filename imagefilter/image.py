import logger
import cv2
import numpy as np
import sys


def open_image():
    image = cv2.imread('amongus.jpeg')
    logger.log(f'image ouverte')
    return image


def nb(image):
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        logger.log(f'image est en noir et blanc')
        return gray
    except:
        print("l'image n'est pas bonne")
        sys.exit()


def blur(image):
    try:

        ksize = (10, 10)
        blur = cv2.blur(image, ksize)
        logger.log(f'image floue')
        return blur
    except:
        print("l'image n'est pas bonne ou la valeur du flou est negative")
        sys.exit()


def dilate(image):
    try:
        kernel = np.ones((5, 5), np.uint8)
        dilation = cv2.dilate(image, kernel, 20)
        logger.log(f'image dilate')
        return dilation
    except:
        print("l'image n'est pas bonne")
        sys.exit()


def save(imageToSave):
    cv2.imwrite('imagesvg/image.jpeg', imageToSave)
    logger.log(f'image sauvegarde')


image = open_image()
image = nb(image)
save(image)

logger.dump_log()
