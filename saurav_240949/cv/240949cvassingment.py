import cv2
import numpy as np

def image_to_braille(image_path, output_txt="output.txt", threshold=127):
    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Image not found or path is incorrect")
        return

    # Resize to fit Braille grid (width multiple of 2, height multiple of 4)
    h, w = img.shape
    h -= h % 4
    w -= w % 2
    img = cv2.resize(img, (w, h))

    # Normalize and binarize
    _, binary = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)

    # Dot positions in Braille Unicode character
    dot_offsets = [
        (0, 0),  # dot 1
        (1, 0),  # dot 2
        (2, 0),  # dot 3
        (0, 1),  # dot 4
        (1, 1),  # dot 5
        (2, 1),  # dot 6
        (3, 0),  # dot 7
        (3, 1),  # dot 8
    ]

    output_lines = []

    for y in range(0, h, 4):
        line = ''
        for x in range(0, w, 2):
            dots = 0
            for i, (dy, dx) in enumerate(dot_offsets):
                px = binary[y + dy, x + dx]
                if px > 0:
                    dots |= 1 << i
            braille_char = chr(0x2800 + dots)
            line += braille_char
        output_lines.append(line)

    # Write to file
    with open(output_txt, 'w', encoding='utf-8') as f:
        for line in output_lines:
            f.write(line + '\n')

    print(f"Braille output saved to '{output_txt}'")

# Example usage
image_to_braille("input.jpg")
