import cv2 as cv
img=cv.imread('pikachu.jpeg')
print(img.shape)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

_, binary=cv.threshold(gray,128,255,cv.THRESH_BINARY)
cv.imshow("Binary",binary)

h,w= binary.shape
braille_size=(h//3,w//2)
resize = cv.resize(binary, braille_size, interpolation=cv.INTER_AREA)

braille_map = {
    (0,0,0,0,0,0): " ",
    (1,0,0,0,0,0): "⠁", (1,1,0,0,0,0): "⠃", (1,0,1,0,0,0): "⠉", (1,1,1,0,0,0): "⠋",
    (1,1,0,1,0,0): "⠛", (0,1,0,1,0,1): "⠣", (1,1,1,1,1,1): "⣿"
}
braille_text = ""
for y in range(0, resize.shape[0]-2, 3):
    for x in range(0, resize.shape[1]-1, 2):
        cell = (resize[y:y+3, x:x+2] > 128).astype(int).flatten()
        braille_text += braille_map.get(tuple(cell), " ")
    braille_text += "\n"

# Save Braille output with correct encoding
with open("braille_art.txt", "w", encoding="utf-8") as f:
    f.write(braille_text)

print("Braille art saved in braille_art.txt!")

cv.waitKey(0)


