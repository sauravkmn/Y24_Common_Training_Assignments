import cv2
import numpy as np

# Mapping from dot positions to binary weights (Braille encoding)
DOT_MAP = {
    (0, 0): 0b00000001,  # Dot 1
    (1, 0): 0b00000010,  # Dot 2
    (2, 0): 0b00000100,  # Dot 3
    (0, 1): 0b00001000,  # Dot 4
    (1, 1): 0b00010000,  # Dot 5
    (2, 1): 0b00100000,  # Dot 6
    (3, 0): 0b01000000,  # Dot 7
    (3, 1): 0b10000000,  # Dot 8
}

def image_to_braille(image_path, output_txt='output.txt', cell_height=4, cell_width=2):
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize to a size divisible by 4x2 for Braille cells
    h, w = img.shape
    new_h = (h // cell_height) * cell_height
    new_w = (w // cell_width) * cell_width
    img = cv2.resize(img, (new_w, new_h))

    # Binarize image using adaptive threshold
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    # Normalize to 0 and 1
    binary = binary // 255

    output_lines = []
    for i in range(0, new_h, cell_height):
        line = ""
        for j in range(0, new_w, cell_width):
            dots = 0
            for y in range(cell_height):
                for x in range(cell_width):
                    if binary[i + y, j + x]:
                        dots |= DOT_MAP.get((y, x), 0)
            braille_char = chr(0x2800 + dots)
            line += braille_char
        output_lines.append(line)

    # Save to txt file
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    print(f"Braille art written to {output_txt}")

# Example usage
image_to_braille('images.jpeg', 'braille_output.txt')


