#*********************************************************
#-----------------------IMPORTS---------------------------
#*********************************************************
import numpy as np
from cv2 import *
import cv2
import time as t
from matplotlib import pyplot as plt
from PIL import Image
import statistics
#*********************************************************
#*********************************************************
#---------------------cameraman.png ----------------------
imgL = cv2.imread('stereo-pairs/venus/imL.png')
imgR = cv2.imread('stereo-pairs/venus/imR.png')
b1, g1, r1 = cv2.split(imgL)
b2, g2, r2 = cv2.split(imgR)

newImg = cv2.merge((b1, g1, r2))

cv2.imwrite("3D.png", newImg)
cv2.imshow("3D.png", newImg)
#---------------------------------------------------------
#-------------------------PART 2--------------------------
#---------------------------------------------------------
imgL = cv2.imread('stereo-pairs/venus/imL.png', 0)
imgR = cv2.imread('stereo-pairs/venus/imR.png', 0)


# def disparitySAD(imgL, imgR, Dx, Dy, windowRows, windowColumns):
#     for i in range(len(imgL)):
#         for j in range(len(imgL[i])):
#             for k in range(Dx):
#                 for l in range(Dy):

def disparitySAD(left_img, right_img, kernel, max_offset):
    left_img = Image.open(left_img).convert('L')
    left = np.asarray(left_img)
    right_img = Image.open(right_img).convert('L')
    right = np.asarray(right_img)
    w, h = left_img.size
    depthImg = np.zeros((w, h), np.uint8)
    depthImg.shape = h, w

    for y in range((int(kernel / 2)), h - (int(kernel / 2))):
        for x in range((int(kernel / 2)), w - (int(kernel / 2))):
            prv = 88888
            best_offset = 0

            for offset in range(max_offset):
                SAD = 0
                for v in range(-(int(kernel / 2)), (int(kernel / 2))):
                    for u in range(-(int(kernel / 2)), (int(kernel / 2))):
                        SAD += abs(int(left[y + v, x + u]) -
                                   int(right[y + v, (x + u) - offset]))

                if SAD < prv:
                    prv = SAD

            depthImg[y, x] = SAD

    cv2.imwrite("depthImg.png", depthImg)
    cv2.imshow("depthImg.png", depthImg)



disparitySAD("stereo-pairs/view0.png", "stereo-pairs/view1.png", 6, 30)


#------------Handling img showing and closing-------------
#---------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------