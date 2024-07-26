<div style="text-align: center;">
  <h1 style="text-decoration: underline;">FoodBank Video Creator</h1>
</div>

<div style="text-align: center;">
  <img src="Files/img/Fridge_readme.png" alt="Blog Banner" style="border-radius: 50%; width: 150px; height: 150px; object-fit: cover;">
</div>

[Check out our YouTube video](https://youtu.be/YQYi-I0GTlc)
## Description
FoodBank Video Creator is a Python script that creates multiple time-lapse videos from a series of images. This tool is useful for projects that document movement and progress over time. The script processes images from a specified directory, sorts them by modification date, and generates videos based on specified ranges.

## Table of Contents
- [Usage](#usage)
- [Configuration](#configuration)
- [Script Details](#script-details)
- [Created Video Preview](#created-video-preview)


## Usage
To create the time-lapse videos:

1. **Place Your Image Files**:
   - Place your image files in a specified directory on your local machine. Ensure that the images are in JPG format.

2. **Update the Script Configuration**:
   - Open the script file `FoodBank_Video_Creator.py`.
   - Update the `folder_path` variable to point to your image directory. For example:
     ```python
     # Define Path to Images Folder
     folder_path = r'C:\Users\James\Desktop\FoodBank_Video_Creator'

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where your script is located:
     ```bash
     cd path\to\your\script\directory
     ```
   - Run the script using Python:
     ```bash
     python timeLaps.py
     ```

4. **Output**:
   - The script will process the images and generate time-lapse videos.
   - The output videos will be saved in the same directory as the script, named `timelapse_video_1.avi`, `timelapse_video_2.avi`, etc.

### Configuration

1. **Place Your Image Files**:
   - Ensure your images are in the correct format (e.g., .jpg) and are located in the directory specified by the `folder_path`.

2. **Update the Script Configuration**:
   - Open the `FoodBank_Video_Creator.py` file in a text editor.
   - Locate the `folder_path` variable and set it to the path where your images are stored:
     ```python
     folder_path = r'C:\Users\James\Desktop\FoodBank_Video_Creator'
     ```

3. **Open Terminal or Command Prompt**:
   - On Windows: Press `Win + R`, type `cmd`, and press Enter.
   - On macOS: Press `Cmd + Space`, type `Terminal`, and press Enter.
   - On Linux: Use the application menu to open the Terminal.

4. **Navigate to the Script Directory**:
   - Use the `cd` command to change the directory to where your script is located. For example:
     ```bash
     cd C:\Users\James\Desktop\FoodBank
     ```

5. **Run the Script**:
   - Execute the script by typing the following command:
     ```bash
     python FoodBank_Video_Creator.py
     ```

6. **Check the Output**:
   - After running the script, check the output directory for the generated video files.
   - The videos will be named `timelapse_video_1.avi`, `timelapse_video_2.avi`, etc.

## Script Details

The script performs the following steps to create time-lapse videos from a series of images:

1. **Import Required Libraries**:
   - The script uses the `cv2` library from OpenCV for image processing and the `os` library for interacting with the operating system, such as reading files from a directory.

   ```python
   import cv2
   import os

2. **Define Path to Images Folder and Get Image Files with Timestamps**:
   - Set the folder_path variable to the directory where your images are stored.
   - Get a list of image files along with their modification timestamps.

   ```python
   folder_path = r'C:\Users\James\Desktop\FoodBank_Video_Creator'
   images = [
      (img, os.path.getmtime(os.path.join(folder_path, img)))
       for img in os.listdir(folder_path)
       if img.endswith(".jpg")
   ]

3. **Sort Images in the Correct Order**:
   - Sort the images by their modification date to ensure they are processed in the correct order.

   ```python
   images.sort(key=lambda x: x[1])
   images = [img[0] for img in images]

4. **Error Handling if Images Not Found**:
   - Check if any images were found in the specified directory. If not, print an error message and exit the script.

   ```python
   if not images:
    print("No images found in the specified directory.")
    exit()

5. **Define the Ranges for the Videos**:
   - Specify the ranges of images to be used for creating different videos. Each range is defined by a start and end index.

   ```python
   ranges = [(0, 900), (2500, 3400), (4100, 5000)]

6. **Loop Through Each Range and Create a Video**:
   - For each range, read and resize the images, then add them to a video file.
   - Save the video file.

   ```python
   for idx, (start, end) in enumerate(ranges):
       # Read the first image in the range to get the dimensions
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

      # Define the output video file name and parameters
      video_name = f'timelapse_video_{idx+1}.avi'
      fps = 15  # Frames per second
      fourcc = cv2.VideoWriter_fourcc(*'XVID')
      video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

      if not video.isOpened():
         print(f"Error: VideoWriter not opened for video {video_name}.")
         continue

      # Add each image in the range to the video
      for image in images[start:end]:
         img_path = os.path.join(folder_path, image)
         frame = cv2.imread(img_path)
         if frame is None:
            print(f"Error reading image {img_path}")
            continue

           # Resize the frame to the desired resolution
         frame = cv2.resize(frame, (desired_width, desired_height))
         video.write(frame)

      # Release the video writer and finalize the video
      video.release()
      print(f"Video saved as {video_name}")

   # Clean up and close any open windows
   cv2.destroyAllWindows()

## Created Video Preview

You can watch an example of the time-lapse video created using this script on YouTube:

[Watch the time-lapse video](https://youtu.be/YQYi-I0GTlc)
