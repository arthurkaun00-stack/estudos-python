import pygame

pygame.init()
pygame.mixer.music.load('Exercicios/ex021.mp3')
pygame.mixer.music.play()
input('Dê Enter para parar a música...')
'''time.sleep(5)
pygame.mixer.music.stop()
while pygame.mixer.music.get_busy(): 
    pass'''