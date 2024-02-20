import cv2  # For image processing
import easygui  # to open a filebox
import numpy as np  # to store a image
import imageio  # to read image stored at particular
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

# Making main widow
top = tk.Tk()
top.geometry('400x400')
top.title("Cartoonify Your Image!")
top.configure(background='white')
label = Label(top, background='#CDCDCD', font=('calibri', 20, 'bold'))


"""filedialogbox opena the box to choose file and help us store file path as string"""


def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)


def cartoonify(ImagePath):

    # read the image
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
# print(image) #image is stored in number form

    # confir that image is choosen
    if originalImage is None:
        print("Can not find any image. Choose apporiate file.")
        sys.exit()

    ReSized1 = cv2.resize(originalImage, (960, 540))

    #plt.imshow(ReSized1, cmap='gray')

    # converting image into grayscale
    grayScaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, (960, 540))
   # plt.imshow(ReSized2, cmp='gray')

    # Applying median blur to smooth an image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    ReSized3 = cv2.resize(smoothGrayScale, (960, 540))
    # plt.imshow(ReSized3, cmap='gray)

    # retrieving the edge for cartoon effect
    # by using thresholding technique
    getEdge = cv2.adaptiveThreshold(
        smoothGrayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    ReSized4 = cv2.resize(getEdge, (960, 540))
    #plt.imshow(ReSized4, cmp='gray')

    # applying bilateral filter to remove noise
    # and keep edge sharp as required
    colorImage = cv2.bilateralFilter(originalImage, 9, 300, 300)
    ReSized5 = cv2.resize(colorImage, (960, 540))
    #plt.imshow(ReSized5, cmap='map')

    # masking edged image with our beautify image
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)

    ReSized6 = cv2.resize(cartoonImage, (960, 540))
    # plt.imshow(ReSized6, cmap='gray')

    # plotting all images together
    images = [ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6]

    fig, axes = plt.subplots(3, 2, figsize=(8, 8), subplot_kw={
                             'xticks': [], 'yticks': []}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')

    # save button code
    save1 = Button(top, text="Save cartoon image", command=lambda: save(ReSized6,
                                                                        ImagePath), padx=30, pady=5)
    save1.configure(background='#364156', foreground='white',
                    font=('calibri', 10, 'bold'))
    save1.pack(side=TOP, pady=50)
    plt.show()


def save(ReSized6, ImagePath):
    # saving an image using imwrite()
    newName = "cartoonified_Image"
    path1 = os.path.dirname(ImagePath)
    extension = os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName+extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))
    I = "Image saved by name " + newName + " at " + path
    tk.messagebox.showinfo(title=None, message=I)


upload = Button(top, text='Cartoonify an Image',
                command=upload, padx=20, pady=5)
upload.configure(background='#364156', foreground='white',
                 font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)


top.mainloop()
