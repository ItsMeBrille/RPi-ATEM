# RPi-ATEM
RPi-ATEM is an automatic camera project designed to simplify the process of capturing video in a live event. The project combines various components to produce an efficient and streamlined video capturing process.

## Website
The project enables you to draw rectangles on an image captured by a "system camera". You can then name, move, or delete these rectangles using a list that appears under the picture.

## AutoCam
The AutoCam feature utilizes a camera to determine whether a person is within any of the specified locations. If the person is in multiple places, the system prioritizes the location closest to the center of the stage. The microphone sound also plays a role, with the pulpit microphone having priority. The system switches to a camera that points to where the person is located and captures clips based on their position and microphone sound.

### Clipping rules:
- If there are completely silent clips, the system uses preset videos from a folder.
- If necessary, the system moves the camera first.
  - If the camera to be moved is already on, a total image must come in between.
- If the same camera has been on for an extended period, the system cuts to a total image for a few seconds.

## Tally
The RPi-ATEM project also features an ESP8266 with an LED light that can be wirelessly connected to act as a tally light.
