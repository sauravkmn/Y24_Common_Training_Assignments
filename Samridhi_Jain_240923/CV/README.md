# 🎨 Braille Art Generator using OpenCV (Google Colab Ready)

Turn any .jpg image into cool-looking *Braille Art* using Python and OpenCV — no AI, no APIs, just raw pixel-level manipulation.

This project is a fun way to explore how images can be represented in text, and it uses the Unicode Braille character set to generate visuals that can be viewed in any text editor or right inside your Google Colab notebook.

---

## ✨ What This Project Does

- You upload a .jpg image (like a logo, sketch, or photo)
- The script converts it into *Braille characters*, each representing a 2x4 grid of pixels
- The result:
  - Is displayed inside your notebook so you can see it immediately
  - Is saved into a braille_output.txt file so you can keep or share it

This is great for:
- Learning how image processing works
- Converting images into terminal art
- Accessibility-inspired projects
- Just having fun with code and Unicode

---

## 🔧 How It Works

- Every *Braille Unicode character* can represent a 2x4 grid of pixels.
- The image is:
  - Converted to grayscale
  - Resized to match a specific width in Braille characters
  - Thresholded to make it black & white
- The script loops through 2x4 pixel blocks and decides which dots are “on” or “off”
- It then builds the Braille character using the correct bit pattern and adds it to the output

It’s all done using basic image processing in OpenCV — no machine learning, no dependencies other than NumPy and OpenCV.

---

## ✅ Features

- 👁️ Adaptive thresholding for better contrast handling
- 🧱 Pixel-based block detection (2x4 blocks → 1 Braille char)
- 💾 Saves output as a downloadable .txt file
- 🖥️ Shows Braille Art inline in Google Colab using Markdown
- 🔧 Customizable output width for more or less detail

---

## 📦 Requirements

This is made to work best in *Google Colab*, but you can also run it locally with:

```bash
pip install opencv-python numpy