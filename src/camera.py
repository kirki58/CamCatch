import cv2

class Camera:
    def __init__(self, camera_id=0, width=640, height=480):
        self.camera = cv2.VideoCapture(camera_id)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.camera.set(cv2.CAP_PROP_FPS, 10)

    # Provides a constant stream of frames from the camera as iterable
    # Should be used with a while loop and next() function
    # check if the frame was captured successfully with the ret value
    def capture(self):
        while True:
            ret, frame = self.camera.read()
            if not ret:
                yield None
                break

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