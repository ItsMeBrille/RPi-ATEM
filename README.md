# RPi-ATEM
RPi-ATEM is an automatic camera project designed to simplify the process of capturing video in a live event. The project combines various components to produce an efficient and streamlined video capturing process.

## Website
The project enables you to draw rectangles on an image captured by a "system camera". You can then name, move, or delete these rectangles using a list that appears under the picture.

## AutoCam
The AutoCam feature utilizes a camera to determine whether a person is within any of the specified locations. If the person is in multiple places, the system prioritizes the location closest to the center of the stage. The microphone sound also plays a role, with the pulpit microphone having priority. The system switches to a camera that points to where the person is located and captures clips based on their position and microphone sound.

### Clipping rules:
- Switch to a camera that points to where the person is.
  - People towards the center of the stage have priority. Exception if sound comes from certain microphones. Then it has priority. For example if there is a lectern with seperate microphone
  - If necessary, move the camera first. If the camera to be moved is already on, a shot from the total angle must show in between.
- If there are completely silent clips between total, person and short, preset videos from around the room. Put such videos in `src` folder
- If the same camera has been on for a long duration of time, cut to total shot for a few seconds.

## Tally
The RPi-ATEM project also features an ESP8266 with an LED light that can be wirelessly connected to act as a tally light.
