# -*- coding: utf-8 -*-

# Create ATEMMax object
import PyATEMMax
switcher = PyATEMMax.ATEMMax()

# Connect
switcher.connect("192.168.1.100")
switcher.waitForConnection()

# Have fun!
switcher.setPreviewInputVideoSource(0, 5)  # Set PVW on input 5 for m/e 0