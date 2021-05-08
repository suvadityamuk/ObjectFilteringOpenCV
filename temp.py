import cv2
import os
import numpy

f = open('positive.txt', 'a+')
def mark_img(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        car = img[y: y + height, x: x + width]
        
        

while True:
    cv2.imshow("my_img", img)
    key = cv2.waitKey(1)
    if key == 27:
        break

def create_pos_and_neg():
    for file_type in ['negative', 'positive']:
        for img in os.listdir(file_type):
            if file_type == 'negative':
                line = file_type + '/' + img + '\n'
                f = open(bg.txt, 'a')
                f.write(line)
            elif file_type == 'positive':