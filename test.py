# -*- coding: utf-8 -*-
"""
This program takes gcode and returns the individual extrusions that the printhead lays down. 

"""
from gcode_converter import gcode_to_array, visualize_paths
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

gcode = gcode_to_array(Path('input_gcode','slab_gcode.gcode'))

visualize_paths(gcode,include_positioning_move=True)