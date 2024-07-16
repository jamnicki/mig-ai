import cv2
import mediapipe as mp
import pandas as pd
from src.settings import MOVIE_CLIPS_DIR, DATA_DIR, POLISH_ANNOTATIONS_SLICED
import os
import glob
import os.path
import re
import tqdm


def write_landmarks_to_csv(landmarks, frame_number, csv_data, video_name):
    for idx, landmark in enumerate(landmarks):
        csv_data.append([video_name, frame_number, mp_pose.PoseLandmark(idx).name, idx,landmark.x, landmark.y, landmark.z])


def get_pose_landmarks(video_path, output_csv, output_dir, video_file):
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
            write_landmarks_to_csv(result.pose_landmarks.landmark, frame_number, csv_data, video_file)

        # cv2.imshow('Pose estimation',frame)
        # filename = f'saved_image_{frame_number}.jpg'
        frame_number +=1
        # Using cv2.imwrite() method 
        # Saving the image 
        # cv2.imwrite(filename, frame) 

    
    df = pd.DataFrame(csv_data, columns=['VideoName', 'FrameNumber','LandmarkName','LandmarkIdx','X', 'Y', 'Z'])

    if not os.path.exists(output_dir): 
        os.makedirs(output_dir) 
    df.to_csv(output_csv)


mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# video_dir = 'K01AF'
# video_file = 'K01AF__07_5160-5640.mp4'
# video_path = str(MOVIE_CLIPS_DIR / video_dir / video_file)


movies = os.listdir(POLISH_ANNOTATIONS_SLICED)
videos = os.listdir(POLISH_ANNOTATIONS_SLICED/str(movies[0]))
files = glob.glob(os.path.join(POLISH_ANNOTATIONS_SLICED/str(movies[0]), '*.mp4'))

for movie in movies[60:]:
    video_clips = glob.glob(os.path.join(POLISH_ANNOTATIONS_SLICED/str(movie), '*.mp4'))
    print(movie)
    for clip in video_clips:
        print(clip)
        clip_match = re.search(r'([^/]+)\.mp4$', clip).group(1)
        output_dir = DATA_DIR / 'landmarks' / movie
        output_csv = DATA_DIR / 'landmarks' / movie / f"{clip_match}.csv"
        get_pose_landmarks(clip, output_csv, output_dir, movie)

