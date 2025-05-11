import cv2
import numpy as np

def image_to_braille(image_path, output_txt_path, width=100, threshold=128):
    """
    Convert an image to Braille art.
    
    Args:
        image_path (str): Path to the input image file
        output_txt_path (str): Path to save the output text file
        width (int): Desired width of the Braille art in characters
        threshold (int): Brightness threshold for binarization (0-255)
    """
    
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Could not load image from path: " + image_path)
    
    # Calculate aspect ratio and resize
    height = int(width * (img.shape[0] / img.shape[1])) // 2  # Divide by 2 because Braille chars are 2x4 dots
    img = cv2.resize(img, (width, height * 2))
    
    # Binarize the image (convert to black and white)
    _, binary_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)
    
    # Braille Unicode starts at 0x2800
    braille_offset = 0x2800
    
    # Braille patterns are arranged in a 2x4 grid:
    # (1) (4)
    # (2) (5)
    # (3) (6)
    # (7) (8)
    # We'll use 2x4 blocks from the image to form each Braille character
    
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        for y in range(0, binary_img.shape[0], 4):
            for x in range(0, binary_img.shape[1], 2):
                # Get a 2x4 block of pixels
                block = binary_img[y:y+4, x:x+2]
                
                # Create Braille character by checking which dots should be raised
                braille_code = 0
                
                # Dot 1 (top-left)
                if block.shape[0] > 0 and block.shape[1] > 0 and block[0, 0] > 0:
                    braille_code += 1 << 0
                
                # Dot 2 (middle-left)
                if block.shape[0] > 1 and block.shape[1] > 0 and block[1, 0] > 0:
                    braille_code += 1 << 1
                
                # Dot 3 (bottom-left)
                if block.shape[0] > 2 and block.shape[1] > 0 and block[2, 0] > 0:
                    braille_code += 1 << 2
                
                # Dot 4 (top-right)
                if block.shape[0] > 0 and block.shape[1] > 1 and block[0, 1] > 0:
                    braille_code += 1 << 3
                
                # Dot 5 (middle-right)
                if block.shape[0] > 1 and block.shape[1] > 1 and block[1, 1] > 0:
                    braille_code += 1 << 4
                
                # Dot 6 (bottom-right)
                if block.shape[0] > 2 and block.shape[1] > 1 and block[2, 1] > 0:
                    braille_code += 1 << 5
                
                # Dot 7 (very bottom-left - only if we have 4 rows)
                if block.shape[0] > 3 and block.shape[1] > 0 and block[3, 0] > 0:
                    braille_code += 1 << 6
                
                # Dot 8 (very bottom-right - only if we have 4 rows)
                if block.shape[0] > 3 and block.shape[1] > 1 and block[3, 1] > 0:
                    braille_code += 1 << 7
                
                # Convert to Braille character
                braille_char = chr(braille_offset + braille_code)
                f.write(braille_char)
            
            f.write('\n')

if __name__ == "__main__":
    input_image = input("Enter the path to the input image (jpg): ").strip()
    output_file = input("Enter the path for the output text file: ").strip()
    
    try:
        width = int(input("Enter desired width in characters (default 100): ") or 100)
        threshold = int(input("Enter brightness threshold (0-255, default 128): ") or 128)
    except ValueError:
        print("Invalid input, using defaults")
        width = 100
        threshold = 128
    
    image_to_braille(input_image, output_file, width, threshold)
    print(f"Braille art saved to {output_file}")