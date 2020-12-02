import cv2
import sys
import image as i
import os

args = sys.argv
image = ""

def commande():
    sep = args[1].split("|")
    taille = len(sep)
    print(taille)
    image = i.open_image()

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





