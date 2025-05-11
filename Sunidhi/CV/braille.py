import cv2  # For image processing
import numpy as np

# Step 1: Load and preprocess image
def load_image(image_path, scale_percent=100):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("Image not found or path is incorrect.")
    
    # Resize for better terminal fitting
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    
    return resized

# Step 2: Map for Braille dots (Unicode encoding)
# Each Braille char represents 2x4 pixels
# Dot positions follow this pattern:
# 1 4
# 2 5
# 3 6
# 7 8
braille_dot_map = [
    (0, 0, 0b00000001),  # dot 1
    (1, 0, 0b00000010),  # dot 2
    (2, 0, 0b00000100),  # dot 3
    (0, 1, 0b00001000),  # dot 4
    (1, 1, 0b00010000),  # dot 5
    (2, 1, 0b00100000),  # dot 6
    (3, 0, 0b01000000),  # dot 7
    (3, 1, 0b10000000),  # dot 8
]

def image_to_braille(img, threshold=98):
    rows, cols = img.shape
    output_lines = []

    # Go in 4-row, 2-col steps
    for y in range(0, rows - 3, 4):
        line = ""
        for x in range(0, cols - 1, 2):
            braille_char = 0
            for dy, dx, mask in braille_dot_map:
                pixel_y = y + dy
                pixel_x = x + dx
                if img[pixel_y, pixel_x] < threshold:
                    braille_char |= mask  # Turn on this dot
            unicode_char = chr(0x2800 + braille_char)
            line += unicode_char
        output_lines.append(line)
    
    return output_lines

def save_to_file(lines, output_path="braille_art.txt"):
    with open(output_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"Braille art saved to {output_path}")

# Main function to run
def convert_image_to_braille(image_path, scale=100, threshold=98):
    img = load_image(image_path, scale)
    lines = image_to_braille(img, threshold)
    save_to_file(lines)

# Example usage
if __name__ == "__main__":
    # Modify scale and threshold for better results
    convert_image_to_braille("pic.jpg", scale=100, threshold=98)