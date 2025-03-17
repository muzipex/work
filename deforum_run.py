import os

# Ask the user for a text prompt
prompt = input("Enter a text prompt for the animation: ")

# Run Deforum with the user's prompt
os.system(f"python deforum_run.py --prompt '{prompt}' --output robot_dance.mp4")
