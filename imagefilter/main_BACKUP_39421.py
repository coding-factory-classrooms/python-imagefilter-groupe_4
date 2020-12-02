import cv2
import sys
import image as i
import os

args = sys.argv
image = ""

if args[1] == "open":
    image = i.open_image()
    if args[2] == "nb":
        image = i.nb(image)
        i.save(image)
    elif args[2] == "blur":
        image = i.blur(image)
        i.save(image)
    elif args[2] == "dilate":
        image = i.dilate(image)
        i.save(image)
<<<<<<< HEAD
if args[1] == "-h":
    print("usage: imagefilter")
    print("--h,----help")
    print("-i,--input-dir <directory>")
    print("-o,--output-dir <directory>")
=======
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

>>>>>>> 61e35003d608befa1880cd0e2d27fe5c78f897fa
