import cv2

image = cv2.imread("image-path")
cv2.imshow("Original Image",image)

grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey)

blur = cv2.GaussianBlur(invert,(21,21),0)
invertblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey,invertblur,sclae=256.0)

cv2.imwrite("download path",sketch)

image2 =cv2.imread("sketch img path")

cv2.imshow("Sketch Image",image2)

cv2.waitKey(0)
cv2.destroyAllWindows()