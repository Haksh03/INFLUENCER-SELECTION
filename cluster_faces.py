# cluster_faces.py

import numpy as np
from sklearn.cluster import DBSCAN

def cluster_faces(face_embeddings):
    """
    Cluster face embeddings using DBSCAN.
    """
    try:
        embeddings = np.array(face_embeddings)
        clustering = DBSCAN(eps=0.7, min_samples=2, metric='euclidean').fit(embeddings)
        return clustering.labels_
    except Exception as e:
        print(f"Error clustering faces: {e}")
        return []
