
import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import filedialog

def zh_ch(string):
	return string.encode("gbk").decode(errors="ignore")

def get_different_image(ori_image, syn_image, thr):
    syn_h, syn_w, _ = syn_image.shape # (338, 600, 3)

    ori_re = cv.resize(ori_image, (syn_w, syn_h),interpolation=cv.INTER_LINEAR)
    sub_img = ori_re.astype(np.int16)-syn_image.astype(np.int16)
    sub_img = np.abs(sub_img).astype(np.uint8)
    gray_sub_img = cv.cvtColor(sub_img, cv.COLOR_BGR2GRAY)
    mask = (gray_sub_img<thr).astype(np.uint8)*255
    return mask

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    Fpath = filedialog.askopenfilenames()
    raw_img = cv.imread(Fpath[0])#A
    syn_image = cv.imread(Fpath[1])#B
    mask = get_different_image(raw_img, syn_image, 1)
    print(type(mask))
    # 保存mask到txt文件夹
    cv.imwrite('diff.' + Fpath[0][-3:], mask)
    cv.imshow('chafentu', mask)
    cv.waitKey()

