import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play()
while pygame.mixer.music.get_busy():
    pass

# pygame mudou desde a video aula. É preciso ler o manual.
