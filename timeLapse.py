import cv2
import os

# Define Path to Images Folder and Get Image Files with timestamp
folder_path = r'C:\Users\James Simmill\Desktop\ImageLaps'

# Get list of the image files with their modification timestamps
images = [
    (img, os.path.getmtime(os.path.join(folder_path, img)))
    for img in os.listdir(folder_path)
    if img.endswith(".jpg")
]

# Sort images in the correct order
images.sort(key=lambda x: x[1])
images = [img[0] for img in images]

# Error handling if images not found
if not images:
    print("No images found in the specified directory.")
    exit()

# Define the ranges for the three videos
ranges = [(0, 900), (2500, 3400), (4100, 5000)]

# Loop through each range and create a video
for idx, (start, end) in enumerate(ranges):
    # Define Video Parameters
    frame = cv2.imread(os.path.join(folder_path, images[start]))
    if frame is None:
        print(f"Error reading the first image in range {start}:{end}.")
        continue

    # Resize resolution to SD (480x640)
    desired_width = 480
    desired_height = 640
    frame = cv2.resize(frame, (desired_width, desired_height))

    height, width, layers = frame.shape
    print(f"Frame size: {width}x{height}")

    video_name = f'timelapse_video_{idx+1}.avi'
    fps = 15  # Frames per second

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    if not video.isOpened():
        print(f"Error: VideoWriter not opened for video {video_name}.")
        continue

    # Add Images to the Video
    for image in images[start:end]:
        img_path = os.path.join(folder_path, image)
        frame = cv2.imread(img_path)
        if frame is None:
            print(f"Error reading image {img_path}")
            continue

        # Resize the frame to the desired resolution (1280x720)
        frame = cv2.resize(frame, (desired_width, desired_height))
        video.write(frame)

    # Release Video Writer and Finish
    video.release()
    print(f"Video saved as {video_name}")

cv2.destroyAllWindows()
