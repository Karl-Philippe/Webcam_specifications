# Webcam Specs Display

This repository contains two scripts that demonstrate how to capture and display webcam specifications using both HTML/JavaScript and Python. These scripts allow you to retrieve and display information such as resolution, frame rate, aspect ratio, and megapixels of your webcam.

## Contents

- `index.html`: An HTML/JavaScript file that runs in a web browser and displays webcam specifications.
- `webcam_specs.py`: A Python script that captures and displays webcam specifications using OpenCV.
- `requirements.txt`: A file listing the Python dependencies required to run the `webcam_specs.py` script.

## Getting Started

### HTML/JavaScript (index.html)

The `index.html` file allows you to access your webcam and view its specifications directly in your web browser.

#### Features:
- Displays the resolution, megapixels, and aspect ratio for both photo and video streams.
- Shows the frame rate, bitrate, and other general information about the webcam.

#### Usage:
1. Open `index.html` in your web browser.
2. Allow the browser to access your webcam when prompted.
3. The webcam specifications will be displayed on the page.

#### Compatibility:
- This script is compatible with modern web browsers that support the `navigator.mediaDevices.getUserMedia` API.

### Python (webcam_specs.py)

The `webcam_specs.py` script uses the OpenCV library to capture and display webcam specifications in the terminal.

#### Features:
- Retrieves and displays the spatial resolution, the pixel density, the data rate, the frame rate and the aspect ratio of webcam video stream.

#### Prerequisites:
- Python 3.x

#### Installation:

1. Clone the repository or download the script.
2. Install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

#### Usage:
1. Run the script using Python:

```bash
python webcam_specs.py
```

2. The webcam specifications will be printed in the terminal.

#### Compatibility:
- This script should work on any system with a webcam and Python installed, along with OpenCV.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.