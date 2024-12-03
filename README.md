
# Influencer Performance Analysis

This repository contains the implementation for analyzing influencer performance across video datasets. The analysis includes frame extraction, face detection, clustering, and performance metric calculation.

## Problem statement

In the crowded world of social media, choosing the right influencer can make or break a campaign's success. We need your help in building a data-driven approach to influencer selection.

-> Build a system that can:

* Identify unique influencers appearing across these videos

* Calculate their average performance for each influencer 

* Help us understand which influencers consistently drive better engagement

### Project Overview
#### Goal:
 Identify unique influencers in videos, calculate their average performance.
#### Components:
Extract frames from videos.
Detect faces and generate embeddings.
Cluster similar faces using DBSCAN.
Calculate performance metrics for each influencer.
####  influencers consistently drive better engagement 

* This step is done by sorting(highest) the average perfornace of influencers and low standard deviation
  
Code Workflow
# 1. Video Frame Extraction
Extracts frames from videos provided via URLs.

Input: Video URL.

Output: Extracted frames saved locally.

# 2. Face Detection and Embedding Generation
Uses MTCNN for face detection and DeepFace for generating face embeddings.

Input: Extracted video frame.

Output: Detected faces and corresponding embeddings.

# 3. Face Clustering
Clusters face embeddings using DBSCAN.

Input: Face embeddings.

Output: Cluster labels for each face.

# 4. Video Processing
Processes all videos in the dataset by integrating frame extraction, face detection, and clustering.

Input: Dataset containing video URLs.

Output: Processed data with detected faces and cluster labels.


# 5. Performance Metrics Calculation
Calculates average performance, standard deviation, and video count for each influencer.

Input: Processed video data with performance scores.

Output: Performance metrics for each unique influencer (cluster).

# 6. Main Workflow
Orchestrates the entire process, including:

Loading video data.

Processing videos for frames, faces, and clusters.

Calculating performance metrics.

Saving results to files.


### Folders and Files
#### extracted_frames_videos/:

Stores extracted frames from videos->
detected_faces_videos/:

Stores detected face images from frames->
face_clusters/:

Contains folders for each cluster group with influencer faces

#### Input Files:

Assignment Data.xlsx: Input dataset with video URLs and performance data.

#### Output Files:

ProcessedVideos_videos.xlsx: Processed video data with face clusters.

PerformanceMetrics_videos.xlsx: Influencer performance metrics.

Ranked_Influencers.xlsx: Ranks teh influencers face groupg by their average performance.




## snippet


```bash
def extract_frame_from_video(url, video_index):
    """
    Extract a single frame from a video and save it.
    """
    # Logic for downloading video and extracting a frame
```



```bash
def detect_faces(frame, video_index):
    """
    Detect faces in the frame using MTCNN and generate embeddings.
    """
    # Logic for detecting faces and extracting embeddings
```

```bash
def cluster_faces(face_embeddings):
    """
    Cluster face embeddings using DBSCAN.
    """
    # Logic for clustering
```

```bash
def process_videos(df):
    """
    Process all videos to extract frames, detect faces, and generate clusters.
    """
    # Combines the above methods into one workflow

```
```bash
def calculate_performance(df):
    """
    Calculate average performance for each Face_Group.
    """
    # Aggregates performance metrics for each cluster
```
```bash
def main():
    """
    Main function to orchestrate the analysis workflow.
    """
    # Integrates all methods into a complete analysis

```

# OUTPUTS
The output consists of (Performance_metrics, Ranked_Influencers, Processed_videos) csv files.

The output folder consists of video frames, detected images and face_clusters which consists of images that have been repeated.

# DATASET
https://docs.google.com/spreadsheets/d/1Bj4-sd6362GWrFZOPcND3fFo0oroO1pfhkpMJh8iIE4/edit?usp=sharing


