import cv2
from config import cam_width, cam_height
class Camera:
    def __init__(self, camera_id=0, width=cam_width, height=cam_height):
        self.camera = cv2.VideoCapture(camera_id)
        if not self.camera.isOpened():
            raise Exception("Failed to open the camera.")
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # Provides a constant stream of frames from the camera as iterable
    # returns None if the camera is not able to capture a frame to provide more flexibility with handling camera errors
    def capture(self):
        while True:
            ret, frame = self.camera.read()
            if not ret:
                return None

            yield frame

    # Free the camera resource
    def release(self):
        self.camera.release()

    # Executed when the object is used in a with statement
    def __enter__(self):
        return self

    # Executed when the with statement block is exited
    def __exit__(self, exc_type, exc_value, traceback):
        self.release()
        return False