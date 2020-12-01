import cv2

def open_image():
    image = cv2.imread('helloWorld.png')
    return image



def nb(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray
def blur(image):
    ksize = (10, 10)
    blur = cv2.blur(image, ksize)
    return blur
def save(imageToSave):
    cv2.imwrite('imagesvg/image.jpeg', imageToSave)



image = open_image()
blur = blur(image)
save(blur)