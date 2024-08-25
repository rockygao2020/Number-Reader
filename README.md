# Number-Reader
Attempt at creating a program that recognizes single handwritten digits using Singular Value Decomposition (SVD). Currently 75% accuracy (when using my own handwriting, and a sample dataset written by me).

# PyQT6 Tests
1. ![image](https://github.com/user-attachments/assets/5c4035e1-b498-4143-915e-d31753351bb1)

2. ![image](https://github.com/user-attachments/assets/262fcb31-625c-450c-94e7-e6e97b115b21)

# Test Suite (My handwriting)

```
TESTING DIGIT 0:
        Success Rate: 0.9
        Failed Cases: ['0.9.png']
TESTING DIGIT 1:
        Success Rate: 0.8
        Failed Cases: ['1.1.png', '1.10.png']
TESTING DIGIT 2:
        Success Rate: 1.0
        Failed Cases: []
TESTING DIGIT 3:
        Success Rate: 0.6
        Failed Cases: ['3.3.png', '3.4.png', '3.7.png', '3.10.png']
TESTING DIGIT 4:
        Success Rate: 1.0
        Failed Cases: []
TESTING DIGIT 5:
        Success Rate: 0.8
        Failed Cases: ['5.3.png', '5.4.png']
TESTING DIGIT 6:
        Success Rate: 0.7
        Failed Cases: ['6.4.png', '6.5.png', '6.7.png']
TESTING DIGIT 7:
        Success Rate: 1.0
        Failed Cases: []
TESTING DIGIT 8:
        Success Rate: 0.7
        Failed Cases: ['8.1.png', '8.3.png', '8.8.png']
TESTING DIGIT 9:
        Success Rate: 0.6
        Failed Cases: ['9.3.png', '9.5.png', '9.6.png', '9.9.png']
```
# Assumptions:
* Each of the 0-9 digits have 15 images that serve as data.
* Digits are processed in 20x20 pixel PNGs.
* All PNGs are colorless.

# How to Run:
* Requires the following dependencies:
```
pip install numpy
pip install matplotlib
pip install pyqt5
```
* Run the main file in CMD `python main.py`
* The `input` folder holds test cases, not the digit drawn by the user.
* The `tests` folder holds the dataset that the program depends on. Written by me, but can be replaced by any sample data by the same naming convention.

# What I Utilized:
* Basic Optical Character Recognition(OCR) and Handwritten Text Recognition(HTR) using Singular Value Decomposition(SVD).
* Linear Algebra and Matrix Computations using Numpy. 
* Python Modular Programming/Inheritance/Object-Oriented-Programming
* Basics of PyQt6 frontend, Numpy.

# Resources Used:
* PyQt6 (Frontend)
* Numpy (Matrix and SVD calculations)
