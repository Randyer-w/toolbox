import cv2
import tkinter as tk
from PIL import Image, ImageDraw
from tkinter import filedialog
import numpy as np

from removebg import RemoveBg


def gaussianblur(img, mask_2):#mask_2为灰度; mask mask_3为RGB mask; processed为高斯模糊后的原图
    processed = img
    for i in range(1,5):
        processed = cv2.GaussianBlur(processed, (5, 5), 0)
    mask_3 = cv2.cvtColor(mask_2, cv2.COLOR_GRAY2RGB)
    Rol_imagea_1 = cv2.bitwise_and(mask_3, img)
    Rol_imagea_2 = cv2.bitwise_and(~mask_3, processed)

    Rol_imageb_1 = cv2.bitwise_and(~mask_3, img)
    Rol_imageb_2 = cv2.bitwise_and(mask_3, processed)

    cv2.imshow('Image A', cv2.bitwise_or(Rol_imagea_1, Rol_imagea_2))
    cv2.imshow('Image B', cv2.bitwise_or(Rol_imageb_1, Rol_imageb_2))
    cv2.imwrite('../Image_A.png', cv2.bitwise_or(Rol_imagea_1, Rol_imagea_2))
    cv2.imwrite('../Image_B.png', cv2.bitwise_or(Rol_imageb_1, Rol_imageb_2))


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    Fpath = filedialog.askopenfilenames()
    path = Fpath[0]
    # rmbg = RemoveBg("vkQcyPZkFWiJDvN7iazbnpaF", "error.log")  # 引号内是你获取的API
    # rmbg.remove_background_from_img_file(path)  # 图片地址 得到抠图的图像
    path_nobg = path + '_no_bg.png'
    img = cv2.imread(path)
    img_nobg = cv2.imread(path_nobg)
    img_nobg = cv2.resize(img_nobg, (img.shape[0], img.shape[1]))
    cv2.imwrite(path_nobg, img_nobg)
    img_nobg = cv2.imread(path_nobg)
    ##########################将黑色像素转换为白色
    black_pixels = np.where(
        (img_nobg[:, :, 0] == 0) &
        (img_nobg[:, :, 1] == 0) &
        (img_nobg[:, :, 2] == 0)
    )
    img_nobg[black_pixels] = [255, 255, 255]
    ####################转换完成进行阈值处理
    gray = cv2.cvtColor(img_nobg, cv2.COLOR_BGR2GRAY)
    retval, mask1 = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY)###############生成第一个Mask
    ##########################生成第二个Mask
    mask2 = ~mask1
    ##########################保存两张Mask图
    cv2.imwrite('../MaskA.jpg', mask1)
    cv2.imwrite('../MaskB.jpg', mask2)
    ##########################利用Mask生成高斯模糊图像



    imageA = gaussianblur(img, mask1)

    imageB = gaussianblur(img, mask2)

    cv2.imshow("Mask A" ,mask1)
    cv2.imshow("Mask B", mask2)

    ########生成MASK成功
    cv2.waitKey(0)




