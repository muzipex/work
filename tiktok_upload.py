from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Configure ChromeDriver
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Login to TikTok (use environment variables for credentials!)
driver.get("https://www.tiktok.com/login")
time.sleep(10)  # Manually log in once (or automate with caution)

# Upload video
driver.get("https://www.tiktok.com/upload")
time.sleep(5)

# Upload the video file
upload_button = driver.find_element(By.XPATH, "//input[@type='file']")
upload_button.send_keys(os.path.abspath("final_tiktok_video.mp4"))

# Add caption and post
caption_box = driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
caption_box.send_keys("Check out this AI-generated video! 🤖 #AI #TikTokBot")
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(text(), 'Post')]").click()

# Close the browser
time.sleep(5)
driver.quit()
print("Video uploaded to TikTok!")
