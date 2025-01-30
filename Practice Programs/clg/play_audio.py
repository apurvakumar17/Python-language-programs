import pygame

pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\\kumar\\Downloads\\Copines(PagalWorld).mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue  # Keep script running while audio plays
