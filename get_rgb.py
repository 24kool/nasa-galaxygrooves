import audio
import numpy as np
import sounddevice as sd
import time
import cv2
import wave

def rgb (image):
    rgb_array = cv2.imread(image)
    print(rgb_array.shape)
    height, width, _ = rgb_array.shape
    print(_)
    square_size = 20
    r_vals = []
    g_vals = []
    b_vals = []
    for i in range(0, height, square_size):
        for j in range(0, width, square_size):
            block_height = min(square_size, height - i)
            block_width = min(square_size, width - j)
            block = rgb_array[i:i + block_height, j:j + block_width]
            r = np.mean(block[:, :, 0])
            g = np.mean(block[:, :, 1])
            b = np.mean(block[:, :, 2])
            r_vals.append(r)
            g_vals.append(g)
            b_vals.append(b)
    average_rgb = []
    for val in zip(r_vals, b_vals, g_vals):
        val = np.mean(val)
        average_rgb.append(val)
    #print(average_rgb)
    return (average_rgb)

image = './static/M33/band1.png'
rgb(image)