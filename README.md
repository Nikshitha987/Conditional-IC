# Conditional Image Colorization

## Overview
This project implements **conditional image colorization**, which takes grayscale images and predicts realistic color versions based on learned patterns.  
It supports **real-time colorization of images and videos**, including webcam streams. The project uses **OpenCV**, **PyTorch**, and pretrained deep learning models to generate vibrant, natural colors.

This repository demonstrates both **offline colorization** and **real-time colorization with a GUI** to switch models dynamically.

---

## Features
- Colorize grayscale images and videos  
- Real-time webcam colorization  
- Multiple colorization models supported  
- Graphical User Interface (GUI) to display results  
- Preprocessing and postprocessing for high-quality outputs  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Nikshitha987/Conditional-Image-Colorization.git
cd Conditional-Image-Colorization
Create a Python virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows (PowerShell):

bash
Copy code
venv\Scripts\Activate.ps1
Windows (CMD):

bash
Copy code
venv\Scripts\activate
Linux / macOS:

bash
Copy code
source venv/bin/activate
Install required packages:

bash
Copy code
pip install -r requirements.txt
Usage
1. Colorize an Image
bash
Copy code
python colorize_image.py --input path/to/grayscale_image.jpg --output path/to/output_image.jpg
2. Colorize a Video or Webcam Stream (Real-Time)
bash
Copy code
python app.py
The GUI will open, displaying the colorized video.

Switch between colorization models if multiple are available.

Pretrained Models
Important: Large model files are not included due to GitHub size limits.

You need the following files inside the models/ folder:

colorization_deploy_v2.prototxt

colorization_release_v2.caffemodel (download from OpenCV official repo)

pts_in_hull.npy

Place them in:

text
Copy code
models/colorization_deploy_v2.prototxt
models/colorization_release_v2.caffemodel
models/pts_in_hull.npy
Project Structure
graphql
Copy code
Conditional-Image-Colorization/
│
├── models/                # Pretrained model files (download separately)
├── app.py                 # Real-time colorization GUI
├── colorize_image.py      # Script to colorize single images
├── requirements.txt       # Required Python packages
├── .gitignore             # Ignored files and folders
└── README.md              # Project documentation
