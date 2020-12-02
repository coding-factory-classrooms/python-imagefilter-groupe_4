import cv2
import sys
import image as i
import os
import logger

args = sys.argv
image = ""

def commande():
    sep = args[1].split("|")
    taille = len(sep)
    print(taille)
    image = i.open_image()
<<<<<<< HEAD

    for c in range(taille):
        argument = sep[c]

        if argument == "nb":
                image = i.nb(image)

        elif argument == "blur":

                image = i.blur(image)

        elif argument == "dilate":

                image = i.dilate(image)


        if argument == "-h":
            print("usage: imagefilter")
            print("--h,----help")
            print("-i,--input-dir <directory>")
            print("-o,--output-dir <directory>")
            print("nb,--convert all the image of the input directory to black and white")
            print("blur,--convert all the image of the input directory to blur")
            print("dilate,--convert all the image of the input directory to dilate")

    i.save(image)
commande()



=======
    if args[2] == "nb":
        image = i.nb(image)
        i.save(image)
    elif args[2] == "blur":
        image = i.blur(image)
        i.save(image)
    elif args[2] == "dilate":
        image = i.dilate(image)
        i.save(image)

if args[1] == "-h":
    print("usage: imagefilter")
    print("--h,----help")
    print("-i,--input-dir <directory>")
    print("-o,--output-dir <directory>")

if args[1] == "--filter":
    option = args[2]
    option = option.split("|")


def createFolder(directory):

    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


# Example
createFolder('./output/')
>>>>>>> 62c999f3fad62b46878f3b1a76555b66d6c9f504


