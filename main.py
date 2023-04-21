# -*- coding: utf-8 -*-

import time
import random



def get_key_matching_values(dictionary, values):
    matching_keys = []
    for key in dictionary:
        if dictionary[key] in values:
            matching_keys.append(key)
    if len(matching_keys) > 0:
        return random.choice(matching_keys)
    else:
        return None


# Function to see what cameras are available
def getAvailableCameras():
    # Define all cameras:
    # # n : ["Camera name", ATEM port, Mic port on RPi, PTZ("192.168.1.1")]
    all_cameras = {
        0 : ["Oversikt", 3, 3],
        1 : ["Alter", 4, 4],
        2 : ["Prekestol", 5, 5]
    }
    
    # Check if available
    for i in all_cameras:
        print(i)

    return cameradict








autocamactive = True

# Get cameras to choose from
cameras = getAvailableCameras()


while True:
        
    # Budrunde på kamera
    
    # Mikrofon
    if (switcher.audioMixer.input["mic1"].volume < 0):
        
    
    
    # Deside what camera to switch to
    cameratoswitchto = 0
    
    
    # Switch camera
    print(cameratoswitchto)
    time.sleep(1)
    
    
    
    
    
    
    