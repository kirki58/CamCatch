# Contains utility functions for image processing.

import cv2
import numpy as np

# Convert image to Grayscale
# Explanation: A BGR image is received, each channel is given a weight (B = 0.114, G = 0.587, R = 0.299)
# Each channel is multiplied by the weight then summed up to obtain a single channel. Which results in a grayscale image with specified weights.
def from_bgr_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert image to inverted binary
# Explanation: A BGR image is received, converted to grayscale
# For THRESH_BINARY_INV mode, every pixel value above the threshold is set to 0, and every pixel value below the threshold is set to 255
# This results in a binary image (every pixel value 0 or 255) with inverted colors.
def from_bgr_to_inverted_binary(image, threshold=127):
    gray = from_bgr_to_gray(image)
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)
    return binary

# Convert Grayscale image to inverted binary
def from_gray_to_inverted_binary(gray, threshold=127):
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)
    return binary

# Iterate over each pixel in the inv_bin image if any neighboring pixel in kernel is 0, set the pixel to 0 
def apply_erosion(inv_bin, kernel_size = 3, iterations = 1):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    return cv2.erode(inv_bin, kernel, iterations=iterations)

# Description: We find contours in the binary image, then filter out the contours that are too small (noise)
def apply_contour_filtering(inv_bin, min_area = 100):
    # RETR_EXTERNAL retrieves only the extreme outer contours
    # CHAIN_APPROX_SIMPLE removes redundant points of the contour line, saves memory
    contours, _ = cv2.findContours(inv_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out contours that are too small
    output_image = np.zeros_like(inv_bin) # Create a black image with the same size as the input image

    for contour in contours:
        if(cv2.contourArea(contour) > min_area):
            # -1 = Draw all contours, 255 = White color, -1 = Fill the contour
            cv2.drawContours(output_image, [contour], -1, 255, -1) # Draw valid contours back to the output image, fill the contour with white
        
    return output_image

def center_of_mass(inv_bin, draw=False):
    # returns m00, m10, m01
    # m00 = sum of all pixel values
    # m10 = sum of all pixel values multiplied by their x coordinate
    # m01 = sum of all pixel values multiplied by their y coordinate
    moments = cv2.moments(inv_bin)

    # Calculate the center of mass
    if(moments["m00"] != 0):
        cx = int(moments["m10"] / moments["m00"])
        cy = int(moments["m01"] / moments["m00"])

        if(draw):
            # Draw a crosshair at the center of mass
            cv2.line(inv_bin, (cx - 10, cy), (cx + 10, cy), 255, 2)
            cv2.line(inv_bin, (cx, cy - 10), (cx, cy + 10), 255, 2)

        return cx, cy
    else:
        return -1, -1