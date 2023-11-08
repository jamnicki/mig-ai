import cv2
import mediapipe as mp
import csv
from src.settings import MOVIE_CLIPS_DIR


video_path = MOVIE_CLIPS_DIR / 'K01AF/K01AF__07_5160-5640.mp4'
print(video_path)
output_csv = 'output.csv'

# Initialize MediaPipe Pose and Drawing utilities
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Open the video file
cap = cv2.VideoCapture(video_path)

frame_number = 0
csv_data = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Pose
    result = pose.process(frame_rgb)

    # Draw the pose landmarks on the frame
    if result.pose_landmarks:
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Add the landmark coordinates to the list and print them
        # write_landmarks_to_csv(result.pose_landmarks.landmark, frame_number, csv_data)

    cv2.imshow(frame)