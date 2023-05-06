#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ref. https://colab.research.google.com/github/googlesamples/mediapipe/blob/main/examples/gesture_recognizer/python/gesture_recognizer.ipynb#scrollTo=KHqaswD6M8iO

import os
import csv
import copy
import argparse
import itertools
import asyncio
import cv2 as cv
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2
from collections import Counter
from collections import deque
from concurrent.futures import ThreadPoolExecutor

from printer import controller as printer

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)
    parser.add_argument('--use_static_image_mode', action='store_true')
    parser.add_argument("--min_detection_confidence",
                        help='min_detection_confidence',
                        type=float,
                        default=0.7)
    parser.add_argument("--min_tracking_confidence",
                        help='min_tracking_confidence',
                        type=int,
                        default=0.5)

    args = parser.parse_args()
    return args

def prepare():
    printer.init_printer()
    
    # 引数解析
    args = get_args()
    cap_device = args.device
    cap_width = args.width
    cap_height = args.height

    # use_static_image_mode = args.use_static_image_mode
    # min_detection_confidence = args.min_detection_confidence
    # min_tracking_confidence = args.min_tracking_confidence
    # use_brect = True

    # カメラ準備 
    cap=cv.VideoCapture(cap_device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    # Create an GestureRecognizer object.
    base_options = python.BaseOptions(model_asset_path='./hands/model/gesture_recognizer.task')
    options = vision.GestureRecognizerOptions(base_options=base_options)
    recognizer = vision.GestureRecognizer.create_from_options(options)

    return (cap,recognizer)

def draw_info(image, gesture):
    title = f"{gesture.category_name} ({gesture.score:.2f})"
    if title != "":
        info_text += ' : ' + title
    cv.putText(image, info_text, (100,100),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv.LINE_AA)
    # return image
    

def execute():

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    counter_ = 0
    isPrinting_ = False
    image_ = None

    cap_,recognizer_ = prepare()

    try:
        while True:
            counter_+=1
            if counter_==3:
                counter_ = 0
                continue

            # カメラキャプチャ #####################################################
            ret, image_ = cap_.read()
            if not ret: return
            image_ = cv.flip(image_, 1)  # ミラー表示
            debug_image = copy.deepcopy(image_)

            # 検出実施 
            image_ = cv.cvtColor(image_, cv.COLOR_BGR2RGB)
            recognition_result = recognizer_.recognize(image_)

            # 結果の処理
            top_gesture = recognition_result.gestures[0][0]
            hand_landmarks = recognition_result.hand_landmarks

            # # 印刷指示
            # if not isPrinting_:
            #     isPrinting_ = True
            #     ### start thread (escposがasyncio未対応のためconcurrent.futureでラップしています😿) ###
            #     # ref. https://gist.github.com/tag1216/40b75346fd4ffdbfba22a55905094b0e#file-03_map-py
            #     with ThreadPoolExecutor(max_workers=2, thread_name_prefix="print_thread") as executor:
            #         future = executor.submit(printer.output_and_cut, "XXXXXXX!")
            #     # print(future.result())
            # ### end thread ###
            # isPrinting_ = False

            # 描画処理
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
            ])

            mp_drawing.draw_landmarks(
                image_,
                hand_landmarks_proto,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            debug_image = draw_info(image_,top_gesture)

            # クライアントへkeypoints描画した画像を送り返す #############################################################
            imgencode=cv.imencode('.jpg',debug_image)[1]
            stringData=imgencode.tostring()
            yield (b'--frame\r\n'
                b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')


    except KeyboardInterrupt:
        print('===KeyboardInterrupt===')
    except Exception as e:
        print(f'===Exception===\n{e.with_traceback}')
    finally:
        cap_.release()
        del(cap_)
        cv.destroyAllWindows()
        return
