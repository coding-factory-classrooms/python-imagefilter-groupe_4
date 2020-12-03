import cv2
import numpy as np
import sys
import os
import logger

test = 1
nom_image = ""
dirs = os.listdir()
path = "img"
isImage = False
dico = {}
folder = 'output/'

def open_image():
    """
    open all the images of an folder
    :return: a dictionary with all the reference of images in a folders in input
    """
    dirs = os.listdir(path)
    nbImg = 0
    for file in dirs:
        if file.find(".png") >= 0 or file.find(".jpg")>= 0 or file.find(".jpeg"):
            dico[nbImg] = file
            nbImg = nbImg + 1

    print("l'image est ouverte")

    return dico
def nb():
    """
    add a grayscale to all the image
    :return: all the image with a grayscale filter
    """
    print("ici")
    gray = {}

    for n in dico:

        global isImage

        if isImage == False:

            imgPath = path+"/"+dico[n]

            image = cv2.imread(imgPath)
        else:
            image = dico[n]

        gray[n] = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


        #cv2.imwrite('output/' + 'image' + str(n) + '.jpeg', gray[n])
        print("l'image est noir est blanc")
    isImage = True
    return gray
def blur(height):
    """
    add a blur on all the images
    :param height: value oh the blur
    :return: a dico with all the image with a blur
    """
    print(height)
    ksize = (height,height)

    try:
        blur = {}

        for n in dico:
            global isImage
            if isImage == False:
                imgPath = path + "/" + dico[n]
                image = cv2.imread(imgPath)

            else:

                image = dico[n]



            blur[n] = cv2.blur(image, ksize)
            print("l'image est floue")
        isImage = True
        return blur
    except ValueError:
        print("l'image n'est pas bonne ou la valeur du flou est negative")
        sys.exit()
def dilate(height):
    """
    dilate all the image
    :param height: value of the dilatation
    :return: a dico with all the dilate's image
    """
    global isImage
    dilation = {}
    for n in dico:

        if isImage == False:

            imgPath = path + "/" + dico[n]
            image = cv2.imread(imgPath)

        else:
            image = dico[n]


        kernel = np.ones((5, 5), np.uint8)
        dilation[n] = cv2.dilate(image, kernel, height)
        print("l'image est dilate")
    isImage = True
    return dilation
def save():
    """
    save all the image in a folders
    :return: nothing
    """

    createFolder(folder)
    for n in dico:
        print(dico[n])
        cv2.imwrite(folder+'image'+str(n)+'.jpeg', dico[n])
        print("l'image est sauvegarder")
def createFolder(directory):

    try:
        if not os.path.exists(directory):
            os.makedirs(directory)


    except OSError:
        print('Error: Creating directory. ' + directory)



