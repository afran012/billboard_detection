# Billboard Detection Project

## Overview
The Billboard Detection project is designed to detect billboards in images, calculate their real sizes, and extract text from them using advanced machine learning techniques. This project leverages PySpark for distributed data processing and TensorFlow for deep learning model inference.

## Installation Instructions
To set up the project, clone the repository and install the required dependencies. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

## Usage
To run the application, execute the `main.py` file. This will initialize a Spark session, load images, detect billboards, calculate their dimensions, and extract any text present.

```bash
python main.py
```

Make sure to update the paths in `main.py` to point to your model and image directories.

## Project Structure
```
Copybillboard_detection/
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── spark_config.py
│   │   └── model_config.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   └── preprocessing.py
│   ├── detection/
│   │   ├── __init__.py
│   │   ├── billboard_detector.py
│   │   ├── size_calculator.py
│   │   └── text_extractor.py
│   ├── model/
│   │   ├── __init__.py
│   │   ├── cnn_model.py
│   │   └── distributed_trainer.py
│   └── utils/
│       ├── __init__.py
│       ├── spark_utils.py
│       ├── calibration.py
│       └── image_utils.py
├── tests/
│   └── __init__.py
└── main.py
```

## Dependencies
The project requires the following Python packages:

- pyspark==3.3.0
- tensorflow==2.9.0
- opencv-python==4.7.0
- numpy==1.23.5
- easyocr==1.6.2
- pillow==9.5.0

## License
This project is licensed under the MIT License. See the LICENSE file for more details.