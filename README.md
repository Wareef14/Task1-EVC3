#  Building a GUI with OpenCv and Tkinter in Python

This code is a Python script that allows the user to perform some basic operations on an image file. The script uses two libraries: tkinter and OpenCV.

Before we begin to explain the code let's get to know the most important libraries used.

1- tkinter : is a standard Python library for creating graphical user interfaces (GUIs). It provides a set of tools to create windows, buttons, text boxes, and other GUI elements that can interact with the user.

2- OpenCV : (Open Source Computer Vision Library) is a popular computer vision library that provides tools for image and video processing. It has a large collection of functions for image manipulation, including image filtering, segmentation, feature detection, and geometric transformations.
## Now, let's go through the code line by line:

Frist of all, We must import the necessary libraries,`tkinter` for creating the GUI, `filedialog` for opening and saving files, and `cv2` for image processing.
```
import tkinter as tk

from tkinter import filedialog

import cv2
```
-----
We want to allow the user to select an image file from their computer, which can then be displayed in an OpenCV window.

The function makes use of the `filedialog` module from the tkinter library to display a file selection dialog box. Once the user selects an image file, the function reads the image using `cv2.imread()` function and stores it in a global variable called `img_original`. The function then displays the image in a window using the `cv2.imshow()` function.
```
def open_image():
    global img_path, img_original
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    img_original = cv2.imread(img_path)
    cv2.imshow("Original Image", img_original)
    cv2.waitKey(0)
```
---
when user select the image, he/she will be able to try five OpenCv function, which are: Rotate,Resize,Grayscale,Save image,exit.

1- Rotate Function 

This function defines what happens when the "Rotate" button is clicked. It rotates the image by a fixed angle (45 degrees) using `cv2.getRotationMatrix2D()` and `cv2.warpAffine()`, then displays the rotated image using `cv2.imshow()`.
```
def rotate_image():
    global img_rotated
    angle = 45  # Change the angle as per your requirement
    rows, cols = img_original.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    img_rotated = cv2.warpAffine(img_original, M, (cols, rows))
    cv2.imshow("Rotated Image", img_rotated)
    cv2.waitKey(0)
```
2- Resize Function

This function defines what happens when the "Resize" button is clicked. It resizes the image by a fixed percentage (50%) using `cv2.resize()`, then displays the resized image using `cv2.imshow()`.
```
def resize_image():
    global img_resized
    scale_percent = 50  # Change the scale percentage as per your requirement
    width = int(img_original.shape[1] * scale_percent / 100)
    height = int(img_original.shape[0] * scale_percent / 100)
    dim = (width, height)
    img_resized = cv2.resize(img_original, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized Image", img_resized)
    cv2.waitKey(0)
```
3- Grayscale Function

This function defines what happens when the "Grayscale" button is clicked. It converts the image to grayscale using `cv2.cvtColor()` and displays the grayscale image using `cv2.imshow()`.
```
def grayscale_image():
    global img_grayscale
    img_grayscale = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", img_grayscale)
    cv2.waitKey(0)
```
4- Save Image

This function defines what happens when the "Save Image" button is clicked. It prompts the user to select a file name and location to save the resized image using `filedialog.asksaveasfilename()`, then saves the image using `cv2.imwrite()`.
```
def save_image():
    global img_path, img_resized
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    cv2.imwrite(save_path, img_resized)
    print("Image saved successfully!")
```
----
After that, Create the main window of the GUI using `tk.Tk()`, set its title to "Image Operations", and set its size to 300x200 pixels using `root.geometry()` as follows:
```
root = tk.Tk()
root.title("Image Operations")
root.geometry("300x200")
```
------
Now, you must Create the buttons for each operation in the GUI using `tk.Button()`, set their text labels and command functions, and pack them into the main window using `pack()` with some padding (`pady`) to adjust their positions as follows :

1-button for open image
```
btn_open = tk.Button(root, text="Open Image", command=open_image)
btn_open.pack(pady=10)
```
2- button for rotate function 
```
btn_rotate = tk.Button(root, text="Rotate", command=rotate_image)
btn_rotate.pack(pady=5)
```
3- button for resize function
```
btn_resize = tk.Button(root, text="Resize", command=resize_image)
btn_resize.pack(pady=5)
```
4- button for grayscale function
```
btn_grayscale = tk.Button(root, text="Grayscale", command=grayscale_image)
btn_grayscale.pack(pady=5)
```
5- button for save image function
```
btn_save = tk.Button(root, text="Save Image", command=save_image)
btn_save.pack(pady=10)
```
6- button for exit 
```
btn_exit = tk.Button(root, text="Exit", command=root.destroy)
btn_exit.pack(pady=5)
```
-----
Finally, We want to keeps the GUI window open until the user closes it or exits the program by starts the event loop of the GUI, which handles user input and updates the display as follows :
```
root.mainloop()
```
