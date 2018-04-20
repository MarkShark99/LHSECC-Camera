import sys

import pygame
import pygame.camera
from lib import Adafruit_BME280, MCP3008

AMP_PORT = 0
VOLT_PORT = 1

pygame.init()
pygame.display.init()
pygame.camera.init()

size = (320, 240)  # Resolution for PiTFT screen
screen = pygame.display.set_mode(size, 0)
cam_list = pygame.camera.list_cameras()
font = pygame.font.Font(None, 20)

thermometer = Adafruit_BME280.BME280(t_mode=Adafruit_BME280.BME280_OSAMPLE_8,
                                     p_mode=Adafruit_BME280.BME280_OSAMPLE_8,
                                     h_mode=Adafruit_BME280.BME280_OSAMPLE_8)

amp_or_something_sensor = MCP3008(clk=18, cs=25, miso=23, mosi=24)

cam = pygame.camera.Camera(cam_list[0], size)
cam.start()

while True:
    try:
        temperature = round(thermometer.read_temperature_f(), 1)  # Get temperature in fahrenheit
        amps = round(amp_or_something_sensor.read_adc(AMP_PORT), 1)
    except:
        temperature = "Error"
    
    image = cam.get_image()
    temperature_text = font.render(str(temperature), True, (255, 255, 255))
    amp_text = font.render(str(amps), True, (255, 255, 255))

    screen.blit(image, (0, 0))  # Blit image from camera to screen
    screen.blit(temperature_text + '\n' + amps, (3, 210))  # Blit temperature to screen

    pygame.display.update()

    for event in pygame.event.get():  # Get list of pygame events
        if event.type == pygame.QUIT:
            cam.stop()
            pygame.quit()
            sys.exit(0)
