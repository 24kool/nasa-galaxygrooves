import audio
import numpy as np
#import sounddevice as sd
import time
import cv2
import wave
import sys
import streamlit as st

def rgb (image):
    rgb_array = cv2.imread(image)
    height, width, rgb_value = rgb_array.shape
    square_size = 20
    b_vals = []
    g_vals = []
    r_vals = []
    for i in range(0, height, square_size):
        for j in range(0, width, square_size):
            block_height = min(square_size, height - i)
            block_width = min(square_size, width - j)
            block = rgb_array[i:i + block_height, j:j + block_width, :]
            b = np.mean(block[:, :, 0])
            g = np.mean(block[:, :, 1])
            r = np.mean(block[:, :, 2])
            b_vals.append(b)
            g_vals.append(g)
            r_vals.append(r)
    average_rgb = []
    for val in zip(r_vals, b_vals, g_vals):
        val = np.mean(val)
        #print(val)
        average_rgb.append(val)
    return (average_rgb)

if __name__ == "__main__":
    image = sys.argv[1]
    band1DecData = rgb(image)
    image = sys.argv[2]
    band2DecData = rgb(image)
    image = sys.argv[3]
    band4DecData = rgb(image)
    notes = []
    for i in range(200,len(band1DecData)-200, 50):
        notes.append(audio.Note(band2DecData[i], band1DecData[i], band4DecData[i]))
    sample_rate = audio.sample_rate
    for note in notes:
        # Generate time values
        t = np.linspace(0, note.duration, int(sample_rate * note.duration), endpoint=False)
        # Generate the sine wave signal
        x = note.volume * np.sin(2 * np.pi * note.frequency * t)
        # Play the sound
        st.audio(x, sample_rate=44100)
        # Wait until the sound is played completely
        #st.wait()
        # Pause between notes
        # time.sleep(0.1)
    # notes = [audio.Note(0.5, 440, 0.5), audio.Note(1, 880, 0.7), audio.Note(0.2, 1760, 0.3)]


# play()