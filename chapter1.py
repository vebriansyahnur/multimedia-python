import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') 

import pygame
import PIL
import cv2
import moviepy.editor as mp
import pydub
import tkinter as tk

print("✅ Semua pustaka telah terinstal dengan benar!")