# Cross Section Creator
Cross Section Creator (CSC) is a Python script used to produce cross sections from .xlsx files using the Python library Matplotlib. This README document is designed to inform the reader on how to understand, run and edit the script for your specific requirements.


## Purpose

CSC was developed by Joseph McQuade in summer 2023 for use by Portland Port Ltd. It was created specifically for the regular monitoring of the Potrland Harbour breakwaters. However, the script can be edited in order to produce cross sections for other projects if needed, though an understanding of python would be required.

* CSC can be found and cloned from the main branch on [Github](https://github.com/JoeyMcQuade/Cross-Section-Creator).

## Requirements

Python 3 is required in order to run CSC. Python can be installed from their [website](https://www.python.org/downloads/) or from the [Microsoft store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5).
* The [VS Code](https://code.visualstudio.com/) IDE was used for the entire development of this project. This README will, at points, be VS code specific. As such VS code is recomended but not required - [VS code for Python](https://www.youtube.com/watch?v=-udPvjv8jyI).
* Downloading the requirements will require PIP. PIP is automatically installed with Python 3.4+ but if there are any issue please consult the [PIP documentation](https://pip.pypa.io/en/stable/installation/).

### Requirements.txt

All of the script specific requirements are stored in the requirements.txt file. Please do not edit this file, as it contains relevant information for Python.

* I recommend installing these requirements within a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/) - [VS code tutorial](https://www.youtube.com/watch?v=GZbeL5AcTgw).

From the terminal, directed to the project folder, or from the VS code built-in terminal type:

```console
pip install -r requirements.txt
```
or if that fails try
```console
python -m pip install -r requirements.txt 
```
This will tell pip to read the requirement.txt folder and install the dependancies listed within. 

## Useage

The code is run from the CSC.py file, however, code from the ExcelData.py file is imported and called by CSC.
* CSC.py builds the cross section profiles utilising Matplotlib
* The ExcelData.py file processes and formats the relevant data from the xlsx file  