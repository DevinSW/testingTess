import pytesseract
from pytesseract import Output
import PIL.Image
import cv2

myconfig = r"--psm 3 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("2022-08-08 Maryland Michigan 1 cropped.JPG"), config=myconfig)
print(text)

img = cv2.imread("2022-08-08 Maryland Michigan 1 cropped.JPG")
height, width, _ = img.shape

data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

amount_boxes = len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i]) > 10:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x,y), (x+width, y + height), (0,255,0), 2)
        # img = cv2.putText(img, data['text'][i], (x, y+height+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey(0)