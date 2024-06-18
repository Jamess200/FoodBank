import cv2
import os

# Define Path to Images Folder and Get Image Files with timestamp
folder_path = r'C:\Users\James Simmill\Desktop\ImageLaps'
images = [(img, os.path.getmtime(os.path.join(folder_path, img))) for img in os.listdir(folder_path) if img.endswith(".")]

# Sort images in the correct order
images.sort(key=lambda x: x[1])
images = [img[0] for img in images]

# Error handeling if images not found
if not images:
    print("No images found in the specified directory.")
    exit()

# Define Video Parameters
frame = cv2.imread(os.path.join(folder_path, images[0]))
if frame is None:
    print("Error reading the first image.")
    exit()

height, width, layers = frame.shape
print(f"Frame size: {width}x{height}")

video_name = 'timelapse_video.avi'
fps = 10  # Frames per second

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

if not video.isOpened():
    print("Error: VideoWriter not opened.")
    exit(1)

# Add Images to the Video
for image in images:
    img_path = os.path.join(folder_path, image)
    frame = cv2.imread(img_path)
    if frame is None:
        print(f"Error reading image {img_path}")
        continue
    video.write(frame)

# Release Video Writer and Finish
video.release()
cv2.destroyAllWindows()

print(f"Video saved as {video_name}")
