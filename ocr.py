import pytesseract
from PIL import Image

# Load the image from file
image_path = 'OCR/resources/img.png'
img = Image.open(image_path)

# Use tesseract to do OCR on the image
text = pytesseract.image_to_string(img)

print(text)