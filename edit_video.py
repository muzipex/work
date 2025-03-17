from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

# Load the generated video
video = VideoFileClip("robot_dance.mp4")

# Ask the user for a caption
caption = input("Enter a caption for the video: ")

# Add text caption
text = TextClip(caption, fontsize=40, color='white', font='Arial-Bold')
text = text.set_position(('center', 'top')).set_duration(video.duration)

# Add background music (ensure you have rights to use the audio!)
music = AudioFileClip("background_music.mp3").subclip(0, video.duration)
final_video = video.set_audio(music)

# Combine video and text
final_video = CompositeVideoClip([final_video, text])
final_video.write_videofile("final_tiktok_video.mp4", fps=24)
print("Edited video saved as final_tiktok_video.mp4")
