import cv2
import imutils
from skimage.filters import threshold_local
from transform import perspective_transform

orgimg = cv2.imread("image path")
copy = orgimg.copy()

ratio = orgimg.shape[0] / 500.0
resizeimg = imutils.resize(orgimg, height=500)

gray = cv2.cvtColor(resizeimg, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

cnts, _ = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]


for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    if len(approx) == 4:
        doc = approx
        break

p = []
for d in doc:
    tuple_point = tuple(d[0])
    cv2.circle(resizeimg, tuple_point, 3, (0, 0, 255), 4)
    p.append(tuple_point)

warped_image = perspective_transform(copy, doc.reshape(4, 2) * ratio)
warped_image = cv2.cvtColor(warped_image, cv2.COLOR_BGR2GRAY)


T = threshold_local(warped_image, 11, offset=10, method="gaussian")
warped = (warped_image > T).astype("uint8") * 255
cv2.imwrite('./'+'scan'+'.png',warped)

cv2.imshow("Scanned", imutils.resize(warped, height=650))
cv2.waitKey(0)
cv2.destroyAllWindows()





