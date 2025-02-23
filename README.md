<div align="center">
  <h1>FoodBank Video Creator</h1>
  <p><img src="Files/img/Fridge_readme.png" alt="FoodBank Video Banner" width="200px" height="200px"></p>
  <a href="https://youtu.be/YQYi-I0GTlc"><b>📺 Watch the Time-Lapse Video</b></a>
</div>

---

## **Overview**
The **FoodBank Video Creator** is a Python-based tool designed to **generate time-lapse videos** from a sequence of images.  
Originally developed as part of a **food sustainability project at Harper Adams University**, this script enables **automated video creation**  
to document changes over time.

---

## **Table of Contents**
- [Overview](#-overview)
- [Features](#-features)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Created Video Preview](#-created-video-preview)
- [License](#-license)

---

## **Features**
✔️ **Processes images into a time-lapse video**  
✔️ **Sorts images by timestamp to ensure correct sequencing**  
✔️ **User-defined video segments for flexibility**  
✔️ **Handles missing images gracefully**  
✔️ **Saves `.avi` videos in a specified output folder**  

---

## **Installation & Setup**
### **Prerequisites**
- Python **3.x**
- OpenCV (`cv2`)

### **Installation**
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/YourUsername/FoodBank-Video-Creator.git
   cd FoodBank-Video-Creator

2. **Install dependencies**:
   ```bash
   pip install opencv-python

3. **Run the script**:
   ```bash
   python FoodBank_Video_Creator.py

## **Usage**
### **Step 1: Place Your Image Files**
- Ensure your **images are in JPG or PNG format**.
- Store them in a single directory.

### **Step 2: Run the Script**
- Open a terminal and execute:
  ```bash
  python FoodBank_Video_Creator.py
- Enter the path to the image folder when prompted.

### **Step 3: Enter Video Ranges**
- The script will prompt you to enter the start and end indices for each video.
  ```bash
  0,100
  100,200
  200,300
  done
- Once entered, the script will process and create time-lapse videos.

### **Step 4: Locate the Output Videos**
- Videos are saved in:
  ```makefile
  C:\Users\YourUsername\Videos\timelapse_video_1.avi
  C:\Users\YourUsername\Videos\timelapse_video_2.avi
-You can customize the save location in the script.

## **How It Works**
- The script processes images from a specified folder and creates time-lapse videos by following these steps:

1. **Loads images** from the user-specified folder.
2. **Sorts images** by modification timestamp to ensure correct sequencing.
3. **Prompts the user** to enter custom start and end indices for video segments.
4. **Creates `.avi` time-lapse videos** using OpenCV.
5. **Resizes frames** to a standard resolution (`480x640`).
6. **Handles missing or corrupted images** gracefully by skipping them.
7. **Saves the generated videos** in the specified output directory.
- By automating this process, the script efficiently converts large sets of images into compressed videos for analysis or presentation.

## **Created Video Preview**
Check out an example of the time-lapse video on YouTube:
[Watch the video](https://youtu.be/YQYi-I0GTlc)

## **License**
This project is licensed under the MIT License – feel free to use and modify!