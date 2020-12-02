import cv2
import sys
import image as i
import os
import logger

args = sys.argv
image = ""


def commande():
    nbargs = 1
    if args[1] == "-i" or args[1] =="-o":
        if args[1] == "-i":

            i.path = args[2]
            nbargs = 3
        elif args[1] =="-o":
            i.folder = args[2]
            nbargs = 3
        if args[2] != None and args[3] == "-o":
            i.folder = args[4]
            nbargs = 5

    sep = args[nbargs].split("|")
    taille = len(sep)

    i.dico = i.open_image()

    for c in range(taille):
        argument = sep[c]

        if argument == "nb":
            i.dico = i.nb()

        elif argument == "blur":

            i.dico = i.blur()

        elif argument == "dilate":

            i.dico = i.dilate()

        if argument == "-h":
            print("usage: imagefilter")
            print("--h,----help")
            print("-i,--input-dir <directory>")
            print("-o,--output-dir <directory>")
            print("nb,--convert all the image of the input directory to black and white")
            print("blur,--convert all the image of the input directory to blur")
            print("dilate,--convert all the image of the input directory to dilate")

    i.save()



commande()


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


# Example
createFolder('./output/')
