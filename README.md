# Diplomat
Python code to extract CIS Benchmark controls from pdf automatically, using regex.

## Overview
There are two main files:

 - extract_controls.py will generate a csv file based on an input pdf following CIS format
 - generate_stubs.py will take the generated csv file and create a folder containing one py file for each control

 The idea is to use this as the platform to create the different controls in automated way

 ## Adjusting the Code
 On extract_controls.py, you can change the pdf file name/location and the number of pages you want to extract.
 Current code works for AWS and GCP controls. For Kubernetes it struggled with some controls where the new line char was just before the page number, happy to merge a PR if submitted.

## Execution
```
# Import dependencies
pip install -r requirements.txt
# Create csv
python extract_controls.py
# Crreate stubs from csv
python generate_stubs.py
```
