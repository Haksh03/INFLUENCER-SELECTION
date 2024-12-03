import os
from PIL import Image
import matplotlib.pyplot as plt

# Path to the extracted frames directory
frames_dir = "extracted_frames_videos"  # Updated directory name

def display_images_side_by_side(image_dir, num_cols=5):
    """
    Display multiple images side by side in a grid layout.
    
    Parameters:
    - image_dir: Directory containing images
    - num_cols: Number of images per row
    """
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

    if not image_files:
        print("No images found in the directory.")
        return

    num_images = len(image_files)
    num_rows = (num_images + num_cols - 1) // num_cols  # Calculate the required number of rows

    plt.figure(figsize=(15, num_rows * 3))  # Adjust the figure size based on rows

    for i, image_file in enumerate(image_files):
        image_path = os.path.join(image_dir, image_file)
        img = Image.open(image_path)

        # Add subplot for each image
        plt.subplot(num_rows, num_cols, i + 1)
        plt.title(image_file, fontsize=8)  # Use smaller font for titles
        plt.imshow(img)
        plt.axis("off")

    plt.tight_layout()
    plt.show()

# Display extracted frames side by side
display_images_side_by_side(frames_dir, num_cols=5)  # Adjust num_cols for layout
