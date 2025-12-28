import streamlit as st
import cv2
import numpy as np
from PIL import Image

from model import get_segmentation_masks
from colorize import conditional_colorize

st.set_page_config(page_title="Conditional Image Colorization")

st.title("🎨 Conditional Image Colorization")
st.write("Colorize grayscale images based on user-defined conditions")

uploaded_file = st.file_uploader("Upload a grayscale image", type=["jpg", "png"])

def hex_to_bgr(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return (b, g, r)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")
    gray_image = np.array(image)

    st.image(gray_image, caption="Input Grayscale Image", use_container_width=True)


    st.sidebar.header("🎛️ Choose Colors")

    sky_color = st.sidebar.color_picker("Sky Color", "#4A90E2")
    grass_color = st.sidebar.color_picker("Grass Color", "#2ECC71")

    if st.button("Colorize Image"):
        with st.spinner("Colorizing..."):

            gray_bgr = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

            sky_mask, grass_mask = get_segmentation_masks(gray_bgr)

            output = conditional_colorize(
                gray_image,
                sky_mask,
                grass_mask,
                hex_to_bgr(sky_color),
                hex_to_bgr(grass_color)
            )

        
        st.image(output, caption="Conditionally Colorized Output", use_container_width=True)




