from turtle import Screen
import pygame
pygame.init()

# Memuat gambar
screen = pygame.display.set_mode((800, 600))
image = pygame.image.load('example.jpg')

#Loop utama permainan
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #memperbarui posisi
    x += 5
    if x > 800:
        x = 0
    #Menggambar gambar
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()
    
    # Memuat suara
    sound = pygame.mixer.Sound('example.mp3')

     #Memutar suara
    sound.play()

pygame.quit()

