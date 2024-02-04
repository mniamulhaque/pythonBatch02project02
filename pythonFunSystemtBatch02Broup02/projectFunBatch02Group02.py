import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('Amar.mp3')
pygame.mixer.music.play()
sleep(5)
pygame.mixer.music.load('song2.mpeg')
pygame.mixer.music.play()
sleep(1)
image = pygame.image.load('bhot.jpeg')
window.blit(image,(0,0))
pygame.display.update()
sleep(3)
#Batch - 02 Create, Group - 02
#name of grou member
#1.Sumaiya ,1.Mariya, 3.Moshfika, 4.Moriom, 5.Taskiya, 6.Jara, 7.Taher, 8.Ikra