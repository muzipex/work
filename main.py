import os

# Step 1: Ask the user for a text prompt
prompt = input("Enter a text prompt for the video: ")

# Step 2: Generate image
os.system(f"python text_to_image.py --prompt '{prompt}'")

# Step 3: Animate image into video
os.system(f"python deforum_run.py --prompt '{prompt}' --output robot_dance.mp4")

# Step 4: Edit video
os.system("python edit_video.py")

# Step 5: Upload to TikTok
os.system("python tiktok_upload.py")
