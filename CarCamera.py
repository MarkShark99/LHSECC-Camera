'''
Written by Mark Washington
''' 

import sys

import pygame
import pygame.camera
from lib import Adafruit_BME280, MCP3008

VOLT_PORT = 1
AMP_PORT = 3

pygame.init()
pygame.display.init()
pygame.camera.init()

resolution = (320, 240)  # Resolution for PiTFT screen
screen = pygame.display.set_mode(resolution, 0)
cam_list = pygame.camera.list_cameras()
overlay_font = pygame.overlay_font.overlay_font(None, 20)

thermometer = Adafruit_BME280.BME280(t_mode=Adafruit_BME280.BME280_OSAMPLE_8,
                                     p_mode=Adafruit_BME280.BME280_OSAMPLE_8,
                                     h_mode=Adafruit_BME280.BME280_OSAMPLE_8)

amp_volt_sensor = MCP3008.MCP3008(clk=18, cs=25, miso=23, mosi=24)

cam = pygame.camera.Camera(cam_list[0], resolution)
cam.start()

while True:
    try:
        temperature = round(thermometer.read_temperature_f(), 1)
        amps = round(amp_volt_sensor.read_adc(AMP_PORT), 1)
        volts = round(amp_volt_sensor.read_adc(VOLT_PORT), 1)
    except:
        temperature = "Error"
        amps = "Error"
        volts = "Error"
    
    image = cam.get_image()

    temperature_text = overlay_font.render("Temp  " + str(temperature), True, (255, 255, 255))
    amperage_text = overlay_font.render("Amps: " + str(amps), True, (255, 255, 255))
    voltage_text = overlay_font.render("Volt: " + str(volts), True, (255, 255, 255))

    screen.blit(image, (0, 0))  # Blit image from camera to screen
    screen.blit(temperature_text, (3, 190))  # Blit temperature to screen
    screen.blit(amperage_text, (3, 205))
    screen.blit(voltage_text, (3, 220))

    pygame.display.update()

    for event in pygame.event.get():  # Get list of pygame events and check for request to quit
        if event.type == pygame.QUIT:
            cam.stop()
            pygame.quit()
            sys.exit(0)
