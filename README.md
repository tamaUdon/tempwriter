### What is TEMP-WRITER

TEMP-WRITER is a virtual typewriter system that can be used on a desktop.  
 It utilizes mediapipe(Hands) to recognize your hand gestures, and a thermal printer (EPSON TM-T90) is used to print images and strings that have been bound to specific gestures in real-time.

The preset images and strings can be customized and used for various creative purposes.  
For example, registering alphabets and symbols will make it work like a "real" typewriter.  
It is also possible to endlessly print out only kawaii cat images.

Now, please enjoy this creation.

### install

`git clone <tempwriter-repo>`  
`cd tempwriter`  
`poetry install`  
`poetry run python tempwriter/main.py`  
`poetry run python -m SimpleHTTPServer`

### note

this project based on https://github.com/Kazuhito00/mediapipe-python-sample, https://clutter.ikuta.me/webusb-escpos-demo/ and https://github.com/samccone/thermal_print
