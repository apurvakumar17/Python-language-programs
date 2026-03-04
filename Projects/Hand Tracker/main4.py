import cv2
import mediapipe as mp
import pyautogui
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Safety
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01
frame_margin = 100 

# Screen size
screen_w, screen_h = pyautogui.size()

# MediaPipe Hand Landmarker
base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)
detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

prev_x, prev_y = 0, 0
smoothening = 7

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = detector.detect(mp_image)

    if result.hand_landmarks:
        hand = result.hand_landmarks[0]

        # Index finger tip (8), Thumb tip (4)
        index_tip = hand[8]
        thumb_tip = hand[4]

        x = int(index_tip.x * w)
        y = int(index_tip.y * h)

        # Map webcam coords → screen coords
        x_clamped = np.clip(x, frame_margin, w - frame_margin)
        y_clamped = np.clip(y, frame_margin, h - frame_margin)

        screen_x = np.interp(
            x_clamped,
            (frame_margin, w - frame_margin),
            (0, screen_w)
        )

        screen_y = np.interp(
            y_clamped,
            (frame_margin, h - frame_margin),
            (0, screen_h)
        )


        # Smooth mouse movement
        curr_x = prev_x + (screen_x - prev_x) / smoothening
        curr_y = prev_y + (screen_y - prev_y) / smoothening

        pyautogui.moveTo(curr_x, curr_y)

        prev_x, prev_y = curr_x, curr_y

        # Pinch distance for click
        pinch_dist = np.hypot(
            (index_tip.x - thumb_tip.x) * w,
            (index_tip.y - thumb_tip.y) * h
        )

        if pinch_dist < 40:
            pyautogui.click()

        # Visual feedback
        cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

    cv2.rectangle(
        frame,
        (frame_margin, frame_margin),
        (w - frame_margin, h - frame_margin),
        (255, 0, 255),
        2
    )

    cv2.imshow("Hand Mouse Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
