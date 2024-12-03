# extract_frames.py

import os
import cv2
import requests

frames_dir = "extracted_frames_videos"
os.makedirs(frames_dir, exist_ok=True)

def extract_frame_from_video(url, video_index):
    """
    Extract a frame from the video and save it.
    """
    try:
        response = requests.get(url, stream=True, timeout=10)
        video_path = f"temp_video_{video_index}.mp4"
        with open(video_path, 'wb') as f:
            f.write(response.content)
        
        cap = cv2.VideoCapture(video_path)
        success, frame = cap.read()
        cap.release()
        
        if success:
            frame_path = os.path.join(frames_dir, f"frame_{video_index}.jpg")
            cv2.imwrite(frame_path, frame)
            print(f"Frame saved: {frame_path}")
            return frame
        else:
            print(f"Failed to extract frame from video {video_index}")
            return None
    except Exception as e:
        print(f"Error extracting frame from {url}: {e}")
        return None
