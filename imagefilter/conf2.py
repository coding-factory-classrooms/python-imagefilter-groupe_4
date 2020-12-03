import image as i


def readfile():
    file = open("conf.txt",'r')
    for line in file:
        isActive = line.split("=")

        if line.find("input_dir=") >=0 and isActive[1] != "\n":
            if line.find("= ") >=0:
                command = line.split("= ")
            else:
                command = line.split("=")
            i.path = command[1]
            i.dico = i.open_image()
            i.dico = i.nb()
            i.save()
        if line.find("output_dir=") >=0 and isActive[1] != "\n":
            if line.find("= ") >=0:
                command = line.split("= ")
            else:
                command = line.split("=")
            i.folder = command[1]
            i.dico = i.open_image()
            i.dico = i.nb()
            i.save()
        if line.find("filters=") >=0 and isActive[1] != "\n":

            i.dico = i.open_image()
            if line.find("= ") >=0:
                command = line.split("= ")
            else:
                command = line.split("=")
            filtre = command[1].split("|")

            for c in filtre:

                if c == "grayscale":

                    i.dico = i.nb()

                if c.find("blur") >= 0:
                    sep = c.split(":")
                    i.dico = i.blur(int(sep[1]))
                if c.find("dilate") >= 0:
                    sep = c.split(":")

                    i.dico = i.dilate(int(sep[1]))


        i.save()


readfile()