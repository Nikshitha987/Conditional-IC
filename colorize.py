import cv2
import numpy as np

def apply_color(mask, image, color):
    """
    Apply BGR color to masked region
    """
    for i in range(3):
        image[:, :, i] = np.where(mask > 0, color[i], image[:, :, i])
    return image

def conditional_colorize(gray_image, sky_mask, grass_mask, sky_color, grass_color):
    """
    Convert grayscale to color image based on conditions
    """

    color_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

    color_image = apply_color(sky_mask, color_image, sky_color)
    color_image = apply_color(grass_mask, color_image, grass_color)

    return color_image
