import PIL.Image
import numpy as np
import pandas as pd
import cv2
import PIL
import pytesseract
import spacy

# img_cv = cv2.imread('/Users/suveern/learnings/Udemy/NER-OCR/Selected/001.jpeg')
# cv2.imshow('Business Card', img_cv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
img_pl = PIL.Image.open('/Users/mitulgarg/Desktop/image3.jpeg')
# img_pl.show()
# text_cv = pytesseract.image_to_boxes(img_cv)
data = pytesseract.image_to_data(img_pl)
d = list(map(lambda x: x.split('\t'), data.split('\n')))
print()
print()
print(data)
# print(d)