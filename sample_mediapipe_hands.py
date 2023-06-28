# mediapipe Hands (python) とMMMで転移学習したモデルでジェスチャ認識する
# ジェスチャモデルの実行サンプル: https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer/python
# callback関数の参考: https://discuss.streamlit.io/t/unable-to-view-integrated-webcam-window/44153
# draw_landmarksの参考: https://colab.research.google.com/github/googlesamples/mediapipe/blob/main/examples/hand_landmarker/python/hand_landmarker.ipynb

# TODO: typing導入する

import mediapipe as mp
import functools
import threading
import numpy as np
import cv2 as cv
import asyncio

from asyncio import events
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from printer import controller as printer
from mediapipe.framework.formats import landmark_pb2
from typing import Any, Callable, TypeVar

T = TypeVar("T")

from concurrent.futures import ThreadPoolExecutor

model_path = './model/gesture_recognizer.task'

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

lock = threading.Lock()
current_gestures = []
current_landmarks = []
last_gesture = []
num_hands = 2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=num_hands,
    min_detection_confidence=0.65,
    min_tracking_confidence=0.65)

# ジェスチャ認識コールバック
def __callback(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    lock.acquire() # solves potential concurrency issues

    # ジェスチャ認識されていたらパースして配列に格納
    if result is not None and any(result.gestures):
        print("Recognized gestures:")
        for single_hand_gesture_data in result.gestures:
            gesture_name = single_hand_gesture_data[0].category_name
            print(gesture_name)
            current_gestures.append(gesture_name)

    # hand認識されていたらパースして配列に格納
    if not result is not None and any(result.hand_landmarks):
        for hand_landmarks in result.hand_landmarks:
            current_landmarks.append(hand_landmarks)
            
    # 300frameに1回print
    if timestamp_ms%60*5 == 0:
        printer.output_and_cut("apple🍎orange🍊bananna🍌")
                            
    lock.release()

    ### ジェスチャの戻り値形式
    # GestureRecognizerResult:
    #   Handedness:
    #     Categories #0:
    #       index        : 0
    #       score        : 0.98396
    #       categoryName : Left
    #   Gestures:
    #     Categories #0:
    #       score        : 0.76893
    #       categoryName : Thumb_Up
    #   Landmarks:
    #     Landmark #0:
    #       x            : 0.638852
    #       y            : 0.671197
    #       z            : -3.41E-7
    #     Landmark #1:
    #      ...

# ジェスチャ種類を描画
def put_gestures(image):
    lock.acquire()
    gestures = current_gestures
    lock.release()
    y_pos = 50
    for hand_gesture_name in gestures:
    # show the prediction on the frame
        cv.putText(image, hand_gesture_name, 
                   (10, y_pos), 
                   cv.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, 
                   cv.LINE_AA)
        y_pos += 50
    return image

# landmark描画
def put_landmarks(image):
    lock.acquire()
    landmarks = current_landmarks
    lock.release()
    # mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image.numpy_view())

    # Draw the hand landmarks.
    mp_drawing.draw_landmarks(
      image,
      landmarks,
      mp.solutions.hands.HAND_CONNECTIONS,
      mp.solutions.drawing_styles.get_default_hand_landmarks_style(), # If this argument is explicitly set to None, no landmarks will be drawn.
      mp.solutions.drawing_styles.get_default_hand_connections_style()) # If this argument is explicitly set to None, no connections will be drawn.
    
# # ジェスチャを画像にマップ
# def map_gesture_to_img():
#     # if current_gestures[0] == "a":
#     #     raise NotImplementedError()
#     # elif current_gestures[0] == "p":
#     #     raise NotImplementedError()
#     # elif current_gestures[0] == "l":
#     #     raise NotImplementedError()
#     # elif current_gestures[0] == "e":
#     #     raise NotImplementedError()
#     # elif current_gestures[0] == "none":
#     #     raise NotImplementedError()
#     print(f'current gestures[0]={current_gestures[0]}')
#     return "txttxttxttxttxttxt"

# # 今回認識したジェスチャと同じかチェック
# def is_gesture_changed():
#     if last_gesture[0] == current_gestures[0]:
#         return False
#     return True

# # 前回認識したジェスチャを記憶
# def update_last_gesture():
#     lock.acquire()
#     last_gesture = current_gestures
#     current_gestures = []
#     current_landmarks = []
#     lock.release()

# 初期化
def prepare():
    # printer準備
    printer.init_printer()
    
    # カメラ準備 
    # Use OpenCV’s VideoCapture to start capturing from the webcam.
    cap=cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 960)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 540)

    # Create an GestureRecognizer object.
    options = GestureRecognizerOptions(
        base_options=BaseOptions(model_asset_path=model_path),
        running_mode=VisionRunningMode.LIVE_STREAM,
        result_callback=__callback)

    return (cap, options)

# タイプライター実行
def execute():
    ms_timestamp = 0
    image_ = None
    cap_,options = prepare()
    isPrinting = False

    with GestureRecognizer.create_from_options(options) as recognizer:
        try:
            while True:
                # カメラキャプチャ #####################################################
                ret, image_ = cap_.read()
                if not ret: break

                image_ = cv.flip(image_, 1)  # ミラー表示
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_) # data =  numpy_frame_from_opencv
                recognizer.recognize_async(mp_image, ms_timestamp) # 検出実施, 結果の処理はコールバックへ
                    
                # landmarkを描画します
                copied_ = image_.copy()
                # im_ = put_gestures(copied_)
                put_landmarks(copied_)
                mp_drawing.draw_landmarks(
                    copied_,
                    current_landmarks,
                    mp.solutions.hands.HAND_CONNECTIONS,
                    mp.solutions.drawing_styles.get_default_hand_landmarks_style(), # If this argument is explicitly set to None, no landmarks will be drawn.
                    mp.solutions.drawing_styles.get_default_hand_connections_style()) # If this argument is explicitly set to None, no connections will be drawn.

                ms_timestamp += 1 # should be monotonically increasing, because in LIVE_STREAM mode
                # update_last_gesture()

                cv.imshow('MediaPipe Hands', copied_)
                if cv.waitKey(1) & 0xFF == 27:
                    break

        except KeyboardInterrupt:
            print('===KeyboardInterrupt===')
        except Exception as e:
            print(f'===Exception===\n{e}')
        finally:
            cap_.release()
            del(cap_)
            cv.destroyAllWindows()
            return
        
if __name__ == "__main__":
    execute()
