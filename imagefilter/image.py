import cv2

def open_image():
    image = cv2.imread('helloWorld.png')
    cv2.imshow('Original image',image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('imagesvg/image.jpeg', gray)
open_image()