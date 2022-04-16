import os


def printFiles():
    path = "/home/lothri/Pictures/Wallpapers"

    for files in os.listdir(path):
        print(files)


printFiles()
