import cv2
import sys
import image as i

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
if args[1] == "-h":
    print("usage: imagefilter")
    print("--h,----help")
    print("-i,--input-dir <directory>")
    print("-o,--output-dir <directory>")
