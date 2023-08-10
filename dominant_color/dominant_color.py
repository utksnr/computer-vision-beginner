import numpy as np
import cv2

def create_bar(ht, w, color):
    bar = np.zeros((h, w, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)

img = cv2.imread("image_path")
h,w,_ = np.shape(img)

data = np.reshape(img,(h*w,3))
data = np.float32(data)

cluster_number = 3
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness , labels ,centers = cv2.kmeans(data,cluster_number,None,criteria,10,flags)

font = cv2.FONT_HERSHEY_COMPLEX
bar_list = []
rgb_vals = []

for index , row in enumerate(centers):
    bar , rgb = create_bar(200,200,row)
    bar_list.append(bar)
    rgb_vals.append(rgb)

img_bar = np.hstack(bar_list)

for index, row in enumerate(rgb_vals):
    image = cv2.putText(img_bar, f'{index + 1}. RGB: {row}', (5 + 200 * index, 200 - 10),
                        font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    print(f'{index + 1}. RGB{row}')

cv2.imshow('Image', img)
cv2.imshow('Dominant colors', img_bar)

cv2.waitKey(0)