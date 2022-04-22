import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog


if __name__ == '__main__':
    raw_img = cv2.imread('./lytro-03-A.jpg')  # A
    gray = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print(retval)
    cv2.imshow('mask', dst)
    cv2.waitKey()