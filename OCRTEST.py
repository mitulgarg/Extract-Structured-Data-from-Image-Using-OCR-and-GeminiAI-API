import pytesseract
from PIL import Image

img = Image.open('/Users/mitulgarg/Desktop/image3.jpeg')

# Perform OCR
extracted_text = pytesseract.image_to_string(img)

# Print the extracted text
print(extracted_text)