import numpy as np
from PIL import Image

def my_convolve(img_arr, kernel):
    kh, kw = kernel.shape
    ih, iw = img_arr.shape
    pad_h = kh // 2
    pad_w = kw // 2
    padded = np.pad(img_arr, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
    out = np.zeros_like(img_arr, dtype=float)
    for y in range(ih):
        for x in range(iw):
            region = padded[y:y+kh, x:x+kw]
            out[y, x] = np.sum(region * kernel)
    return out

def sobel_edges(img_arr):
    kx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    ky = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    gx = my_convolve(img_arr, kx)
    gy = my_convolve(img_arr, ky)
    mag = np.sqrt(gx**2 + gy**2)
    mag = np.clip(mag, 0, 255)
    return mag.astype(np.uint8)

def change_brightness(img_arr, factor=1.0):
    arr = img_arr * factor
    arr = np.clip(arr, 0, 255)
    return arr.astype(np.uint8)

def lbp(img_arr):
    radius = 1
    padded = np.pad(img_arr, radius, 'constant')
    out = np.zeros_like(img_arr, dtype=np.uint8)
    offsets = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for i in range(radius, padded.shape[0]-radius):
        for j in range(radius, padded.shape[1]-radius):
            center = padded[i, j]
            bits = 0
            for k, (dy, dx) in enumerate(offsets):
                bits |= (padded[i+dy, j+dx] >= center) << k
            out[i-radius, j-radius] = bits
    return out

def resize_nn(img_arr, new_w, new_h):
    old_h, old_w = img_arr.shape
    result = np.zeros((new_h, new_w), dtype=img_arr.dtype)
    for y in range(new_h):
        for x in range(new_w):
            src_x = int(x * old_w / new_w)
            src_y = int(y * old_h / new_h)
            result[y, x] = img_arr[src_y, src_x]
    return result

def img_to_braille(input_file, output_file, width=100, edge_w=0.7, tex_w=0.3, bright=1.2):
    img = Image.open(input_file).convert('L')
    arr = np.array(img)
    arr = change_brightness(arr, bright)
    edges = sobel_edges(arr)
    texture = lbp(arr)
    combined = arr.astype(float) * (1 - edge_w - tex_w) + edges.astype(float) * edge_w + texture.astype(float) * tex_w
    combined = np.clip(combined, 0, 255).astype(np.uint8)
    aspect = combined.shape[0] / combined.shape[1]
    new_h = int(width * aspect)
    resized = resize_nn(combined, width*2, new_h*4)
    chars = []
    for y in range(0, resized.shape[0], 4):
        row = []
        for x in range(0, resized.shape[1], 2):
            block = resized[y:y+4, x:x+2]
            if block.shape != (4,2):
                block = np.ones((4,2), dtype=np.uint8) * 255
            dots = 0
            for i in range(4):
                for j in range(2):
                    if block[i,j] < 80:
                        dots |= 1 << (i + j*4)
            row.append(chr(0x2800 + dots))
        chars.append(''.join(row))
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(chars))

img_to_braille('tester.jpg', 'output.txt', width=100, edge_w=0.3, tex_w=0.15)
