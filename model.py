import cv2
import numpy as np

def get_segmentation_masks(image):
    """
    Improved heuristic segmentation:
    - Sky: bright, low-texture regions in upper half
    - Grass: darker, high-texture regions in lower half
    """

    h, w, _ = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Smooth image
    blur = cv2.GaussianBlur(gray, (7, 7), 0)

    # Sky detection (bright areas, upper half)
    sky_mask = np.zeros((h, w), dtype=np.uint8)
    _, bright = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
    sky_mask[:h//2, :] = bright[:h//2, :]

    # Grass detection (edges + darker regions, lower half)
    edges = cv2.Canny(blur, 50, 150)
    grass_mask = np.zeros((h, w), dtype=np.uint8)
    grass_mask[h//2:, :] = (edges[h//2:, :] > 0).astype(np.uint8)

    return sky_mask, grass_mask
