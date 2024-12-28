import cv2

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
