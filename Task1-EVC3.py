import tkinter as tk
from tkinter import filedialog
import cv2

def open_image():
    global img_path, img_original, img_display
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    img_original = cv2.imread(img_path)
    scale_percent = 25  # Change the scale percentage as per your requirement
    width = int(img_original.shape[1] * scale_percent / 100)
    height = int(img_original.shape[0] * scale_percent / 100)
    dim = (width, height)
    img_display = cv2.resize(img_original, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Original Image", img_display)
    cv2.waitKey(0)

def rotate_image():
    global img_rotated, img_display
    angle = 45  # Change the angle as per your requirement
    rows, cols = img_original.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    img_rotated = cv2.warpAffine(img_original, M, (cols, rows))
    img_rotated_display = cv2.resize(img_rotated, (img_display.shape[1], img_display.shape[0]), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Rotated Image", img_rotated_display)

def resize_image():
    global img_resized
    scale_percent = 50  # Change the scale percentage as per your requirement
    width = int(img_original.shape[1] * scale_percent / 100)
    height = int(img_original.shape[0] * scale_percent / 100)
    dim = (width, height)
    img_resized = cv2.resize(img_original, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized Image", img_resized)

def grayscale_image():
    global img_grayscale, img_display
    img_grayscale = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    scale_percent = 25  # Change the scale percentage as per your requirement
    width = int(img_grayscale.shape[1] * scale_percent / 100)
    height = int(img_grayscale.shape[0] * scale_percent / 100)
    dim = (width, height)
    img_display = cv2.resize(img_grayscale, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Grayscale Image", img_display)

def save_image():
    global img_path, img_resized
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    cv2.imwrite(save_path, img_resized)
    print("Image saved successfully!")

root = tk.Tk()
root.title("Image Operations")
root.geometry("300x200")

btn_open = tk.Button(root, text="Open Image", command=open_image)
btn_open.pack(pady=10)

btn_rotate = tk.Button(root, text="Rotate", command=rotate_image)
btn_rotate.pack(pady=5)

btn_resize = tk.Button(root, text="Resize", command=resize_image)
btn_resize.pack(pady=5)

btn_grayscale = tk.Button(root, text="Grayscale", command=grayscale_image)
btn_grayscale.pack(pady=5)

btn_save = tk.Button(root, text="Save Image", command=save_image)
btn_save.pack(pady=10)

root.mainloop()

