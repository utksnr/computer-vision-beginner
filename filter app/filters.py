import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage

original = cv2.imread("your_image.jpg")
image = original.copy()

filters = {
    'grayscale': False,
    'bluescale': False,
    'redscale': False,
    'greenfilter': False,
    'invert': False
}

def apply_filters():
    img = original.copy()
    if filters['grayscale']:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    if filters['bluescale']:
        img[:, :, 1] = 0
        img[:, :, 2] = 0
    if filters['redscale']:
        img[:, :, 0] = 0
        img[:, :, 1] = 0
    if filters['greenfilter']:
        img[:, :, 0] = 0
        img[:, :, 2] = 0
    if filters['invert']:
        img = cv2.bitwise_not(img)
    return img

def update_image(label):
    img = apply_filters()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, ch = img_rgb.shape
    bytes_per_line = ch * w
    qimg = QImage(img_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
    label.setPixmap(QPixmap.fromImage(qimg))

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Photo Filter App")

label = QLabel()
update_image(label)

main_layout = QHBoxLayout()
button_layout = QVBoxLayout()

def make_button(name):
    btn = QPushButton(name.capitalize())
    btn.setCheckable(True)
    def toggle():
        filters[name] = not filters[name]
        update_image(label)
    btn.clicked.connect(toggle)
    button_layout.addWidget(btn)

for name in filters:
    make_button(name)

main_layout.addWidget(label)
main_layout.addLayout(button_layout)
window.setLayout(main_layout)

window.show()
sys.exit(app.exec_())
