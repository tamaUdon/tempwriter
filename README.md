### What is TEMP-WRITER

TEMP-WRITER is a virtual typewriter system that can be used on a desktop.  
 It utilizes mediapipe(Hands) to recognize your hand gestures, and a thermal printer (EPSON TM-T90) is used to print images and strings that have been bound to specific gestures in real-time.

The preset images and strings can be customized and used for various creative purposes.  
For example, registering alphabets and symbols will make it work like a "real" typewriter.  
It is also possible to endlessly print out only kawaii cat images.

Now, please enjoy this creation.

### Install

```
$ brew install libusb // requirements for pyusb (macOS)
$ poetry install
$ poetry run python xxx.py
```

### Train model

[colab](https://colab.research.google.com/drive/1JMFFDpNhgk0m1NZFeWFyuNj6yojQzyKI?usp=sharing)
