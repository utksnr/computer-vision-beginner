import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRubberBand, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QRect, QPoint, QSize
from PyQt5.QtGui import QGuiApplication

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Simple Screenshot Tool")
window.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
window.showFullScreen()
window.setWindowOpacity(0.3)

layout = QVBoxLayout()
label = QLabel("Drag to select area, then release mouse to capture")
layout.addWidget(label)
window.setLayout(layout)

rubberBand = QRubberBand(QRubberBand.Rectangle, window)
origin = QPoint()
selection = QRect()

def mouse_press(event):
    global origin
    origin = event.pos()
    rubberBand.setGeometry(QRect(origin, QSize()))
    rubberBand.show()

def mouse_move(event):
    rubberBand.setGeometry(QRect(origin, event.pos()).normalized())

def mouse_release(event):
    global selection
    selection = rubberBand.geometry()
    rubberBand.hide()
    take_screenshot()
    window.close()

def take_screenshot():
    screen = QGuiApplication.primaryScreen()
    if screen:
        pixmap = screen.grabWindow(0)
        cropped = pixmap.copy(selection)
        file_path = "screenshot.png"
        cropped.save(file_path, "png")
        print(f"Screenshot saved to {file_path}")

window.mousePressEvent = mouse_press
window.mouseMoveEvent = mouse_move
window.mouseReleaseEvent = mouse_release

sys.exit(app.exec_())
