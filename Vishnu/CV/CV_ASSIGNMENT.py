from PIL import Image as ijk
import cv2

i = input("enter file name in this folder")

image = cv2.imread(i,0)

blurred = cv2.GaussianBlur(src=image, ksize=(3, 5), sigmaX=0.5)
edges = cv2.Canny(blurred, 70, 135)
DOTS = [
    (0, 0), (0, 1), (0, 2), (1, 0), 
    (1, 1), (1, 2), (0, 3), (1, 3)
]

def image_to_braille(image_path, threshold=1):
    img = image_path.convert("L")
    new_width = 200
    new_height = 200
    img = img.resize((200, 200))
    
    pixels = img.load()
    print(type(pixels))
    braille_art = ""
    for y in range(0, new_height, 4):
        for x in range(0, new_width, 2):
            braille_char = 0x2800
            for i, (dx, dy) in enumerate(DOTS):
                px = x + dx
                py = y + dy
                if px < new_width and py < new_height:
                    if pixels[px, py] < threshold:
                        braille_char |= (1 << i)
            braille_art += chr(braille_char)
        braille_art += '\n'
    return braille_art


h = ijk.fromarray(edges)

f = open("result.txt","w")
f.write(image_to_braille(h))
f.close()
