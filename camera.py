from picamera import PiCamera
from datetime import datetime

class Camera:
    camera = PiCamera()

    def __init__(self):
        self.camera.resolution = (3280, 2464)
        self.camera.awb_mode='incandescent'

    def take_picture(self, result_path):
        self.camera.capture(result_path)

def get_timestamp_filename():
    current_date = datetime.now()
    return current_date.strftime('%Y-%m-%d') + '.jpg'
