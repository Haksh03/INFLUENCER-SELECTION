# process_videos.py

from extract_frames import extract_frame_from_video
from detect_faces import detect_faces
from cluster_faces import cluster_faces

def process_videos(df):
    """
    Process all videos to extract frames, detect faces, and generate clusters.
    """
    face_embeddings = []
    video_face_map = []  # Map video index to embeddings for clustering
    df['Faces_Detected'] = 0
    df['Face_Group'] = None

    for i, row in df.iterrows():
        url = row['Video URL']
        print(f"Processing video {i + 1}/{len(df)}: {url}")
        
        frame = extract_frame_from_video(url, i)
        if frame is not None:
            embeddings = detect_faces(frame, i)
            df.loc[i, 'Faces_Detected'] = len(embeddings)
            for embedding in embeddings:
                face_embeddings.append(embedding)
                video_face_map.append(i)
    
    # Cluster embeddings
    if face_embeddings:
        print("Clustering face embeddings...")
        cluster_labels = cluster_faces(face_embeddings)
        
        # Assign cluster labels to videos
        for video_idx, cluster_label in zip(video_face_map, cluster_labels):
            df.at[video_idx, 'Face_Group'] = cluster_label

    return df
