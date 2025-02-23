import cv2
import os

# Ask user for folder path and validate
folder_path = input("Enter the path to your image folder: ").strip()
if not os.path.exists(folder_path):
    print("Error: The specified folder does not exist.")
    exit()

# Define valid image extensions
valid_extensions = (".jpg", ".jpeg", ".png")

# Get list of image files with modification timestamps
images = [
    (img, os.path.getmtime(os.path.join(folder_path, img)))
    for img in os.listdir(folder_path)
    if img.lower().endswith(valid_extensions)
]

# Sort images in the correct order
images.sort(key=lambda x: x[1])
images = [img[0] for img in images]

# Error handling if no images found
if not images:
    print("No images found in the specified directory.")
    exit()

# Ask user for video segments
ranges = []
print("Enter the start and end indices for each video segment. Type 'done' when finished.")

while True:
    user_input = input("Enter range as 'start,end' or 'done': ").strip()
    if user_input.lower() == "done":
        break
    try:
        start, end = map(int, user_input.split(","))
        if start < 0 or end < 0:
            print("Error: Start and end indices must be positive integers.")
            continue
        if start >= end:
            print("Error: Start index must be less than end index.")
            continue
        if end > len(images):
            print("Error: End index exceeds available images.")
            continue
        ranges.append((start, end))
    except ValueError:
        print("Invalid input. Please enter two numbers separated by a comma.")

# Loop through ranges and create videos
for idx, (start, end) in enumerate(ranges):
    full_image_path = os.path.join(folder_path, images[start])
    frame = cv2.imread(full_image_path)

    if frame is None:
        print(f"Error reading the first image in range {start}:{end}. Skipping this range.")
        continue

    # Resize resolution to SD (480x640)
    desired_width = 480
    desired_height = 640
    frame = cv2.resize(frame, (desired_width, desired_height))

    height, width, layers = frame.shape
    print(f"Processing video {idx+1}: Frame size {width}x{height}")

    save_folder = "C:/Users/James/Videos/"  # Change this to your preferred location
    video_name = os.path.join(save_folder, f'timelapse_video_{idx+1}.avi')
    print(f"📂 Saving video to: {video_name}")
    
    fps = 15  # Frames per second
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    if not video.isOpened():
        print(f"Error: Failed to create {video_name}. Skipping this range.")
        continue

    # Add images to video
    for image in images[start:end]:
        img_path = os.path.join(folder_path, image)
        frame = cv2.imread(img_path)

        if frame is None:
            print(f"Error reading image {img_path}. Skipping.")
            continue

        frame = cv2.resize(frame, (desired_width, desired_height))
        video.write(frame)

    video.release()
    print(f"✅ Video saved as {video_name}")

cv2.destroyAllWindows()

from colorama import Fore, Style
import random
import time

confetti = ["🎉", "✨", "🎊", "🎆", "🎇"]

for _ in range(10):
    print(random.choice(confetti), end=" ", flush=True)
    time.sleep(0.1)

print(Fore.GREEN + "\n🎉 ✅ All time-lapse videos successfully created! 🎉" + Style.RESET_ALL)
