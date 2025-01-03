# Utility functions to calculate the 2 angles needed to target a point on planar surface

import numpy as np
import math
from config import cam_width, cam_height, fov_w, d1, l1, l2, robot_offset_keyboard, robot_offset_screen, robot_distance_from_plane

def pixels_to_cm(px, py):
    xc = px - (cam_width / 2)
    yc = (cam_height / 2) - py

    scale = fov_w / cam_width

    x = xc * scale
    y = yc * scale

    return x, y

def get_angles(xcm, ycm):
    px = robot_distance_from_plane
    py = xcm + robot_offset_keyboard
    pz = ycm + robot_offset_screen

    theta1 = math.atan2(py, px)
    l1c1 = l1 * math.cos(theta1)

    px_ = px - l1c1
    pz_ = pz + d1

    theta2 = math.pi - math.atan2(px_, pz_)

    mapped_theta1 = (90 - math.degrees(theta1))
    mapped_theta2 = (180 - math.degrees(theta2))

    return mapped_theta1, mapped_theta2