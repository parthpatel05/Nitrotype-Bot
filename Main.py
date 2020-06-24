# This just gives u a slight boost
import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time
import cv2
from pynput.keyboard import Key, Controller
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'F:\Users\parth\AppData\Local\Tesseract-OCR\tesseract.exe'

keyboard = Controller()

# checks if the game started
def check_start(data):
    for i in range(950, 1025):
        for j in range(750, 775):
            if data[i, j] > 250:
                return True


def hit(key):
    pyautogui.keyDown(key)
    return


def split(word):
    return [char for char in word]


def split_hit(string):
    splited = split(string)
    for char in splited:
        hit(char)
        print(char)
        time.sleep(.75)


# takes ss till you get go
go = True
while go:
    image = ImageGrab.grab().convert('L')
    # image = Image.open('ss.png').convert('L')
    data = image.load()
    if check_start(data):
        go = False

# takes a ss of just the text box
# u will need to find the coordinates of the text box
img = ImageGrab.grab(bbox=(535, 820, 1180, 960))
img = img.save('Saved.png')

# opens img and converts for CV
img = cv2.imread('Saved.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# to find coordinates of the first letter box
hImg, wImg, _ = img.shape
boxes = tess.image_to_boxes(img)

first = boxes.splitlines()
st = first[0].split()

x, y, w, h = int(st[1]), int(st[2]), int(st[3]), int(st[4])

# j  (x,w)
# I (h2, y2)
# print(x)
# print(y)
# print(w)
# print(h)
y2 = hImg - y
h2 = hImg - h
# print(y2)
# print(h2)

# turns the first letter and box white
for i in range(h2, y2):
    for j in range(x, w):
        img[i, j] = [232, 232, 233]

text = tess.image_to_string(img)
print(text)
time.sleep(3)
# split_hit(text)
keyboard.type(text)

# show the img
#cv2.imshow('img', img)
#cv2.waitKey(0)