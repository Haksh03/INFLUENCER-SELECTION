import os
import pandas as pd
import numpy as np
from deepface import DeepFace
from sklearn.cluster import DBSCAN

# Paths to directories and files
faces_dir = "detected_faces_videos"  # Directory where face images are stored
frames_dir = "extracted_frames_videos"  # Directory where frames are stored
processed_videos_file = "Processed_Videos.csv"  # Path to save clustered video data
performance_metrics_file = "Performance_Metrics.csv"  # Path to save performance metrics
ranked_influencers_file = "Ranked_Influencers.csv"  # Path to save ranked influencers
face_embeddings_file = "face_embeddings.npy"  # Path to save face embeddings
face_file_mapping_file = "face_file_mapping.csv"  # Path to save face file mapping

def generate_face_embeddings(faces_dir):
    """
    Generate embeddings for all detected faces.
    """
    face_files = [f for f in os.listdir(faces_dir) if f.endswith('.jpg')]
    face_embeddings = []
    file_mapping = []

    for i, face_file in enumerate(face_files):
        face_path = os.path.join(faces_dir, face_file)
        print(f"Processing face {i + 1}/{len(face_files)}: {face_file}")
        try:
            embedding = DeepFace.represent(face_path, model_name='Facenet')[0]['embedding']
            face_embeddings.append(embedding)
            file_mapping.append(face_file)
        except Exception as e:
            print(f"Error generating embedding for {face_file}: {e}")

    # Save results
    np.save(face_embeddings_file, face_embeddings)
    pd.DataFrame({"File": file_mapping}).to_csv(face_file_mapping_file, index=False)

    print(f"Generated embeddings for {len(face_embeddings)} faces.")
    return face_embeddings, file_mapping

def cluster_faces(face_embeddings):
    """
    Cluster face embeddings using DBSCAN to identify unique influencers.
    """
    embeddings = np.array(face_embeddings)
    clustering = DBSCAN(eps=0.5, min_samples=2, metric='euclidean').fit(embeddings)
    cluster_labels = clustering.labels_

    # Debug information
    print(f"Identified {len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)} unique clusters.")
    print("Cluster Distribution:")
    unique, counts = np.unique(cluster_labels, return_counts=True)
    for label, count in zip(unique, counts):
        print(f"Cluster {label}: {count} faces")

    # Save results
    pd.DataFrame({"Cluster": cluster_labels}).to_csv("face_clusters.csv", index=False)
    return cluster_labels

def assign_clusters_to_videos(df, file_mapping, cluster_labels):
    """
    Map clustered face groups back to the videos.
    """
    for face_file, cluster_label in zip(file_mapping, cluster_labels):
        # Extract video index from file name
        video_index = int(face_file.split('_')[1])  # Adjust if naming convention differs
        df.loc[video_index, 'Face_Group'] = cluster_label

    print(f"Assigned clusters to videos. Total unique face groups: {df['Face_Group'].nunique()}")
    
    # Save updated DataFrame
    df.to_csv(processed_videos_file, index=False)
    return df

def calculate_performance_metrics(df):
    """
    Calculate average performance for each Face_Group.
    """
    grouped_data = df.groupby('Face_Group').agg({
        'Performance': ['mean', 'std', 'count']
    }).reset_index()

    grouped_data.columns = ['Face_Group', 'Avg_Performance', 'Performance_Std', 'Video_Count']

    print("Performance Metrics:")
    print(grouped_data.head())

    # Save metrics
    grouped_data.to_csv(performance_metrics_file, index=False)
    return grouped_data

def rank_influencers(performance_metrics):
    """
    Rank influencers based on their average performance.
    """
    ranked_data = performance_metrics.sort_values(by='Avg_Performance', ascending=False)
    print("Top Influencers:")
    print(ranked_data.head())

    # Save ranked influencers
    ranked_data.to_csv(ranked_influencers_file, index=False)
    return ranked_data

def main():
    # Load data
    excel_path = "C:/Users/haksh/Downloads/Assignment Data.xlsx"
    df = pd.read_excel(excel_path)

    print(f"Loaded data with {len(df)} videos.")

    # Generate face embeddings
    face_embeddings, file_mapping = generate_face_embeddings(faces_dir)

    # Cluster faces
    cluster_labels = cluster_faces(face_embeddings)

    # Assign clusters to videos
    df = assign_clusters_to_videos(df, file_mapping, cluster_labels)

    # Save clustered video data
    print("Saving clustered video data...")
    df.to_csv(processed_videos_file, index=False)

    # Calculate performance metrics
    performance_metrics = calculate_performance_metrics(df)

    # Rank influencers
    ranked_influencers = rank_influencers(performance_metrics)
    print("Workflow completed successfully. Results saved to disk.")

if __name__ == "__main__":
    main()
