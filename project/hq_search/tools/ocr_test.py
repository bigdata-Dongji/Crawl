# encoding:utf8
'''
Creation time: 2020/12/6 21:10 
Update time:
Purpose:
'''
import cv2
import pytesseract
from PIL import Image

img = cv2.imread("zhihu_image/a.png")
text = pytesseract.image_to_string(Image.open("zhihu_image/a.png"))
print(text)
cv2.imshow("result", img)
cv2.waitKey(0)