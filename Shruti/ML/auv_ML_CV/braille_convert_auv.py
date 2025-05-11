import cv2
import numpy as np


# Braille dot bit positions
DOT_MAP = [
    [0x01, 0x08],  # Dots 1 and 4
    [0x02, 0x10],  # Dots 2 and 5
    [0x04, 0x20],  # Dots 3 and 6
    [0x40, 0x80]   # Dots 7 and 8
]

# Unicode Braille pattern base
BRAILLE_UNICODE_START = 0x2800

def image_to_braille(img_path, output_path="output.txt", invert=False):
    # Load and convert image to grayscale
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Image not found or path incorrect.")
        return

    # Resize image to a multiple of 2x4 for proper Braille block grouping
    height, width = img.shape
    new_width = width - (width % 2)
    new_height = height - (height % 4)
    img = cv2.resize(img, (new_width, new_height))

    # Threshold the image to black and white (binary)
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    if invert:
        binary = 255 - binary

    output_lines = []

    # Process in 4x2 pixel blocks
    for y in range(0, binary.shape[0], 4):
        line = ""
        for x in range(0, binary.shape[1], 2):
            braille_char = 0
            for dy in range(4):
                for dx in range(2):
                    pixel_y = y + dy
                    pixel_x = x + dx
                    if binary[pixel_y, pixel_x] == 0:  # Black pixel
                        braille_char |= DOT_MAP[dy][dx]
            line += chr(BRAILLE_UNICODE_START + braille_char)
        output_lines.append(line)

    # Write to output text file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print(f"Braille art saved to {output_path}")

# Example usage
image_to_braille("image.jpeg", "braille_art.txt", invert=True)
