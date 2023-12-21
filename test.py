# -*- coding: utf-8 -*-
"""
This program takes gcode and returns the individual extrusions that the printhead lays down. 

"""
from gcode_converter import gcode_to_array
from pathlib import Path
import matplotlib.pyplot as plt

gcode = gcode_to_array(Path('input_gcode','grbl laser.nc'))

#visualize 
plt.figure().add_subplot(projection = '3d')
for path in gcode:
    for move in path:
        plt.scatter(*move[:3])
        
