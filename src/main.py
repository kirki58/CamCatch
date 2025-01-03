import camera as cam
import img
import gui
import cv2
import numpy as np
import targeting as trg

gui = gui.GUI()

with cam.Camera() as camera:
    for frame in camera.capture():
        if(not gui.isStarted):
            gui.update() # Continue updating the GUI

            if not gui.running: # If the user closes the window during stop time, break the loop
                break

            continue # skip the rest of the loop
    
        if frame is None:
            raise Exception("Failed to capture frame")

        gray = img.from_bgr_to_gray(frame)
        inv = img.from_gray_to_inverted_binary(gray, threshold=gui.thresholdValue)

        # Apply Contour Filtering
        if(gui.applyContourFiltering):
            inv = img.apply_contour_filtering(inv, min_area=gui.minAreaValue)

        # Then apply Erosion or Opening
        if(gui.combobox.get() == "Erosion"):
            inv = img.apply_erosion(inv, kernel_size=gui.kernelSizeValue, iterations=gui.iterationsValue)
        elif(gui.combobox.get() == "Opening"):
            inv = cv2.morphologyEx(inv, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (gui.kernelSizeValue, gui.kernelSizeValue)), iterations=gui.iterationsValue)

        # Calculate the center of mass
        cx, cy = img.center_of_mass(inv, draw=gui.drawCenterOfMass)
        x_cm, y_cm = trg.pixels_to_cm(cx, cy)
        theta1, theta2 = trg.get_angles(x_cm, y_cm)

        gui.centerOfMassLabel.config(text=f"Center of Mass:     X:{cx},     Y:{cy}")
        gui.realPositionLabel.config(text=f"Real Position of COM:     X:{x_cm:.2f},     Y:{y_cm:.2f}")
        gui.calculatedAnglesLabel.config(text=f"Calculated Angles:     θ1:{theta1:.2f},     θ2:{theta2:.2f}")

        gui.put_gray(gray)
        gui.put_inv(inv)
        gui.update()

        if not gui.running:
            break