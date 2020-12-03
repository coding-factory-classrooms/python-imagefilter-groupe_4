import cv2
import sys
import image as i
import os
import logger

args = sys.argv
image = ""


def commande():
    """
    check all the commande on cli
    :return: nothing
    """
    nbargs = 1

    taille = 0
    if args[1] == "-h":
        print("usage: imagefilter")
        print("--h,----help")
        print("-i,--input-dir <directory>")
        print("-o,--output-dir <directory>")
        print("--filters \"filters1|filters2|filters3\",--add filters on images")
        print("--------------filters:-----------")
        print("greyscale,--convert all the image of the input directory to black and white")
        print("blur,--convert all the image of the input directory to blur")
        print("dilate,--convert all the image of the input directory to dilate")
        sys.exit()


    if args[1] == "-i" or args[1] == "-o":

        if args[1] == "-i":

            i.path = args[2]
            nbargs = 3
        elif args[1] == "-o":
            i.folder = args[2]
            nbargs = 3
        if args[2] != None and args[3] == "-o":
            i.folder = args[4]
            nbargs = 5
    if args[nbargs] == "--filters":
        sep = args[nbargs+1].split("|")
        taille = len(sep)

    i.dico = i.open_image()

    for c in range(taille):
        argument = sep[c]

        if argument.find(":") >= 0:

            arg = argument.split(":")
            print(arg)
        if argument == "greyscale":

            i.dico = i.nb()

        elif arg[0] == "blur":

            i.dico = i.blur(int(arg[1]))

        elif arg[0] == "dilate":

            i.dico = i.dilate(int(arg[1]))



    i.save()


commande()


def createFolder(directory):
    """
    create the outpout directory
    :param directory: path where save images
    :return: nothing
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)




