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



        if file.find(".png") >= 0 or file.find(".jpg") >= 0 or file.find(".jpeg") >= 0:

            dico[nbImg] = file
            nbImg = nbImg + 1

    logger.log(f'image ouverte')

    return dico


def nb():
    """
    add a grayscale to all the image
    :return: all the image with a grayscale filter
    """

    gray = {}
    print(len(dico))
    for n in dico:

        try:
            global isImage

            if isImage == False:

                imgPath = path + "/" + dico[n]

                image = cv2.imread(imgPath)
            else:
                image = dico[n]

            gray[n] = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # cv2.imwrite('output/' + 'image' + str(n) + '.jpeg', gray[n])
            logger.log(f'image est en noir et blanc')
        except cv2.error:
            print("error during the grayscales")

    isImage = True
    return gray





def blur(height):
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
    except cv2.Error:
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
        try:
            if isImage == False:

                imgPath = path + "/" + dico[n]
                image = cv2.imread(imgPath)

            else:
                image = dico[n]

            kernel = np.ones((5, 5), np.uint8)
            dilation[n] = cv2.dilate(image, kernel, height)
            logger.log(f'image est dilate')
        except:
            print("error during the dilation")
    isImage = True
    return dilation

def FilterZeTeam():
    """
    Add text on the image
    """
    global isImage
    font = cv2.COLOR_BGR2GRAY
    bottomLeftCornerOfText = (10, 500)
    fontScale = 1
    fontColor = (255, 255, 255)
    lineType = 2
    zeTeam = {}
    for n in dico:
        try:
            if isImage == False:

                imgPath = path + "/" + dico[n]
                image = cv2.imread(imgPath)

            else:
                image = dico[n]
            logger.log(f"ajout de la team")
            zeTeam[n] = cv2.putText(image,'-produit par: Alexandre, Angel, Alban',
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            lineType)
            isImage = True
            return zeTeam
        except:
            print("error during the filterZeTeam")


def save():
    """
    save all the image in a folders
    :return: nothing
    """

    createFolder(folder)
    for n in dico:




        #print(dico[n])
        cv2.imwrite(folder + 'image' + str(n) + '.jpeg', dico[n])

        logger.log("l'image est sauvegarder")


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)


    except OSError:
        print('Error: Creating directory. ' + directory)


