# detect_faces.py

import os
import cv2
from deepface import DeepFace
from mtcnn.mtcnn import MTCNN

faces_dir = "detected_faces_videos"
os.makedirs(faces_dir, exist_ok=True)

def detect_faces(frame, video_index):
    """
    Detect faces in the frame using MTCNN and save them.
    """
    try:
        detector = MTCNN()
        results = detector.detect_faces(frame)

        face_embeddings = []
        for idx, result in enumerate(results):
            x, y, w, h = result['box']
            face = frame[y:y+h, x:x+w]
            face = cv2.resize(face, (160, 160))  # Resize for DeepFace
            face_path = os.path.join(faces_dir, f"video_{video_index}_face_{idx}.jpg")
            cv2.imwrite(face_path, face)

            embedding = DeepFace.represent(face, model_name='Facenet')[0]['embedding']
            face_embeddings.append(embedding)

        return face_embeddings
    except Exception as e:
        print(f"Error detecting faces for video {video_index}: {e}")
        return []
