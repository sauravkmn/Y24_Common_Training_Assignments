import cv2 as cv
import numpy as np
import sys

def binary_to_braille(arr):
    dots = [(0,0,0), (1,0,1), (2,0,2), (0,1,3), (1,1,4), (2,1,5), (3,0,6), (3,1,7)]
    h, w = arr.shape
    pad_h = (4 - h % 4) % 4
    pad_w = (2 - w % 2) % 2

    arr = np.pad(arr, ((0, pad_h), (0, pad_w)), constant_values=0)

    output = ""
    for y in range(0, arr.shape[0], 4):
        line = ""
        for x in range(0, arr.shape[1], 2):
            block = arr[y:y+4, x:x+2]
            bits = 0
            for i, j, bit in dots:
                if block[i, j]:
                    bits |= (1 << bit)
            line += chr(0x2800 + bits)
        output += line + "\n"
    return output

img = cv.imread('nggyu.jpg', cv.IMREAD_GRAYSCALE)
edges = cv.Canny(img,100,200)
if img is None:
    sys.exit("Could not read the image.")

cv.imshow("image", img)


blur = cv.GaussianBlur(img,(5,5),0)
ret,bw = cv.threshold(blur,0,255,cv.THRESH_BINARY_INV +cv.THRESH_OTSU)

combined = cv.bitwise_or(bw, edges)

cv.imshow("image", bw)
cv.imshow("combined", combined)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("edited.png", img)

braille_art = binary_to_braille(combined)
with open("braille_art.txt", "w", encoding="utf-8") as f:
    f.write(braille_art)
print("Braille art saved to braille_art.txt") 