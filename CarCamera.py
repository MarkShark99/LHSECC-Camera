import sys

import pygame
from lib import Adafruit_BME280

pygame.init()
pygame.display.init()
pygame.camera.init()

size = (320, 240) # Resolution for PiTFT screen
screen = pygame.display.set_mode(size, 0)
cam_list = pygame.camera.list_cameras()
font = pygame.font.Font(None, 20)

thermometer = Adafruit_BME280.BME280(t_mode=Adafruit_BME280.BME280_OSAMPLE_8,
                                     p_mode=Adafruit_BME280.BME280_OSAMPLE_8,
                                     h_mode=Adafruit_BME280.BME280_OSAMPLE_8)

cam = pygame.camera.Camera(cam_list[0], size)
cam.start()

while True:
    temperature = thermometer.read_temperature_f() #Get temperature in fahrenheit
    image = cam.get_image()
    r = font.render("TEST", True, (255, 255, 255))
    screen.blit(image, (0, 0))
    screen.blit(r, (300, 220))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cam.stop()
            pygame.quit()
            sys.exit(0)