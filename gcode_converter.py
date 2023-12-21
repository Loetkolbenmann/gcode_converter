# -*- coding: utf-8 -*-
"""
Author: Daniel Heink
"""

def gcode_to_array(path):
    """
    Takes gcode and returns the individual continuous paths subdivided into moves that are defined through [X,Y,Z, Feedrate, Extruder]


    Parameters
    ----------
    path : string
        Path of the file that is to be converted

    Returns
    -------
    printpaths_sorted : list
        List of the individual continuous paths subdivided into moves

    """

    gcode = open(path)
    
    #remove comments 
    gcode = [line for line in gcode if not line.startswith(";")]
    
    #remove lines with non G1 or G0 command
    gcode = [line for line in gcode if line.startswith('G1') or line.startswith('G0')]
    
    #group by moves 
    printpaths = []
    temp = []
    for line in gcode: 
        if line.startswith('G0'):
            if temp:
                printpaths.append(temp)
                temp = []
                temp.append(line)
            else:
                temp.append(line)
                
        elif line.startswith('G1'):
            temp.append(line)
            
        else:
            if temp:
                printpaths.append(temp)
                temp = []
                printpaths.append(line)
            else: 
                printpaths.append(line)
    
    #seperate into Parameters 
    current_Z = current_Y = current_X = 0
    printpaths_sorted = []          #final list containing all paths with its moves and parameters 
    for printpath in printpaths: 
        printpath_sorted = []       #contains the single path that is to be analyzed and added
        for line in printpath:
            params = line.split()
            x = y = z = e = f = None
            for param in params:
                
                if param.startswith('X'):
                    try:
                        current_X = x = float(param[1:])
                    except:
                        z = current_X
                else:
                    x = current_X
                    
                if param.startswith('Y'):
                    try:
                        current_Y =y = float(param[1:])
                    except:
                        y = current_Y
                else:
                    y = current_Y
                    
                if param.startswith('Z'):
                    try:
                        current_Z = z = float(param[1:])
                    except:
                        z = current_Z
                else:
                    z = current_Z
                    
                if param.startswith('F'):
                    f = float(param[1:])
                    
                if param.startswith('E'):
                    e = float(param[1:])
            printpath_sorted.append([x,y,z,e,f])
        printpaths_sorted.append(printpath_sorted)
    return printpaths_sorted





