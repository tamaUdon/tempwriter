import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2 as cv
import time

model_path = './model/gesture_recognizer.task'
window_name = 'frame'

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode



# Create a gesture recognizer instance with the live stream mode:
def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    if 0 < len(result.gestures):
         print('gesture recognition result: {}'.format(result.gestures))

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
with GestureRecognizer.create_from_options(options) as recognizer:
    # The detector is initialized. Use it here.
    # ...
    # Send live image data to perform gesture recognition.

    # カメラ準備 
    # Use OpenCV’s VideoCapture to start capturing from the webcam.
    cap=cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 960)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 540)

    # Create a loop to read the latest frame from the camera using VideoCapture#read()
    try:
        while True:
            # counter_+=1
            # if counter_==3:
            #     counter_ = 0
            #     continue

            # カメラキャプチャ #####################################################
            ret, image_ = cap.read()
            # timestamp=int(unix time)
            # doc: https://developers.google.com/mediapipe/api/solutions/python/mp/tasks/vision/GestureRecognizer#recognize_async
            ms_timestamp = int(time.time()*1000) # ms単位で必要なので小数点以下四捨五入せず*1000して残す

            if not ret: continue
            cv.imshow(window_name, ret)
            image_ = cv.flip(image_, 1)  # ミラー表示

            # Convert the frame received from OpenCV to a MediaPipe’s Image object.
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_)

            # The results are accessible via the `result_callback` provided in
            # the `GestureRecognizerOptions` object.
            # The gesture recognizer must be created with the live stream mode.
            recognizer.recognize_async(mp_image, ms_timestamp)
    except KeyboardInterrupt:
            print('===KeyboardInterrupt===')
    except Exception as e:
        print(f'===Exception===\n{e}')
    finally:
        cap.release()
        del(cap)
        cv.destroyAllWindows()
    
    
    