import cv2
import tkinter as tk
from PIL import Image, ImageDraw
from tkinter import filedialog
import numpy as np


root = tk.Tk()
root.withdraw()
Fpath = filedialog.askopenfilenames()





def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append(x)
        b.append(y)
        cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)


def cut_image(image_dir, x ,y ,w ,h):
    im = Image.open(image_dir)

    region = im.crop((x, y, x + w, y + h))
    region.save(image_dir[:-4] + '_cut.' + image_dir[-3:])

    a = ImageDraw.ImageDraw(im)
    a.rectangle(((x, y), (x + w, y + h)), fill=None, outline="red", width=2)
    im.save(image_dir[:-4] + '_new.' + image_dir[-3:])

if __name__ == '__main__':
    # 图片路径
    img = cv2.imread(Fpath[0])
    a = []
    b = []
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cut_x = abs(a[1] - a[0])
    cut_y = abs(b[1] - b[0])
    cut = cut_x if cut_x > cut_y else cut_y
    print(cut_x, cut_y, cut)
    for i in Fpath:
        cut_image(i, a[0], b[0], cut, cut)



