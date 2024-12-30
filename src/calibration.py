# Utility functions for camera calibration.

import cv2
import numpy as np
import os
import glob
from config import base_path

def calibrate_camera(capture_count = 30, chessboard_size = (10,7), square_size = 0.019): # square size is in meters (0.019m = 1.9cm)
    # Validate count
    if not isinstance(capture_count, int) or capture_count < 1:
        raise ValueError("capture_count must be an integer. and greater than 0")
    
    if not (isinstance(chessboard_size, tuple) and len(chessboard_size) == 2 and all(isinstance(i, int) for i in chessboard_size)):
        raise ValueError("chessboard_size must be a tuple of two integers (e.g., (7, 7)).")
    
    if not isinstance(square_size, (int, float)):
        raise ValueError("square_size must be an integer or float.")
    
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return
    
    # Step 1: Save necessary data for calibration from the camera
    
    captured_images_count = 0
    
    obj_points = []
    img_points = []

    objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2) * square_size

    print("Press 's' to save the current frame, Will not save the frame if you don't see the chessboard corners.")
    print("Press 'q' to quit the program.")

    try:
        while captured_images_count < capture_count:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame.")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

            key = cv2.waitKey(10) & 0xFF
            if ret:
                cv2.drawChessboardCorners(frame, chessboard_size, corners, ret)
                
                if key == ord('s'):
                    img_points.append(corners)
                    obj_points.append(objp)
                    captured_images_count += 1
                    print(f"Captured {captured_images_count}/{capture_count} images.")

            if key == ord('q'):
                break

            cv2.imshow('Chessboard Detection', frame)
    
    finally:
        cap.release()
        cv2.destroyAllWindows()
    
        # Step 2: Calibrate the camera and save the calibration results

        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None) 
        # We only need mtx in our case (containing focal length and principal point of the camera)

        if not ret:
            print("Error: Failed to calibrate the camera. Be sure to capture correct images.")
            return
        
        # Save the calibration results
        np.savez(os.path.join(base_path, "calibration_results.npz"), mtx=mtx, dist=dist)

        print("Camera calibration is completed successfully.")
        print(f"Calibration results are saved in {base_path}")


