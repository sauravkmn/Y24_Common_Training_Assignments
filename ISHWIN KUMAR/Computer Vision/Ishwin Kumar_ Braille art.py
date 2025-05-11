import cv2
import numpy as np

# Braille dot positions (index -> bit position)
DOTS = [
    (0, 0),  (1, 0), (2, 0), (0, 1), (1, 1),(2, 1),  (3, 0),  (3, 1),  
]

def pixel_to_braille(block, threshold=127):
    """Convert 2x4 pixel block to a Braille character."""
    value = 0
    for idx, (r, c) in enumerate(DOTS):
        if r < block.shape[0] and c < block.shape[1]:
            if block[r, c] < threshold:  # darker pixel -> raised dot
                value |= (1 << idx)
    return chr(0x2800 + value)

def image_to_braille(image_path, scale):
    # Load image and convert to grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    img = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    11, 2
    )


    # Resize for smaller output
    height, width = img.shape
    new_width = int(width * scale)
    new_height = int(height * scale)
    img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
    # Ensure dimensions are multiples of 4 (height) and 2 (width)
    h_trim = img.shape[0] - (img.shape[0] % 4)
    w_trim = img.shape[1] - (img.shape[1] % 2)
    img = img[:h_trim, :w_trim]

    braille_rows = []
    for y in range(0, img.shape[0], 4):
        row = ''
        for x in range(0, img.shape[1], 2):
            block = img[y:y+4, x:x+2]
            braille_char = pixel_to_braille(block)
            row += braille_char
        braille_rows.append(row)

    return "\n".join(braille_rows)

    

if __name__ == "__main__":
    input_path = r"C:\Users\IK\Desktop\sample.jpg"
    output_path = r"C:\Users\IK\Desktop\output_braille_art.txt"
    braille_art = image_to_braille(input_path, 0.18)
    print(braille_art)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(braille_art)
    print(f" Braille art saved to: {output_path}")

