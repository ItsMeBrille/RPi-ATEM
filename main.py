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
    # ["Navn", Inngang, Mikrofon(Bool), PTZ("192.168.1.1")]
    cameradict = {
        0 : ["Oversikt", 3, "mic3"],
        1 : ["Alter", 4, 4],
        2 : ["Prekestol", 5, 5]
    }
    
    return cameradict








autocamactive = True

# Get cameras to choose from
cameras = getAvailableCameras()


while True:
        
    # Budrunde på kamera
    
    # Mikrofon
    if (switcher.audioMixer.input["mic1"].volume < 0):
        
    
    
    # Deside what camera to switch to
    cameratoswitchto = 
    
    
    # Switch camera
    print(cameratoswitchto)
    time.sleep(1)
    
    
    
    
    
    
    