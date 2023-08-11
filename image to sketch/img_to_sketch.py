import cv2

img = cv2.imread("img_path")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray = 255 - gray
blurred = cv2.GaussianBlur(inverted_gray, (77, 77), 0)
inverted_blurred = 255 - blurred
sketch = cv2.divide(gray, inverted_blurred, scale=256.0)

cv2.imshow("Image", img)
cv2.imshow("Sketch", sketch)

cv2.waitKey(0)

cv2.imwrite("save_name", sketch)