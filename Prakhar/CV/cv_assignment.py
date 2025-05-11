import cv2

def convert_to_braille(packet):
    braille_base = 0x2800
    dot_value = 0
    for i, bit in enumerate(packet):
        if bit:
            dot_value += 2 ** i
    return chr(braille_base + dot_value)

img = cv2.imread('image2.jpg')
if img is None:
    raise FileNotFoundError("Image not found!")

# Resize to be divisible by 3 (rows) and 2 (cols)
img_y, img_x = img.shape[:2]
img = cv2.resize(img, (img_x - img_x % 2, img_y - img_y % 3))

# Convert to HSV once
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

with open('braille_img.txt', 'w', encoding='utf-8') as file:
    for i in range(img.shape[0] // 3):
        for j in range(img.shape[1] // 2):
            packet = [0] * 6
            for ii in range(3):
                for jj in range(2):
                    y = i * 3 + ii
                    x = j * 2 + jj
                    h, s, v = hsv_img[y, x]
                    idx = ii * 2 + jj  # map to dot 1-6

                    # Adjusted HSV thresholds to detect more pixels
                    if 0 < h < 20 and s > 50 and v > 50:
                        packet[idx] = 0
                    else:
                        packet[idx] = 1

            file.write(convert_to_braille(packet))
        file.write('\n')
