#Test program for MLX90640 class, uses matplotlib for plotting temperatures
#Based on example from https://matplotlib.org/stable/gallery/animation/animation_demo.html
#UBC PHAS E-lab, Nov 2022
#Required Packages:
#pyserial
#matplotlib



from MLX90640 import MLX90640
import matplotlib
matplotlib.use('Tkagg')
import matplotlib.pyplot as plt
import numpy as np

#MLX Framerate values 0-7 are 0.5-64Hz
#0 = 0.5Hz
#1 = 1Hz
#2 = 2Hz
#3 = 4Hz
#4 = 8Hz
#5 = 16Hz
#6 = 32Hz
#7 = 64Hz
sensor = MLX90640(port="COM5", baud=115200, framerate=3)#Actual com port name will depend on system

fig, ax = plt.subplots()
plt.inferno()
loop = 0
try:
    while True:
        #Calculate temperature values from MLX RAM
        floatarray = [[sensor.getCompensatedPixDataRAM(i+1,j+1) for i in range(24)] for j in range(32)]
        cmap = ax.imshow(floatarray) #Show the image
        ax.set_title("Temperature Map")
        cb = fig.colorbar(cmap, ax = ax) #Show a colorbar
        plt.pause(0.001)
        sensor.updateRAM() #get copy new of RAM from MLX90640
        loop = loop + 1
        print(loop)
        cb.remove() #remove old plots
        ax.cla()        
finally:
    sensor.close()
