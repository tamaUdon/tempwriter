import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5,
)

image = cv2.imread('../images/Flame_29.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = hands.process(image)



