Influencer Performance Analysis
This repository contains the implementation for analyzing influencer performance across video datasets. The analysis includes frame extraction, face detection, clustering, and performance metric calculation.

Project Overview
Goal: Identify unique influencers in videos, calculate their average performance.
Components:
Extract frames from videos.
Detect faces and generate embeddings.
Cluster similar faces using DBSCAN.
Calculate performance metrics for each influencer.
Code Workflow
1. Video Frame Extraction
Extracts frames from videos provided via URLs.

python
Copy code
def extract_frame_from_video(url, video_index):
    """
    Extract a single frame from a video and save it.
    """
    # Logic for downloading video and extracting a frame
Input: Video URL.
Output: Extracted frames saved locally.
2. Face Detection and Embedding Generation
Uses MTCNN for face detection and DeepFace for generating face embeddings.

python
Copy code
def detect_faces(frame, video_index):
    """
    Detect faces in the frame using MTCNN and generate embeddings.
    """
    # Logic for detecting faces and extracting embeddings
Input: Extracted video frame.
Output: Detected faces and corresponding embeddings.
3. Face Clustering
Clusters face embeddings using DBSCAN.

python
Copy code
def cluster_faces(face_embeddings):
    """
    Cluster face embeddings using DBSCAN.
    """
    # Logic for clustering
Input: Face embeddings.
Output: Cluster labels for each face.
4. Video Processing
Processes all videos in the dataset by integrating frame extraction, face detection, and clustering.

python
Copy code
def process_videos(df):
    """
    Process all videos to extract frames, detect faces, and generate clusters.
    """
    # Combines the above methods into one workflow
Input: Dataset containing video URLs.
Output: Processed data with detected faces and cluster labels.
5. Performance Metrics Calculation
Calculates average performance, standard deviation, and video count for each influencer.

python
Copy code
def calculate_performance(df):
    """
    Calculate average performance for each Face_Group.
    """
    # Aggregates performance metrics for each cluster
Input: Processed video data with performance scores.
Output: Performance metrics for each unique influencer (cluster).
6. Main Workflow
Orchestrates the entire process, including:

Loading video data.
Processing videos for frames, faces, and clusters.
Calculating performance metrics.
Saving results to files.
python
Copy code
def main():
    """
    Main function to orchestrate the analysis workflow.
    """
    # Integrates all methods into a complete analysis
Folders and Files
extracted_frames_videos/:

Stores extracted frames from videos.
detected_faces_videos/:

Stores detected face images from frames.
face_clusters/:

Contains folders for each cluster group with influencer faces.
Input Files:

Assignment Data.xlsx: Input dataset with video URLs and performance data.
Output Files:

ProcessedVideos_videos.xlsx: Processed video data with face clusters.
PerformanceMetrics_videos.xlsx: Influencer performance metrics.