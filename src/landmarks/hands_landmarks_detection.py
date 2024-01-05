import cv2
import mediapipe
import pandas as pd
from src.settings import MOVIE_CLIPS_DIR, DATA_DIR

def write_landmarks_to_csv(landmarks, frame_number, csv_data, video_name):
    for idx, landmark in enumerate(landmarks):
        csv_data.append([video_name, frame_number, handsModule.HandLandmark(idx).name, idx, landmark.x, landmark.y, landmark.z])

video_dir = 'K01AF'
video_file = 'K01AF__07_5160-5640.mp4'
video_path = str(MOVIE_CLIPS_DIR / video_dir / video_file)
output_csv = DATA_DIR / 'landmarks/K01AF__07_5160-5640_hands.csv'

handsModule = mediapipe.solutions.hands
cap= cv2.VideoCapture(video_path)
frame_number = 0
mp_drawing = mediapipe.solutions.drawing_utils
csv_data = []

with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.3, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
          break

      frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      results = hands.process(frame_rgb)

      print(len(results.multi_hand_landmarks))

      if results.multi_hand_landmarks != None:
          for handLandmarks in results.multi_hand_landmarks:
              mp_drawing.draw_landmarks(frame, handLandmarks, handsModule.HAND_CONNECTIONS)

              write_landmarks_to_csv(handLandmarks.landmark, frame_number, csv_data, video_file)

      filename = f'saved_image_{frame_number}.jpg'
      frame_number +=1
    # Using cv2.imwrite() method 
    # Saving the image 
      cv2.imwrite(filename, frame) 

df = pd.DataFrame(csv_data)
df.to_csv(output_csv)