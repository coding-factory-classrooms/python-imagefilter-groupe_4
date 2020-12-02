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


def open_image():
    image = {}
    dirs = os.listdir(path)
    nbImg = 0
    for file in dirs:
        dico[nbImg] = file


        nbImg = nbImg + 1

    print("l'image est ouverte")

    return dico


def nb():
    gray = {}
    for n in dico:
        global isImage
        if isImage == False:
            print(isImage)
            imgPath = path+"/"+dico[n]

            image = cv2.imread(imgPath)
        else:


            image = dico[n]
        gray[n] = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #cv2.imwrite('output/' + 'image' + str(n) + '.jpeg', gray[n])
        print("l'image est noir est blanc")
    isImage = True
    return gray




def blur():
    try:
        blur = {}

        for n in dico:
            global isImage
            if isImage == False:
                imgPath = path + "/" + dico[n]
                image = cv2.imread(imgPath)

            else:

                image = dico[n]

            ksize = (10, 10)

            blur[n] = cv2.blur(image, ksize)
            print("l'image est floue")
        isImage = True
        return blur
    except:
        print("l'image n'est pas bonne ou la valeur du flou est negative")
        sys.exit()


def dilate():
    global isImage
    dilation = {}
    for n in dico:

        if isImage == False:

            imgPath = path + "/" + dico[n]
            image = cv2.imread(imgPath)

        else:
            image = dico[n]


        kernel = np.ones((5, 5), np.uint8)
        dilation[n] = cv2.dilate(image, kernel, 20)
        print("l'image est dilate")
    isImage = True
    return dilation


def save():

    folder = './output/'
    createFolder(folder)
    for n in dico:

        cv2.imwrite('output/'+'image'+str(n)+'.jpeg', dico[n])
        print("l'image est sauvegarder")
def createFolder(directory):

    try:
        if not os.path.exists(directory):
            os.makedirs(directory)


    except OSError:
        print('Error: Creating directory. ' + directory)


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)


    except OSError:
        print('Error: Creating directory. ' + directory)


dico = open_image()


dico = dilate()
dico = blur()

dico = nb()
save()
