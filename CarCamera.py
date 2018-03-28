import sys
import pygame
import pygame.camera
import pygame.font

pygame.init()
pygame.display.init()
pygame.camera.init()

size = (320, 240) # Resolution for PiTFT screen
screen = pygame.display.set_mode(size, 0)
cam_list = pygame.camera.list_cameras()
font = pygame.font.Font(None, 30)

cam = pygame.camera.Camera(cam_list[0], size)
cam.start()

while True:
    image = cam.get_image()
    r = font.render("TEST", True, (255, 255, 255))
    screen.blit(image, (0, 0))
    screen.blit(r, (100, 100))
    
    pygame.display.update()
    
    for event in pygame.event.get()
        if event.type == pygame.QUIT:
            cam.stop()
            pygame.quit()
            sys.exit(0)