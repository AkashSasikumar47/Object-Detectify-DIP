# Object Detectify

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A simple desktop application for object detection and counting using OpenCV and Tkinter.

## Features

- Browse and select images from your file system
- Automatic object detection using contour analysis
- Visual display of detected objects with green contours
- Real-time object counting

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Object-Detectify-DIP.git
cd Object-Detectify-DIP
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

1. Click "Select Image" button
2. Choose an image file
3. View the original image (left) and detected objects (right)
4. See the count of detected objects at the bottom

## Requirements

- Python 3.7+
- OpenCV
- Pillow
- Tkinter (included with Python)

## How It Works

The application uses computer vision techniques:
1. Converts image to grayscale
2. Applies Gaussian blur to reduce noise
3. Uses Canny edge detection
4. Finds and draws contours around detected objects
5. Counts the total number of objects

## License

MIT License - see [LICENSE](LICENSE) file for details.
