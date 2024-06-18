import cv2
import os

# Define Path to Images Folder and Get Image Files with timestamp

# Ed
folder_path = r"D:\Food bank\fridgecam"
# James
# folder_path = r'C:\Users\James Simmill\Desktop\ImageLaps'
images = os.listdir(folder_path)

# Set params
minn = 5000
maxn = 5500
video_name = 'timelapse_video.avi'
fps = 20  # Frames per second

# Define Video Parameters
frame = cv2.imread(os.path.join(folder_path, images[0]))
if frame is None:
    print("Error reading the first image.")
    exit()

height, width, layers = frame.shape
print(f"Frame size: {width}x{height}")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

if not video.isOpened():
    print("Error: VideoWriter not opened.")
    exit(1)

# Add Images to the Video
for image in images[minn:maxn]:
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