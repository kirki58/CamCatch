import camera as cam
import img
import gui

gui = gui.GUI()

with cam.Camera() as camera:
    for frame in camera.capture():
        if frame is None:
            raise Exception("Failed to capture frame")

        gray = img.from_bgr_to_gray(frame)
        inv = img.from_gray_to_inverted_binary(gray)

        gui.put_gray(gray)
        gui.put_inv(inv)
        gui.update()

        if not gui.running:
            break