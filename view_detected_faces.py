import os
from PIL import Image
import matplotlib.pyplot as plt

# Path to the detected faces directory
faces_dir = "detected_faces_videos"

def display_faces_side_by_side(faces_dir, num_cols=5):
    """
    Display multiple detected faces side by side in a grid layout.
    
    Parameters:
    - faces_dir: Directory containing detected face images
    - num_cols: Number of images per row
    """
    face_files = [f for f in os.listdir(faces_dir) if f.endswith('.jpg')]

    if not face_files:
        print("No detected faces found.")
        return

    num_faces = len(face_files)
    num_rows = (num_faces + num_cols - 1) // num_cols  # Calculate the required number of rows

    plt.figure(figsize=(15, num_rows * 3))  # Adjust the figure size based on the number of rows

    for i, face_file in enumerate(face_files):
        face_path = os.path.join(faces_dir, face_file)
        img = Image.open(face_path)

        # Add subplot for each detected face
        plt.subplot(num_rows, num_cols, i + 1)
        plt.title(face_file, fontsize=8)  # Smaller font for file name
        plt.imshow(img)
        plt.axis("off")

    plt.tight_layout()
    plt.show()

# Display detected faces in a grid
display_faces_side_by_side(faces_dir, num_cols=5)  # Adjust num_cols for layout
