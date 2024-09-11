import pygame
import PIL
import cv2
import moviepy
import pydub
import tkinter as tk
import sys

def safe_print(text):
    try:
        print(text)
    except UnicodeEncodeError:
        sys.stdout.buffer.write(text.encode('utf-8') + b'\n')

def check_installation():
    safe_print("✅ Pygame version: " + pygame.__version__)
    safe_print("✅ Pillow version: " + PIL.__version__)
    safe_print("✅ OpenCV version: " + cv2.__version__)
    safe_print("✅ MoviePy version: " + moviepy.__version__)
    safe_print("✅ Pydub is installed.")
    safe_print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()
