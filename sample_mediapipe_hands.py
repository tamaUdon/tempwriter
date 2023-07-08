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
import statistics

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
current_img = None
last_gesture = ""
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
    global current_img
    global last_gesture
    copied_ = output_image.numpy_view()

    # ジェスチャ認識されていたらパースして配列に格納
    if result is not None and any(result.gestures):
        # print("Recognized gestures:")
        for single_hand_gesture_data in result.gestures:
            if gesture_name := single_hand_gesture_data[0].category_name:
                # print(gesture_name)
                current_gestures.append(gesture_name)
                #put_gestures(copied_,current_gestures)

    # hand認識されていたらパースして配列に格納
    if result is not None and any(result.hand_landmarks):
        for hand_landmarks in result.hand_landmarks:
            # landmarkを描画します
            # print(f'hand_landmarks={hand_landmarks}')
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
            ])
            mp_drawing.draw_landmarks(
                copied_,
                hand_landmarks_proto,
                mp.solutions.hands.HAND_CONNECTIONS,
                mp.solutions.drawing_styles.get_default_hand_landmarks_style(), # If this argument is explicitly set to None, no landmarks will be drawn.
                mp.solutions.drawing_styles.get_default_hand_connections_style()) # If this argument is explicitly set to None, no connections will be drawn.
    current_img = copied_
            
    # 240frameに1回print
    if timestamp_ms%60*4 == 0:
        if any(current_gestures):
            mode = statistics.mode(current_gestures)
            print(f'current gestures={current_gestures}')
            print(f'最頻値={mode}')
            if mode != "none" and last_gesture != mode:
                with open(f'./data/AA/{mode}.txt') as f:
                    s = f.read()
                    printer.write(s)
            last_gesture = mode
            current_gestures.clear()

# ジェスチャ種類を描画
def put_gestures(image, current_gestures):
    y_pos = 50
    for hand_gesture_name in current_gestures:
    # show the prediction on the frame
        cv.putText(image, hand_gesture_name, 
                   (10, y_pos), 
                   cv.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, 
                   cv.LINE_AA)
        y_pos += 50

# 初期化
def prepare():
    # printer準備
    printer.init_printer()
    
    # カメラ準備 
    cap=cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 960)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 540)

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

    with GestureRecognizer.create_from_options(options) as recognizer:
        try:
            while True:
                ret, image_ = cap_.read()
                if not ret: break

                image_ = cv.flip(image_, 1)  # ミラー表示
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_) # data =  numpy_frame_from_opencv
                recognizer.recognize_async(mp_image, ms_timestamp) # 検出実施, 結果の処理はコールバックへ
                ms_timestamp += 1 # should be monotonically increasing, because in LIVE_STREAM mode

                if current_img is not None:
                    cv.imshow('MediaPipe Hands', current_img)
                else:
                    cv.imshow('MediaPipe Hands', image_)

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
