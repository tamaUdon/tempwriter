# mediapipe Hands (python) とMMMで転移学習したモデルでジェスチャ認識する
# ジェスチャモデルの実行サンプル: https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer/python

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from printer import controller as printer
import numpy as np
import copy
import argparse
import time

import cv2 as cv

model_path = './model/gesture_recognizer.task'

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode


# クライアントへkeypoints描画した画像を送り返す
# def play_processed_image(output_image):
#     #raise NotImplementedError()
#     imgencode=cv.imencode('.jpg',output_image.numpy_view())[1]
#     stringData=imgencode.tostring()
#     (b'--frame\r\n' # yieldではない
#         b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')

# 検出コールバック
# Create a hand landmarker instance with the live stream mode:
def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    
    # # keypoints描画した画像を表示する
    # try:
    #     #img_ = cv.UMat(output_image.numpy_view())
    #     # cv_mat = cv.imread(output_image)
    #     # img = np.array(output_image)
    #     #img = output_image.numpy_view()
    #     imgencode = cv.imencode('.jpg',output_image.numpy_view())[1]
    #     cv.imshow('frame',imgencode.copy()) # copy avoid Unknown C++ exceptio
    # except Exception as e:
    #     print(f'====CV Exception====\n{e}')

    im = output_image.numpy_view()
    cv.imshow('frame',im)

    # webクライアントに画像を送信する
    # imgencode=cv.imencode('.jpg',mp_image.numpy_view())[1]
    # stringData=imgencode.tostring()
    # yield (b'--frame\r\n'
    #     b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
    if cv.waitKey(1) & 0xFF == ord('q'):
        return
    
    if 0 < len(result.gestures):
         print('gesture recognition result: {}'.format(result.gestures))

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


# 初期化
def prepare():
    # printer準備
    # printer.init_printer()
    
    # カメラ準備 
    # Use OpenCV’s VideoCapture to start capturing from the webcam.
    cap=cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 960)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 540)

    # use_static_image_mode = args.use_static_image_mode
    # min_detection_confidence = args.min_detection_confidence
    # min_tracking_confidence = args.min_tracking_confidence
    # use_brect = True

    # Create an GestureRecognizer object.
    options = GestureRecognizerOptions(
        base_options=BaseOptions(model_asset_path=model_path),
        running_mode=VisionRunningMode.LIVE_STREAM,
        result_callback=print_result)

    return (cap, options)

def execute():

    # mp_hands = mp.solutions.hands
    # mp_drawing = mp.solutions.drawing_utils
    # mp_drawing_styles = mp.solutions.drawing_styles

    counter_ = 0
    isPrinting_ = False
    image_ = None
    frames = []

    cap_,options = prepare()

    with GestureRecognizer.create_from_options(options) as recognizer:
        # The landmarker is initialized. Use it here.
        # ...
        # Create a loop to read the latest frame from the camera using VideoCapture#read()
        try:
            while True:
                # counter_+=1
                # if counter_==3:
                #     counter_ = 0
                #     continue

                # カメラキャプチャ #####################################################
                ret, image_ = cap_.read()
                ms_timestamp = int(time.time()*1000) # ms単位で必要なので小数点以下四捨五入せず*1000して残す

                if not ret: return
                image_ = cv.flip(image_, 1)  # ミラー表示

                #debug_image = copy.deepcopy(image_)

                # Convert the frame received from OpenCV to a MediaPipe’s Image object.
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_) # data =  numpy_frame_from_opencv
                
                # 検出実施 
                # 画像またはビデオモデルで実行している場合、Image Embedder タスクは入力画像またはフレームの処理が完了するまで現在のスレッドをブロックします。
                # とあるので、livestreamモードで実行します
                # TODO: HandLandmarkerOptionsで設定したresult_callbackにresultが入っている
                
                # Send live image data to perform hand landmarks detection.
                # The hand landmarker must be created with the live stream mode.
                recognizer.recognize_async(mp_image, ms_timestamp)

                # 結果の処理はコールバックへ

                # cv.imshow('frame',image_)

                # # webクライアントに画像を送信する
                # # imgencode=cv.imencode('.jpg',mp_image.numpy_view())[1]
                # # stringData=imgencode.tostring()
                # # yield (b'--frame\r\n'
                # #     b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
                # if cv.waitKey(1) & 0xFF == ord('q'):
                #     break

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
