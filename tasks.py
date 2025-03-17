from celery import Celery
from datetime import timedelta
import os

app = Celery('tiktok_scheduler', broker='redis://localhost:6379/0')

@app.task
def schedule_post():
    # Call your TikTok upload script here
    os.system("python tiktok_upload.py")

# Schedule daily posts at 6 PM
app.conf.beat_schedule = {
    'post-daily': {
        'task': 'tasks.schedule_post',
        'schedule': timedelta(days=1),
        'args': (),
    },
}

if __name__ == "__main__":
    app.start()
