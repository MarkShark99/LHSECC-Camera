# LHSECC-Camera
Stands for:
> Lakeshore\
> High\
> School\
> Electric\
> Car\
> Club\
> Camera

This program was requested by Lakeshore High School's electric car racing team for use during races to display a video feed and monitor the temperature and the voltage and amperage draws of the car via an onboard Raspberry Pi.

## Components
- Raspberry Pi Zero W - Main board
- Raspberry Pi Camera Module - Camera for live video feed
- Adafruit PiTFT - Screen used to display sensor values and video feed
- Adafruit BME280 - Temperature sensor for monitoring the temperature of the car
- Adafruit MCP3008 - Analog to digital converter for use with the voltage and amperage sensor

## Features
### Live video feed
Using PyGame's camera module, the program is able to stream the camera feed directly to the screen. This was used to ensure better visibility behind the car during races.

### Temperature monitoring
Using an Adafruit BME280 temperature sensor, the program is able to monitor the temperature (in fahrenheit) of either the cabin or the motor and battery compartment of the car, and display it over the video feed.

### Voltage and amperage monitoring
Using an Adafruit MCP3008 Analog-to-Digital convertor and another unknown sensor, the program is able to monitor the voltage and amperage being drawn by the car's motor, and display these values over the video feed. 

## Unimplemented Features
This is a list of features that were considered or worked on but were ultimately scrapped as this project had to be finished incredibly quickly while minimizing points of failure.

### Wireless track timer and video feed
Using a Wi-Fi network and a custom antenna attached to the Raspberry Pi, the program would be able to stream its video feed over the network and have a track timer that was controlled by a spectator. While the antenna was built and attached to a Raspberry Pi, that Pi ended up being broken by a member of the team and was replaced by one without the antenna. There was also the issue of range of Wi-Fi while on the track.

### Video storage
The program was originally going to store the live video feed to disk, but this idea was scrapped as continuously writing to the Pi's SD card could be a point of failure.