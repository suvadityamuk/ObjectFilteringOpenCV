import urllib.request
import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

directory = 'negative'
c = int(1)
for filename in os.listdir(directory):
    try:
        img = cv2.imread(f'negative/{filename}', cv2.IMREAD_GRAYSCALE)
        resized_img = cv2.resize(img, (200,200))
        print(img.shape)
        print(resized_img.shape)
        cv2.imwrite(f'negative/resized/{filename}', resized_img)
    except Exception as e:
        print(str(e))