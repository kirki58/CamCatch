import os

cam_width = 640 # Camera's width in pixels
cam_height = 480 # Camera's height in pixels
fov_w = 103 # Camera's FOV width in centimeters

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Robot's internal values in cms
d1 = 4
l1 = 3
l2 = 3

robot_offset_keyboard = 18.5
robot_offset_screen = 21.5
robot_distance_from_plane = 105
